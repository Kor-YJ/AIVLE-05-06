from rest_framework import serializers
from django.db.models import Sum
from .models import Consultation,DetailConsultation
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


# class ConsultationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Consultation
#         fields = ('id','patient_id','doctor_id','consultation_date','amount','reservation_id','description')
class ConsultationSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='doctor_id.departments_id.departments_name', read_only=True)
    consultation_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Consultation
        fields = ['id', 'patient_id','consultation_date', 'department', 'total_amount']

    def get_total_amount(self, obj):
        # 기본 진료 금액
        total_amount = obj.amount
        # 세부진료 금액 합산
        sub_consultations = DetailConsultation.objects.filter(consultation_id=obj.id)
        sub_amount = sub_consultations.aggregate(total=Sum('amount'))['total'] or 0
        return total_amount + sub_amount
    
class DetailConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailConsultation
        fields = ['name', 'amount']

class ConsultationPaySerializer(serializers.ModelSerializer):
    patient_id = PatientSerializer(read_only=True)
    doctor_id = DoctorSerializer(read_only=True)
    detailconsultations = DetailConsultationSerializer(many=True, read_only=True, source='detailconsultation_set')

    class Meta:
        model = Consultation
        fields = ['id', 'patient_id', 'doctor_id', 'consultation_date', 'amount', 'reservation_id', 'description', 'detailconsultations']
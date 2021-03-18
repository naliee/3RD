from django.db import models

# Create your models here.
class fcuser(models.Model):
    username = models.CharField(max_length=64,verbose_name='사용자명') #필드명 username을 한글 '사용자명'으로 보여줌
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    # 가입 날짜                             fcuser가 등록되는 시점이 자동으로 저장
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')


    class Meta:
        # 테이블 명 지정 (다른 앱들과 구분)
        db_table = 'fastcampus_fcuser'  

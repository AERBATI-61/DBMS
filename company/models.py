from django.db import models
class Employee(models.Model):
    choices                      = (
                                    ('lisans', 'lisans'),
                                    ('yuksek_lisans', 'yuksek_lisans'),
                                    ('doktora', 'doktora')
                                    )
    isim                         = models.CharField(max_length=64, blank=True, null=True)
    soyisim                      = models.CharField(max_length=64, blank=True, null=True)
    tc                           = models.CharField(max_length=64, blank=True, null=True)
    kan_gurubu                   = models.CharField(max_length=64, blank=True, null=True)
    dogum_yeri                   = models.CharField(max_length=64, blank=True, null=True)
    meslek                       = models.CharField(max_length=64, blank=True, null=True)
    maas                         = models.IntegerField()
    hobiler                      = models.ForeignKey('Hobiler', blank=True, null=True, on_delete=models.CASCADE)
    egitimler                    = models.CharField(max_length=128, blank=True, null=True, choices=choices)
    mesai                        = models.ForeignKey('Calisma_Durumu', blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.isim)


class Hobiler(models.Model):
    hobi1                       = models.CharField(max_length=64, blank=True, null=True)
    hobi2                       = models.CharField(max_length=64, blank=True, null=True)
    hobi3                       = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return str(self.hobi1)



class Belirtiler(models.Model):
    choices                     = (
                                    ("siddetli_oksuru", "siddetli_oksuru"),
                                    ("yuksek_ates", "yuksek_ates"),
                                    ("burun_akinti", "burun_akinti"),
                                    ("nefes_darligi", "nefes_darligi"),
                                    ("asiri_halsizlik", "asiri_halsizlik")
                                  )
    belirtiler                  = models.CharField(max_length=128, blank=True, null=True, choices=choices)


class Hastalik_Durumu(models.Model):
    hastalik_ismi               = models.CharField(max_length=128, blank=True, null=True)
    baslangic_tarih             = models.DateTimeField(auto_now=False, null=True, blank=True, help_text="if it happened")
    recete                      = models.ForeignKey('Recete', blank=True, null=True, on_delete=models.CASCADE)
    belirtiler                  = models.ForeignKey('Belirtiler', blank=True, null=True, on_delete=models.CASCADE)



class Asi(models.Model):
    asi                         = (
                                ("biontech_asi", "biontech_asi"),
                                ("sinovac_asi", "sinovac_asi"),
                                )
    hangi_asi                   = models.CharField(max_length=128, blank=True, null=True, choices=asi)

class Recete(models.Model):
    hangi_asi                   = models.ForeignKey(Asi, blank=True, null=True, on_delete=models.CASCADE)
    ilaclar                     = models.TextField()



class Covid_Durumu(models.Model):
    baslayan_tarih              = models.DateTimeField(auto_now=False, null=True, blank=True, help_text="if it happened")
    bitis_tarih                 = models.DateTimeField(auto_now=False, null=True, blank=True, help_text="if it happened")
    belirtiler                  = models.ForeignKey('Belirtiler', blank=True, null=True, on_delete=models.CASCADE)
    temasli_kisi                = models.ForeignKey('Employee', blank=True, null=True, on_delete=models.CASCADE)
    asi_durumu                  = models.BooleanField(default=False)
    hangi_asi                   = models.ForeignKey(Asi, blank=True, null=True, on_delete=models.CASCADE)
    kronik_mi                   = models.BooleanField(default=False)



class Calisma_Durumu(models.Model):
    days_of_the_week            = (
                                    ('Monday', 'Monday'),
                                    ('Tuesday', 'Tuesday'),
                                    ('Wednesday', 'Wednesday'),
                                    ('Thursday', 'Thursday'),
                                    ('Friday', 'Friday'),
                                    ('Saturday', 'Saturday'),
                                    ('Sunday', 'Sunday')
                                  )
    day                            = models.CharField(max_length=32, blank=True, null=True, choices=days_of_the_week)
    start_time                     = models.TimeField(auto_now_add=False)
    end_time                       = models.TimeField(auto_now_add=False)
    employee                       = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE)



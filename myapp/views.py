from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def profile(request):
    return render(request, "profile.html")

def shader_background_view(request):
    return render(request, 'shader_background.html')

def about(request):
    return render(request, 'about.html')


def projects(request):
    battery_images = [
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACO8N87W4gEMim2RYGKYA3XJZbdpaOQjrRBk46G2EKmMzzqkivBdzWP0aubLWmjBh3vIDMnWZ_HxXfwmPTlg_0AFoYe8KhaZu7uvM4VtlvaUTMO6p17F9PrMYfkQGWhvIrK7zE82araG_8By_mk3YEsH0D0BtKBvTLuXCDiYhFBniSoAAAZEG4827NFzi9qjE5RIPO8GJybXX6mMl8n6GTfDzd0mb8xMm6jJvuiC3DZ6qtlgj25YJ7Yl66QDjsMJE8POQOfkt51hzCLGQkaoHWKSOyArlbKVZAxv_fYmgnDTUOw2pveHljmN4snnTfkdnTng1cYA2dGWPjXcA7k-AOTZ/p.jpeg',
            'description': 'Battery Image 1'},
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACOGfZiU1Ww8MQ038BKoKZYAuw42nkTFT6JWmq2gwLzXK8IMyh1Hhi0qe6rL74ov4lNp5BPBr0pF5RSNKC0-JmleMv1jE0Qd41D8eK5_DgV_KD3P_EGd04nRvmn3yXTc03ctOMcvkVA0uDsmJ5sPb7FPRD1jAbGpPVuReyu6lomNSkLtcmIsJJISD83NVqJsVp2THZoCWXB43MLK3jY42hf2MjfGrh5sVbVjUI0UUPi5QQb4P2-VyUPggXVY0td7SNspWW-r8yEX2iBu10bBnWL6JblYbQ-HrbvgrdBdP9Re3cEhGQa7AW7Dn-O6RrxOJbioKLa3UvwldrsV7_P3m1Mq/p.jpeg',
            'description': 'Battery Image 2'},
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACPR9rpsEkDTh3bZIjC-nWnUSIoh3RntDJgjVVL_j1GAD0prWRdH3A_bNTqF3IFw1W-fKUhiqNOclmIuZOz0ISCd7qGpiqP-HzQfkL35lVReJxF3Nn76WE3YmN6S1imHx2g-rv9RUMLZ3HRwONmH9dsWofAtMt0bbqupY3mWoEdC1SHu6QsUJFsntiyPGFw6m8hUOk3OfY45a8mg_rfhI4urJ57p0oLJ4V_IYHthRuObVruHwHg0er9jUMgU9HKqxUNUmZNeAy_Cb-tCphZu6i90J3rp8xBjuoAzLB3tdkcfWEpLATHmbD4rrNRZUhTpuihsn_ea3S3baWya3Nx4r2ic/p.jpeg',
            'description': 'Battery Image 3'},
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACOuxG1bnTEUxSdFCA774L1aNFh6CYmsXeTlqXZbzbF1jSh1xMu28znHIbaXYqwaPaFsjTPETGNXAkD4c5bqQTbAj5NzcM-FUeHmwiNX7Vm4HWTB2NUedHapd3TBJNkGpXA01TTjDUnxT5Ge_QwW5_lJRVl6eBQoeyGvskzt6JmWSKOa76B7DAv9DASvw5sfaUuh-fx78PJp8m8RTGdV9oGZT2AG3FQAUNRiCyuQhQbH7UfI9esICYeTwuC_a-n6bKqcC66TLMhx3ZAB4zcsUfYBwqmmPDIkxbDYRpuU9x9lqqTn5QUqByVVD9GqVcz2vfbMtgLbLLZHq8F-5brukEqr/p.jpeg',
            'description': 'Battery Image 4'},
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACO7QMj3DurDjsjR13l53-CyE6rFIxrWlir2C5xISZYRcYSjnMvjyuwESG4trR9eT03XK5icQW1nwhmqjpzHsVjVr7ZElbBLJgGXDkdKdTwo9x0i129adm-oSUTKDGYOYk0CSHQRWwFJh_M3F9ha0epe5W6--KISe0v5iZU0OophUtScoze6xd-3fpJxL9st_CA8767sUM35uV0Fy-7XpSKlsSQnaBLt6-yWTOah9PQrmMEeP6RV3QZ3p3FNR5XVfaMhZOfz8aN_XBnhniHcxSCw6K89lFufv-cU5TXRs34l_Q1gtGRrIeAX37TzhDo43MDbRx7wcfYuyUW4DFLzotsE/p.jpeg',
            'description': 'Battery Image 5'},
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACNPik8X2ebdwfCrZv1OAkbWtUAiECMmRIvlacje0jiy7l5qsZ-fbqCdRNTPNv3UiynOHj3K6eFec5Qmr7ST_H0c1t_YOgk0s_vLiQhCX7JDT5UoWiNzLZXuuaSAaS4Soikbexbebb5UJc7iUW22xUhzIb-sYrkjKB4Jf1-wvI9FUY79ZUr9sZYpr_5RqYM_ogiNtWt1aq2Ck58rwzTB-MTTLX-mHxO22bqcbvPH-C2ZmMnumuM6JD7dBM_IYgHNKB4NifEmIS9dpPWLk1NmOFm4Rr-K4yFOLY8NkY3c20MQ9ipn2nVrB32VXozZJxz1mOYKmJzRpl5ZvcnFfVfbwyoA/p.jpeg',
            'description': 'Battery Image 6'},
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACOlADu9ET8fEuznVvbAZOk_1s7gj7ohX5lCY5HfN7KOIst9gDQnz4fk-NA-v0RUJ2d4JN3qZ2s3mo3p78ZwRJpDanaSb5E5FlPLhtA7vSX2Rn4D0wx1YFrAU2GNWV1fL1lKfA7k-vuqZqrwoD4t6jr1TSg1Bc6KJLh8EvnjaQz0AarhOYoiE2AutbmI0t11K29IALbz9yec2cv22_jp2EObPgIcqAIT8Eayhy_hHZ3R1HrvOXmKMkvCsKjh2AsFoA75uhDo-1DJfCIhDfm3_vr1RauEB7Jl2FPNUSNzAkwrDzNjl8JYyP3f9X3EehMfyIUsz9PV5Za4qxzYemaiNsrX/p.jpeg',
            'description': 'Battery Image 7'},
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACPHMyiDOpMyUh5yzUs_SThH9VyEgLJWobqOZgNC95YzfBK3GYb5vT-p0p2tSYaREhVq9Hxqvn5OqbVIzccidX1wVmKcW7Vui21hKP5qCpxn2HO2BL--NsSL4SE7gKYFP6Pd_cSMssOvLSJD1eXSilYdr7PT4RvnKPTN5p36Yov4yGQtLpXZtNtqQDxOEbKd6SvuOb11fB5ipTjxz5NRByAJT8Px9PJobmg7LqgKHARo9giDR1AISdIKj1PCsP-WgoAPChjhRmoNbOSADGXfPTj3R4zs2ozi_5aRNSvWYEjn_-BJsyG3fjCBl_PHEHfoNRXGCSSI-fqGno4RXVEn0uhU/p.jpeg',
            'description': 'Battery Image 8'},
        {
            'url': 'https://previews.dropbox.com/p/thumb/ACO0ki88LDEljN1OYry_PqTkStle2F-uvyENM4AKkXfUv95Yy2CxbzzghdQ917vl_8rhg6F5Lbg6OTAZqgbluJeT4FXclgAEPw9MfhEuYik6RltyQyQf5ERrG95s9jEO2rjqfRxAaxYsahcfsnAIlsToTCZ9fdPSXyDz-I3Ee2loDMpX4o7L_ZnodxDuPAVcaF5CoXZZCNQ3pvuq4stoXSVRZ9nkTrImmEBjfDctUE0oMAvEGXSJQVg26Heeinc3g0fHHysY1GRsi-ZNaZomyU6ZmIHLMQ3KuOUeFO-2PYNsR1gZ5MH3kXl3DwkzABzkcH0dJqc9gbzMzL9L_BmkniYd/p.jpeg',
            'description': 'Battery Image 9'}
    ]

    return render(request, 'projects.html', {'battery_images': battery_images})


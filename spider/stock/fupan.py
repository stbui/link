import requests
from bs4 import BeautifulSoup


def getHtml(id):
    url = id
    # url = 'https://www.taoguba.com.cn/Article/'+id+'/1'
    res = requests.get(url=url)
    return res.text


def parse(text):
    soup = BeautifulSoup(text, 'lxml')

    imgs = soup.find(id="first").find_all('img')

    newImags = ""
    for img in imgs:
        newImags += '   <img src="{}" />'.format(img.get('src2'))
    return newImags


def render(tags, text):
    # date = time.strftime("%Y-%m-%d", time.localtime())
    soup = BeautifulSoup(text, 'lxml')
    date = soup.select(".comment-content .pcyclspan")[0].get_text().split()[0]
    print(date)
    file_name = date+'.html'

    tpl = '''<html><header><title>{date}复盘</title><style></style></header><body><div id="start"></div>{body}<div id="end"></div><script src="./js.js"></script></body></html>'''
    tpl_css = '''<style>*{margin: 0}</style>'''

    html = tpl.format(date=date, body=tags).replace(
        '<style></style>', tpl_css)

    prefix_path = 'html/stock/'
    with open(prefix_path+file_name, 'w+') as f:
        f.write(html)


def start(id):
    res = getHtml(id)
    images = parse(res)
    render(images, res)
    print('干完了')


# var ls=[]
# $('.yinchan').map((i,item)=>{
#     ls.push('https://www.taoguba.com.cn/'+$(item).attr('href'))
# });
# copy(ls)
# https://www.taoguba.com.cn/blog/2824341

links = [
    "https://www.taoguba.com.cn/Article/4479250/1",
    "https://www.taoguba.com.cn/Article/4475726/1",
    "https://www.taoguba.com.cn/Article/4472469/1",
    "https://www.taoguba.com.cn/Article/4472437/1",
    "https://www.taoguba.com.cn/Article/4468285/1",
    "https://www.taoguba.com.cn/Article/4464685/1",
    "https://www.taoguba.com.cn/Article/4459409/1",
    "https://www.taoguba.com.cn/Article/4455966/1",
    "https://www.taoguba.com.cn/Article/4452614/1",

    "https://www.taoguba.com.cn/Article/4448805/1"
    "https://www.taoguba.com.cn/Article/4445339/1",
    "https://www.taoguba.com.cn/Article/4439228/1",
    "https://www.taoguba.com.cn/Article/4435198/1",
    "https://www.taoguba.com.cn/Article/4431694/1",
    "https://www.taoguba.com.cn/Article/4426870/1",
    "https://www.taoguba.com.cn/Article/4423363/1",
    "https://www.taoguba.com.cn/Article/4416914/1",
    "https://www.taoguba.com.cn/Article/4412837/1",
    "https://www.taoguba.com.cn/Article/4409264/1",
    "https://www.taoguba.com.cn/Article/4405409/1",
    "https://www.taoguba.com.cn/Article/4402258/1",
    "https://www.taoguba.com.cn/Article/4396775/1",
    "https://www.taoguba.com.cn/Article/4393438/1",
    "https://www.taoguba.com.cn/Article/4389976/1",
    "https://www.taoguba.com.cn/Article/4386408/1",
    "https://www.taoguba.com.cn/Article/4382821/1",
    "https://www.taoguba.com.cn/Article/4382779/1",
    "https://www.taoguba.com.cn/Article/4377323/1",
    "https://www.taoguba.com.cn/Article/4373985/1",
    "https://www.taoguba.com.cn/Article/4370520/1",
    "https://www.taoguba.com.cn/Article/4367148/1",
    "https://www.taoguba.com.cn/Article/4363991/1",
    "https://www.taoguba.com.cn/Article/4358522/1",
    "https://www.taoguba.com.cn/Article/4355401/1",
    "https://www.taoguba.com.cn/Article/4351994/1",
    "https://www.taoguba.com.cn/Article/4348723/1",
    "https://www.taoguba.com.cn/Article/4345610/1",
    "https://www.taoguba.com.cn/Article/4340320/1",
    "https://www.taoguba.com.cn/Article/4337003/1",
    "https://www.taoguba.com.cn/Article/4333715/1",
    "https://www.taoguba.com.cn/Article/4330904/1",
    "https://www.taoguba.com.cn/Article/4327573/1",
    "https://www.taoguba.com.cn/Article/4325144/1",
    "https://www.taoguba.com.cn/Article/4318404/1",
    "https://www.taoguba.com.cn/Article/4315642/1",
    "https://www.taoguba.com.cn/Article/4312840/1",
    "https://www.taoguba.com.cn/Article/4309698/1",
    "https://www.taoguba.com.cn/Article/4307006/1",
    "https://www.taoguba.com.cn/Article/4302334/1",
    "https://www.taoguba.com.cn/Article/4299347/1",
    "https://www.taoguba.com.cn/Article/4296257/1",
    "https://www.taoguba.com.cn/Article/4293105/1",
    "https://www.taoguba.com.cn/Article/4289845/1",
    "https://www.taoguba.com.cn/Article/4284780/1",
    "https://www.taoguba.com.cn/Article/4281779/1",
    "https://www.taoguba.com.cn/Article/4278692/1",
    "https://www.taoguba.com.cn/Article/4275315/1",
    "https://www.taoguba.com.cn/Article/4269706/1",
    "https://www.taoguba.com.cn/Article/4266504/1",
    "https://www.taoguba.com.cn/Article/4263179/1",
    "https://www.taoguba.com.cn/Article/4259701/1",
    "https://www.taoguba.com.cn/Article/4256174/1",
    "https://www.taoguba.com.cn/Article/4250939/1",
    "https://www.taoguba.com.cn/Article/4250847/1",
    "https://www.taoguba.com.cn/Article/4250760/1",
    "https://www.taoguba.com.cn/Article/4250634/1",
    "https://www.taoguba.com.cn/Article/4236700/1",
    "https://www.taoguba.com.cn/Article/4231529/1",
    "https://www.taoguba.com.cn/Article/4228040/1",
    "https://www.taoguba.com.cn/Article/4224506/1",
    "https://www.taoguba.com.cn/Article/4221193/1",
    "https://www.taoguba.com.cn/Article/4217031/1",
    "https://www.taoguba.com.cn/Article/4211326/1",
    "https://www.taoguba.com.cn/Article/4207507/1",
    "https://www.taoguba.com.cn/Article/4203474/1",
    "https://www.taoguba.com.cn/Article/4199761/1",
    "https://www.taoguba.com.cn/Article/4196095/1",
    "https://www.taoguba.com.cn/Article/4189707/1",
    "https://www.taoguba.com.cn/Article/4185737/1",
    "https://www.taoguba.com.cn/Article/4181836/1",
    "https://www.taoguba.com.cn/Article/4177929/1",
    "https://www.taoguba.com.cn/Article/4174204/1",
    "https://www.taoguba.com.cn/Article/4167814/1",
    "https://www.taoguba.com.cn/Article/4164193/1",
    "https://www.taoguba.com.cn/Article/4160204/1",
    "https://www.taoguba.com.cn/Article/4156207/1",
    "https://www.taoguba.com.cn/Article/4152029/1",
    "https://www.taoguba.com.cn/Article/4144382/1",
    "https://www.taoguba.com.cn/Article/4140227/1",
    "https://www.taoguba.com.cn/Article/4135876/1",
    "https://www.taoguba.com.cn/Article/4131753/1",
    "https://www.taoguba.com.cn/Article/4127653/1",
    "https://www.taoguba.com.cn/Article/4120944/1",
    "https://www.taoguba.com.cn/Article/4116391/1",
    "https://www.taoguba.com.cn/Article/4112527/1",
    "https://www.taoguba.com.cn/Article/4108196/1",
    "https://www.taoguba.com.cn/Article/4104260/1",
    "https://www.taoguba.com.cn/Article/4097959/1",
    "https://www.taoguba.com.cn/Article/4094233/1",
    "https://www.taoguba.com.cn/Article/4090276/1",
    "https://www.taoguba.com.cn/Article/4085185/1",
    "https://www.taoguba.com.cn/Article/4081181/1",
    "https://www.taoguba.com.cn/Article/4074593/1",
    "https://www.taoguba.com.cn/Article/4070438/1",
    "https://www.taoguba.com.cn/Article/4066359/1",
    "https://www.taoguba.com.cn/Article/4062551/1",
    "https://www.taoguba.com.cn/Article/4059009/1",
    "https://www.taoguba.com.cn/Article/4053238/1",
    "https://www.taoguba.com.cn/Article/4049452/1",
    "https://www.taoguba.com.cn/Article/4045676/1",
    "https://www.taoguba.com.cn/Article/4041833/1",
    "https://www.taoguba.com.cn/Article/4038337/1",
    "https://www.taoguba.com.cn/Article/4032679/1",
    "https://www.taoguba.com.cn/Article/4029363/1",
    "https://www.taoguba.com.cn/Article/4025618/1",
    "https://www.taoguba.com.cn/Article/4022085/1",
    "https://www.taoguba.com.cn/Article/4018764/1",
    "https://www.taoguba.com.cn/Article/4014525/1"
]

for key in links:
    start(key)

# start('https://www.taoguba.com.cn/Article/4409264/1')
# start('https://www.taoguba.com.cn/Article/4405409/1')
# start('https://www.taoguba.com.cn/Article/4402258/1')

# 10
# start('https://www.taoguba.com.cn/Article/4373985/1')

# start('https://www.taoguba.com.cn/Article/4367148/1')
# start('https://www.taoguba.com.cn/Article/4363991/1')
# start('https://www.taoguba.com.cn/Article/4358522/1')
# start('https://www.taoguba.com.cn/Article/4355401/1')
# start('https://www.taoguba.com.cn/Article/4351994/1')
# start('https://www.taoguba.com.cn/Article/4348723/1')
# start('https://www.taoguba.com.cn/Article/4345610/1')
# start('https://www.taoguba.com.cn/Article/4340320/1')
# start('https://www.taoguba.com.cn/Article/4337003/1')
# start('https://www.taoguba.com.cn/Article/4333715/1')
# start('https://www.taoguba.com.cn/Article/4330904/1')
# start('https://www.taoguba.com.cn/Article/4327573/1')
# start('https://www.taoguba.com.cn/Article/4325144/1')

# 7
# start('https://www.taoguba.com.cn/Article/4097959/1')
# start('https://www.taoguba.com.cn/Article/4094233/1')
# start('https://www.taoguba.com.cn/Article/4090276/1')
# start('https://www.taoguba.com.cn/Article/4085185/1')
# start('https://www.taoguba.com.cn/Article/4081181/1')
# start('https://www.taoguba.com.cn/Article/4074593/1')
# start('https://www.taoguba.com.cn/Article/4070438/1')
# start('https://www.taoguba.com.cn/Article/4066359/1')
# start('https://www.taoguba.com.cn/Article/4062551/1')
# start('https://www.taoguba.com.cn/Article/4059009/1')
# start('https://www.taoguba.com.cn/Article/4053238/1')
# start('https://www.taoguba.com.cn/Article/4049452/1')
# start('https://www.taoguba.com.cn/Article/4045676/1')
# start('https://www.taoguba.com.cn/Article/4041833/1')
# start('https://www.taoguba.com.cn/Article/4038337/1')
# start('https://www.taoguba.com.cn/Article/4032679/1')
# start('https://www.taoguba.com.cn/Article/4029363/1')
# start('https://www.taoguba.com.cn/Article/4025618/1')
# start('https://www.taoguba.com.cn/Article/4022085/1')
# start('https://www.taoguba.com.cn/Article/4018764/1')
# start('https://www.taoguba.com.cn/Article/4014525/1')
# start('https://www.taoguba.com.cn/Article/4009757/1')
# start('https://www.taoguba.com.cn/Article/4006184/1')
# start('https://www.taoguba.com.cn/Article/4002587/1')
# start('https://www.taoguba.com.cn/Article/3999041/1')
# start('https://www.taoguba.com.cn/Article/3993213/1')
# start('https://www.taoguba.com.cn/Article/3989768/1')
# start('https://www.taoguba.com.cn/Article/3986141/1')
# start('https://www.taoguba.com.cn/Article/3982390/1')
# start('https://www.taoguba.com.cn/Article/3978870/1')
# start('https://www.taoguba.com.cn/Article/3972174/1')
# start('https://www.taoguba.com.cn/Article/3968491/1')
# start('https://www.taoguba.com.cn/Article/3964600/1')
# start('https://www.taoguba.com.cn/Article/3960867/1')
# start('https://www.taoguba.com.cn/Article/3955048/1')
# start('https://www.taoguba.com.cn/Article/3951539/1')
# start('https://www.taoguba.com.cn/Article/3948068/1')
# start('https://www.taoguba.com.cn/Article/3944352/1')
# start('https://www.taoguba.com.cn/Article/3940633/1')
# start('https://www.taoguba.com.cn/Article/3934787/1')
# start('https://www.taoguba.com.cn/Article/3931125/1')
# start('https://www.taoguba.com.cn/Article/3927428/1')
# start('https://www.taoguba.com.cn/Article/3923660/1')
# start('https://www.taoguba.com.cn/Article/3919909/1')
# start('https://www.taoguba.com.cn/Article/3913617/1')
# start('https://www.taoguba.com.cn/Article/3910047/1')
# start('https://www.taoguba.com.cn/Article/3905777/1')
# start('https://www.taoguba.com.cn/Article/3901492/1')
# start('https://www.taoguba.com.cn/Article/3897194/1')
# start('https://www.taoguba.com.cn/Article/3890102/1')


# start('https://www.taoguba.com.cn/Article/3886635/1')
# start('https://www.taoguba.com.cn/Article/3877632/1')
# start('https://www.taoguba.com.cn/Article/3874515/1')
# start('https://www.taoguba.com.cn/Article/3871057/1')
# start('https://www.taoguba.com.cn/Article/3867601/1')
# start('https://www.taoguba.com.cn/Article/3864284/1')
# start('https://www.taoguba.com.cn/Article/3857619/1')
# start('https://www.taoguba.com.cn/Article/3854015/1')
# start('https://www.taoguba.com.cn/Article/3850289/1')
# start('https://www.taoguba.com.cn/Article/3846732/1')
# start('https://www.taoguba.com.cn/Article/3842884/1')
# start('https://www.taoguba.com.cn/Article/3835904/1')
# start('https://www.taoguba.com.cn/Article/3831958/1')
# start('https://www.taoguba.com.cn/Article/3828155/1')
# start('https://www.taoguba.com.cn/Article/3824242/1')
# start('https://www.taoguba.com.cn/Article/3820624/1')
# start('https://www.taoguba.com.cn/Article/3814719/1')
# start('https://www.taoguba.com.cn/Article/3811337/1')
# start('https://www.taoguba.com.cn/Article/3808010/1')
# start('https://www.taoguba.com.cn/Article/3801399/1')
# start('https://www.taoguba.com.cn/Article/3796493/1')
# start('https://www.taoguba.com.cn/Article/3793295/1')
# start('https://www.taoguba.com.cn/Article/3790023/1')
# start('https://www.taoguba.com.cn/Article/3787125/1')
# start('https://www.taoguba.com.cn/Article/3782183/1')
# start('https://www.taoguba.com.cn/Article/3779142/1')
# start('https://www.taoguba.com.cn/Article/3775946/1')
# start('https://www.taoguba.com.cn/Article/3774049/1')
# start('https://www.taoguba.com.cn/Article/3769989/1')
# start('https://www.taoguba.com.cn/Article/3764933/1')
# start('https://www.taoguba.com.cn/Article/3762017/1')
# start('https://www.taoguba.com.cn/Article/3759932/1')
# start('https://www.taoguba.com.cn/Article/3755725/1')
# start('https://www.taoguba.com.cn/Article/3752846/1')
# start('https://www.taoguba.com.cn/Article/3748069/1')
# start('https://www.taoguba.com.cn/Article/3745294/1')
# start('https://www.taoguba.com.cn/Article/3742382/1')
# start('https://www.taoguba.com.cn/Article/3739129/1')
# start('https://www.taoguba.com.cn/Article/3736166/1')
# start('https://www.taoguba.com.cn/Article/3731544/1')
# start('https://www.taoguba.com.cn/Article/3728603/1')
# start('https://www.taoguba.com.cn/Article/3725747/1')
# start('https://www.taoguba.com.cn/Article/3722909/1')
# start('https://www.taoguba.com.cn/Article/3720105/1')
# start('https://www.taoguba.com.cn/Article/3716043/1')
# start('https://www.taoguba.com.cn/Article/3713711/1')
# start('https://www.taoguba.com.cn/Article/3710911/1')
# start('https://www.taoguba.com.cn/Article/3707912/1')
# start('https://www.taoguba.com.cn/Article/3704957/1')
# start('https://www.taoguba.com.cn/Article/3699940/1')

# start('https://www.taoguba.com.cn/Article/3697328/1')
# start('https://www.taoguba.com.cn/Article/3694505/1')
# start('https://www.taoguba.com.cn/Article/3691444/1')
# start('https://www.taoguba.com.cn/Article/3688647/1')
# start('https://www.taoguba.com.cn/Article/3683664/1')
# start('https://www.taoguba.com.cn/Article/3680730/1')
# start('https://www.taoguba.com.cn/Article/3677905/1')
# start('https://www.taoguba.com.cn/Article/3675358/1')
# start('https://www.taoguba.com.cn/Article/3672702/1')
# start('https://www.taoguba.com.cn/Article/3665459/1')
# start('https://www.taoguba.com.cn/Article/3663495/1')
# start('https://www.taoguba.com.cn/Article/3661230/1')
# start('https://www.taoguba.com.cn/Article/3659122/1')
# start('https://www.taoguba.com.cn/Article/3656851/1')
# start('https://www.taoguba.com.cn/Article/3653689/1')
# start('https://www.taoguba.com.cn/Article/3650099/1')
# start('https://www.taoguba.com.cn/Article/3647185/1')
# start('https://www.taoguba.com.cn/Article/3644573/1')
# start('https://www.taoguba.com.cn/Article/3641788/1')
# start('https://www.taoguba.com.cn/Article/3637155/1')
# start('https://www.taoguba.com.cn/Article/3633905/1')
# start('https://www.taoguba.com.cn/Article/3629800/1')
# start('https://www.taoguba.com.cn/Article/3626881/1')
# start('https://www.taoguba.com.cn/Article/3623749/1')
# start('https://www.taoguba.com.cn/Article/3620519/1')
# start('https://www.taoguba.com.cn/Article/3615321/1')
# start('https://www.taoguba.com.cn/Article/3611788/1')
# start('https://www.taoguba.com.cn/Article/3607697/1')
# start('https://www.taoguba.com.cn/Article/3596033/1')
# start('https://www.taoguba.com.cn/Article/3593065/1')
# start('https://www.taoguba.com.cn/Article/3590436/1')
# start('https://www.taoguba.com.cn/Article/3588045/1')
# start('https://www.taoguba.com.cn/Article/3585588/1')
# start('https://www.taoguba.com.cn/Article/3581328/1')
# start('https://www.taoguba.com.cn/Article/3578716/1')
# start('https://www.taoguba.com.cn/Article/3575801/1')
# start('https://www.taoguba.com.cn/Article/3572736/1')
# start('https://www.taoguba.com.cn/Article/3569788/1')
# start('https://www.taoguba.com.cn/Article/3564903/1')
# start('https://www.taoguba.com.cn/Article/3562081/1')
# start('https://www.taoguba.com.cn/Article/3559532/1')
# start('https://www.taoguba.com.cn/Article/3555635/1')
# start('https://www.taoguba.com.cn/Article/3552836/1')
# start('https://www.taoguba.com.cn/Article/3548025/1')
# start('https://www.taoguba.com.cn/Article/3545217/1')
# start('https://www.taoguba.com.cn/Article/3542607/1')
# start('https://www.taoguba.com.cn/Article/3539633/1')
# start('https://www.taoguba.com.cn/Article/3537128/1')
# start('https://www.taoguba.com.cn/Article/3534077/1')
# start('https://www.taoguba.com.cn/Article/3530424/1')

# start('https://www.taoguba.com.cn/Article/3528029/1')
# start('https://www.taoguba.com.cn/Article/3525240/1')
# start('https://www.taoguba.com.cn/Article/3522843/1')
# start('https://www.taoguba.com.cn/Article/3521220/1')
# start('https://www.taoguba.com.cn/Article/3516708/1')
# start('https://www.taoguba.com.cn/Article/3514310/1')
# start('https://www.taoguba.com.cn/Article/3513471/1')
# start('https://www.taoguba.com.cn/Article/3509499/1')
# start('https://www.taoguba.com.cn/Article/3505791/1')
# start('https://www.taoguba.com.cn/Article/3503627/1')
# start('https://www.taoguba.com.cn/Article/3501424/1')
# start('https://www.taoguba.com.cn/Article/3499330/1')
# start('https://www.taoguba.com.cn/Article/3497234/1')
# start('https://www.taoguba.com.cn/Article/3495468/1')
# start('https://www.taoguba.com.cn/Article/3491530/1')
# start('https://www.taoguba.com.cn/Article/3490029/1')
# start('https://www.taoguba.com.cn/Article/3487502/1')
# start('https://www.taoguba.com.cn/Article/3485615/1')
# start('https://www.taoguba.com.cn/Article/3482231/1')
# start('https://www.taoguba.com.cn/Article/3480273/1')
# start('https://www.taoguba.com.cn/Article/3478196/1')
# start('https://www.taoguba.com.cn/Article/3476134/1')
# start('https://www.taoguba.com.cn/Article/3474225/1')
# start('https://www.taoguba.com.cn/Article/3470922/1')
# start('https://www.taoguba.com.cn/Article/3469032/1')
# start('https://www.taoguba.com.cn/Article/3467094/1')
# start('https://www.taoguba.com.cn/Article/3465264/1')
# start('https://www.taoguba.com.cn/Article/3463468/1')
# start('https://www.taoguba.com.cn/Article/3460569/1')
# start('https://www.taoguba.com.cn/Article/3458788/1')
# start('https://www.taoguba.com.cn/Article/3456809/1')
# start('https://www.taoguba.com.cn/Article/3455188/1')
# start('https://www.taoguba.com.cn/Article/3453184/1')
# start('https://www.taoguba.com.cn/Article/3450147/1')
# start('https://www.taoguba.com.cn/Article/3448442/1')
# start('https://www.taoguba.com.cn/Article/3446371/1')
# start('https://www.taoguba.com.cn/Article/3445759/1')
# start('https://www.taoguba.com.cn/Article/3361928/1')
# start('https://www.taoguba.com.cn/Article/3358811/1')
# start('https://www.taoguba.com.cn/Article/3357649/1')
# start('https://www.taoguba.com.cn/Article/3355528/1')
# start('https://www.taoguba.com.cn/Article/3353968/1')
# start('https://www.taoguba.com.cn/Article/3352308/1')
# start('https://www.taoguba.com.cn/Article/3349527/1')
# start('https://www.taoguba.com.cn/Article/3347857/1')
# start('https://www.taoguba.com.cn/Article/3346278/1')
# start('https://www.taoguba.com.cn/Article/3344655/1')
# start('https://www.taoguba.com.cn/Article/3342894/1')
# start('https://www.taoguba.com.cn/Article/3340431/1')
# start('https://www.taoguba.com.cn/Article/3338589/1')

# start('https://www.taoguba.com.cn/Article/3336975/1')
# start('https://www.taoguba.com.cn/Article/3335262/1')
# start('https://www.taoguba.com.cn/Article/3333709/1')
# start('https://www.taoguba.com.cn/Article/3333688/1')
# start('https://www.taoguba.com.cn/Article/3331235/1')
# start('https://www.taoguba.com.cn/Article/3330378/1')
# start('https://www.taoguba.com.cn/Article/3328142/1')
# start('https://www.taoguba.com.cn/Article/3326753/1')
# start('https://www.taoguba.com.cn/Article/3326696/1')
# start('https://www.taoguba.com.cn/Article/3326686/1')
# start('https://www.taoguba.com.cn/Article/3303087/1')
# start('https://www.taoguba.com.cn/Article/3302159/1')
# start('https://www.taoguba.com.cn/Article/3300730/1')
# start('https://www.taoguba.com.cn/Article/3298304/1')
# start('https://www.taoguba.com.cn/Article/3295732/1')
# start('https://www.taoguba.com.cn/Article/3294342/1')
# start('https://www.taoguba.com.cn/Article/3292798/1')
# start('https://www.taoguba.com.cn/Article/3291489/1')
# start('https://www.taoguba.com.cn/Article/3290054/1')
# start('https://www.taoguba.com.cn/Article/3287428/1')
# start('https://www.taoguba.com.cn/Article/3285674/1')
# start('https://www.taoguba.com.cn/Article/3285099/1')
# start('https://www.taoguba.com.cn/Article/3282539/1')
# start('https://www.taoguba.com.cn/Article/3281198/1')
# start('https://www.taoguba.com.cn/Article/3278654/1')
# start('https://www.taoguba.com.cn/Article/3276874/1')
# start('https://www.taoguba.com.cn/Article/3275333/1')
# start('https://www.taoguba.com.cn/Article/3273694/1')
# start('https://www.taoguba.com.cn/Article/3271240/1')
# start('https://www.taoguba.com.cn/Article/3269685/1')
# start('https://www.taoguba.com.cn/Article/3268267/1')
# start('https://www.taoguba.com.cn/Article/3266722/1')
# start('https://www.taoguba.com.cn/Article/3265178/1')
# start('https://www.taoguba.com.cn/Article/3263807/1')
# start('https://www.taoguba.com.cn/Article/3261509/1')
# start('https://www.taoguba.com.cn/Article/3260255/1')
# start('https://www.taoguba.com.cn/Article/3258393/1')
# start('https://www.taoguba.com.cn/Article/3256978/1')
# start('https://www.taoguba.com.cn/Article/3254509/1')
# start('https://www.taoguba.com.cn/Article/3253046/1')
# start('https://www.taoguba.com.cn/Article/3251967/1')
# start('https://www.taoguba.com.cn/Article/3250255/1')
# start('https://www.taoguba.com.cn/Article/3248121/1')
# start('https://www.taoguba.com.cn/Article/3245415/1')
# start('https://www.taoguba.com.cn/Article/3243958/1')
# start('https://www.taoguba.com.cn/Article/3240556/1')
# start('https://www.taoguba.com.cn/Article/3239134/1')
# start('https://www.taoguba.com.cn/Article/3237723/1')
# start('https://www.taoguba.com.cn/Article/3236172/1')
# start('https://www.taoguba.com.cn/Article/3234758/1')

# start('https://www.taoguba.com.cn/Article/3232402/1')
# start('https://www.taoguba.com.cn/Article/3230840/1')
# start('https://www.taoguba.com.cn/Article/3229386/1')
# start('https://www.taoguba.com.cn/Article/3227677/1')
# start('https://www.taoguba.com.cn/Article/3226164/1')
# start('https://www.taoguba.com.cn/Article/3223288/1')
# start('https://www.taoguba.com.cn/Article/3221679/1')
# start('https://www.taoguba.com.cn/Article/3220070/1')
# start('https://www.taoguba.com.cn/Article/3218387/1')
# start('https://www.taoguba.com.cn/Article/3216764/1')
# start('https://www.taoguba.com.cn/Article/3214211/1')
# start('https://www.taoguba.com.cn/Article/3212674/1')
# start('https://www.taoguba.com.cn/Article/3210840/1')
# start('https://www.taoguba.com.cn/Article/3209291/1')
# start('https://www.taoguba.com.cn/Article/3206643/1')
# start('https://www.taoguba.com.cn/Article/3205290/1')
# start('https://www.taoguba.com.cn/Article/3203467/1')
# start('https://www.taoguba.com.cn/Article/3201769/1')
# start('https://www.taoguba.com.cn/Article/3200296/1')
# start('https://www.taoguba.com.cn/Article/3197530/1')
# start('https://www.taoguba.com.cn/Article/3196027/1')
# start('https://www.taoguba.com.cn/Article/3194713/1')
# start('https://www.taoguba.com.cn/Article/3193100/1')
# start('https://www.taoguba.com.cn/Article/3191350/1')
# start('https://www.taoguba.com.cn/Article/3189073/1')
# start('https://www.taoguba.com.cn/Article/3187323/1')
# start('https://www.taoguba.com.cn/Article/3186003/1')
# start('https://www.taoguba.com.cn/Article/3184300/1')
# start('https://www.taoguba.com.cn/Article/3182696/1')
# start('https://www.taoguba.com.cn/Article/3180319/1')
# start('https://www.taoguba.com.cn/Article/3179824/1')
# start('https://www.taoguba.com.cn/Article/3178648/1')
# start('https://www.taoguba.com.cn/Article/3177267/1')
# start('https://www.taoguba.com.cn/Article/3177240/1')
# start('https://www.taoguba.com.cn/Article/3175696/1')
# start('https://www.taoguba.com.cn/Article/3173808/1')
# start('https://www.taoguba.com.cn/Article/3171488/1')
# start('https://www.taoguba.com.cn/Article/3170060/1')
# start('https://www.taoguba.com.cn/Article/3168940/1')
# start('https://www.taoguba.com.cn/Article/3166874/1')
# start('https://www.taoguba.com.cn/Article/3165413/1')
# start('https://www.taoguba.com.cn/Article/3162813/1')
# start('https://www.taoguba.com.cn/Article/3161531/1')
# start('https://www.taoguba.com.cn/Article/3160014/1')
# start('https://www.taoguba.com.cn/Article/3158667/1')
# start('https://www.taoguba.com.cn/Article/3157260/1')
# start('https://www.taoguba.com.cn/Article/3154924/1')
# start('https://www.taoguba.com.cn/Article/3153753/1')
# start('https://www.taoguba.com.cn/Article/3149353/1')
# start('https://www.taoguba.com.cn/Article/3148093/1')

# start('https://www.taoguba.com.cn/Article/3145725/1')
# start('https://www.taoguba.com.cn/Article/3144231/1')

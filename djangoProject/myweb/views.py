from django.shortcuts import render
from django.http import HttpResponse
from .models import 绯闻, 歌曲, 歌手, 好友, 旧爱, 离异, 恋人, 亲属, 人物, 演员, 影视作品, 主演


# Create your views here.
def page_not_found(request, exception):
    return render(request, '404.html')


def server_error(request):
    return render(request, '500.html')


# 去掉字符串最后的逗号
def del_last_comma(str):
    if str != '':
        if str[-1] == ',':
            return str[:-1]
        else:
            return str
    else:
        return '暂无信息'


def get_context(name):
    try:
        # 根据姓名查询人物对象
        person = 人物.objects.get(name=name)
    except 人物.DoesNotExist:
        return HttpResponse('没有这个人!')
    context = {}
    # 查询职业
    if 演员.objects.filter(id=person.id):
        if 歌手.objects.filter(id=person.id):
            context['occupation'] = '演员,歌手'
        else:
            context['occupation'] = '演员'
    else:
        if 歌手.objects.filter(id=person.id):
            context['occupation'] = '歌手'

    # 查询代表作品(影片或歌曲)
    m_works = 主演.objects.filter(person=person.id)
    famous_work = ''
    for m_work in m_works:
        try:
            famous_work += str(影视作品.objects.get(id=m_work.works.id)) + ','
        except 影视作品.DoesNotExist:
            pass
    s_works = 歌曲.objects.filter(singer=person.id)
    for s_work in s_works:
        try:
            famous_work += str(s_work) + ','
        except 歌曲.DoesNotExist:
            pass

    # 查询好友
    friends = 好友.objects.filter(person1=person.id)
    str_friends = ''
    for friend in friends:
        str_friends += friend.person2.name + ','

    # 查询旧爱
    old_lover = 旧爱.objects.filter(person1=person.id)
    str_old_lover = ''
    for lover in old_lover:
        str_old_lover += lover.person2.name + ','

    # 查询绯闻
    gossip = 绯闻.objects.filter(person1=person.id)
    str_gossip = ''
    for g in gossip:
        str_gossip += g.person2.name + ','

    # 查询前任(离异)
    divorced = 离异.objects.filter(person1=person.id)
    str_divorced = ''
    for d in divorced:
        str_divorced += d.person2.name + ','

    # 查询现任(恋人)
    lover = 恋人.objects.filter(person1=person.id)
    str_lover = ''
    for lv in lover:
        str_lover += lv.person2.name + ','

    # 查询亲属
    relatives = 亲属.objects.filter(person1=person.id)
    str_relatives = ''
    for r in relatives:
        str_relatives += r.person2.name + ','

    context['famous_work'] = del_last_comma(famous_work)
    context['friends'] = del_last_comma(str_friends)
    context['old_lover'] = del_last_comma(str_old_lover)
    context['gossip'] = del_last_comma(str_gossip)
    context['divorced'] = del_last_comma(str_divorced)
    context['lover'] = del_last_comma(str_lover)
    context['relatives'] = del_last_comma(str_relatives)

    return context


def query_page(request):
    # 输入姓名查询相关信息
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            person = 人物.objects.filter(name=name)
            context = {'persons': person}
            return render(request, 'query.html', context=context)
    return render(request, 'query.html')


def query_all(request):
    # 查询所有人物信息
    if request.method == 'GET':
        # 获取所有人物对象的查询集
        persons = 人物.objects.all()
        context = {'persons': persons}
        return render(request, 'query.html', context=context)

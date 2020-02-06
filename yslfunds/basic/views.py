import os
import logging

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import Template
from django.utils._os import safe_join

from basic.models import Article, Slogan
from basic.constraint import SLUG_DIR, SUB_SLUG_DIR, TEMPLATE_PAGE_NAME

# Create your views here.

LOGGER = logging.getLogger(__name__)


def index(request):
    latest_article_list = Article.objects.filter(status='0').order_by('-create_time')[:5]
    context = {
        'latest_article_list': latest_article_list,
    }
    return render(request, 'article/index.html', context)


def content(request):
    article_id = request.GET['art_id']
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article/content.html', {'article': article})


# def home(request, slug='home'):
#     context = {
#         'slug': slug
#     }
#     return render(request, 'home.html', context)


def articles(request):
    if 'art_id' in request.GET:
        article_id = request.GET['art_id']
        article = get_object_or_404(Article, pk=article_id)
        context = {
            'index': False,
            'article': article,
        }
    else:
        latest_article_list = Article.objects.filter(status='0').order_by(
            '-create_time')[:5]
        context = {
            'index': True,
            'latest_article_list': latest_article_list,
        }
    return render(request, 'content_template.html', context)


def page_or_404(name):
    """
    Return page content as
    :param name:
    :return:
    """
    try:
        file_path = safe_join(settings.BASE_DIR, 'basic', 'templates', name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r', encoding='UTF-8') as f:
        page = Template(f.read())

    return page


def page(request, slug='home', sub_slug=''):
    """
    Render the requested page if found
    :param request:
    :param slug:
    :param sub_slug:
    :return:
    """
    file_name = '{}.html'.format(slug)
    if slug != 'home':
        file_name = '{}.html'.format(TEMPLATE_PAGE_NAME)
    LOGGER.info('slug is {}'.format(slug))
    page = page_or_404(file_name)
    latest_article_list = Article.objects.filter(status='0').order_by(
        '-create_time')[:3]
    slogan_home_page = Slogan.objects.get(id=1)
    context = {
        'slug': SLUG_DIR.get(slug),
        'page': page,
        'latest_article_list': latest_article_list,
        'slogan': slogan_home_page,
    }
    if slug == 'articles':
        # if 'art_id' in request.GET:
        #     article_id = request.GET['art_id']
        #     article = get_object_or_404(Article, pk=article_id)
        #     context.update({
        #         'index': False,
        #         'article': article,
        #     })
        # else:
        #     latest_article_list = Article.objects.filter(status='0').order_by(
        #         '-create_time')[:5]
        #     context.update({
        #         'index': True,
        #         'latest_article_list': latest_article_list,
        #     })
        art_context = articles_view_context(request, sub_slug)
        context.update(art_context)
    elif slug == 'donations':
        donations_context = donations_view_context(request, sub_slug)
        context.update(donations_context)
    elif slug == 'about':
        about_context = about_view_context(request, sub_slug)
        context.update(about_context)

    return render(request, 'page.html', context)


def about_view_context(request, sub_slug):
    LOGGER.info('sub_slug is {}'.format(sub_slug))
    context = {
        'sub_slug': SUB_SLUG_DIR.get(sub_slug),
    }
    if sub_slug == 'introduction':
        pass

    elif sub_slug == 'donation_his':
        pass
    return context


def articles_view_context(request, sub_slug):
    LOGGER.info('sub_slug is {}'.format(sub_slug))
    context = {
        'sub_slug': SUB_SLUG_DIR.get(sub_slug),
    }
    if sub_slug == 'news':
        if 'art_id' in request.GET:
            article_id = request.GET['art_id']
            article = get_object_or_404(Article, pk=article_id)
            context.update({
                'index': False,
                'article': article,
            })
        else:
            latest_article_list = Article.objects.filter(status='0').order_by(
                '-create_time')[:5]
            context.update({
                'index': True,
                'latest_article_list': latest_article_list,
            })

    return context


def donations_view_context(request, sub_slug):
    LOGGER.info('sub_slug is {}'.format(sub_slug))
    context = {
        'sub_slug': SUB_SLUG_DIR.get(sub_slug),
    }
    if sub_slug == 'activities':
        if sub_slug == 'activities':
            if 'year' in request.GET:
                act_year = request.GET['year']
                context.update({'act_year': act_year})
            else:
                context.update({'act_year': '2019'})
        else:
            latest_article_list = Article.objects.filter(status='0').order_by(
                '-create_time')[:5]
            context.update({
                'index': True,
                'latest_article_list': latest_article_list,
            })

    return context


def get_last_path_in_url(request):
    path_list = request.path.split('/')
    if path_list[-1]:
        return path_list[-1]
    return path_list[-2]

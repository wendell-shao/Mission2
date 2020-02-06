NAV_LIST = ['home', 'about', 'donations', 'articles', 'guides']
SLUG_DIR = {
    'home': {
        'name': 'home',
        'verbose_name': '首页',
    },
    'articles': {
        'name': 'articles',
        'verbose_name': '捐赠新闻',
        'sub_slug': [
            {
                'name': 'news',
                'verbose_name': '新闻动态',
            },
        ],
    },
    'donations': {
        'name': 'donations',
        'verbose_name': '捐赠动态',
        'sub_slug': [
            {
                'name': 'activities',
                'verbose_name': '活动动态',
            },
        ],
    },
    'guides': '办事指南',
    'about': {
        'name': 'about',
        'verbose_name': '基金会概况',
        'sub_slug': [
            {
                'name': 'introduction',
                'verbose_name': '基金会介绍',
            },
            {
                'name': 'donation_his',
                'verbose_name': '捐赠历史'
            },
        ],
    },
}
SUB_SLUG_DIR = {
    'news': {'name': 'news', 'verbose_name': '新闻动态', },
    'activities': {'name': 'activities', 'verbose_name': '活动动态'},
    'principal': {'name': 'principal', 'verbose_name': '原则要求'},
    'application': {'name': 'application', 'verbose_name': '申请流程'},
    'apply_material': {'name': 'apply_material', 'verbose_name': '申请资料'},
    'introduction': {'name': 'introduction', 'verbose_name': '基金会介绍'},
    'donation_his': {'name': 'donation_his', 'verbose_name': '捐赠历史'},
}
TEMPLATE_PAGE_NAME = 'content_template'
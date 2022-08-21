import logging

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from ..models import Question

logger = logging.getLogger('pybo')

def index(request):
    logger.info("INFO 레벨로 출력")

    question_list = Question.objects.order_by('-create_date')
    kw = request.GET.get('kw', '')      # 검색어
    page = request.GET.get('page', '1') # 페이지
    
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  
            Q(content__icontains=kw) |  
            Q(author__username__icontains=kw) |  
            Q(answer__author__username__icontains=kw)  
        ).distinct()

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

from django.shortcuts import render,get_object_or_404,redirect
from blog.models import post
from .forms import CommentForm

# Create your views here.
def post_comment(request,post_pk):
    pst=get_object_or_404(post,pk=post_pk)
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=pst
            comment.save()
            return redirect(pst)
        else:
            comment_list=pst.comment_set.all()
            context={
                'post':pst,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)
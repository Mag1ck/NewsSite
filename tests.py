from django.test import TestCase

def add_article(request):
    tags = Tag.objects.all()

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the main article first
            article = form.save()

            # Process selected tags
            tags_json = request.POST.get('tags')
            tags = json.loads(tags_json) if tags_json else []
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                article.tags.add(tag)

            # Create ArticleImage instances for each uploaded image
            for image_file in request.FILES.getlist('images'):
                article_image = ArticleImage.objects.create(article=article, image=image_file)
                article_image.save()

            # Create ArticleVideo instances for each uploaded video
            for video_file in request.FILES.getlist('videos'):
                article_video = ArticleVideo.objects.create(article=article, video=video_file)
                article_video.save()

            return redirect('article-detail', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'edit.html', {'form': form, 'tags': tags})
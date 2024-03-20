from django import template
from django.utils.safestring import mark_safe  # Import mark_safe
import re

register = template.Library()

@register.filter(name='split_paragraphs')
def split_paragraphs(value):
    lines = value.split('\n')
    wrapped_lines = ['<p>{}</p>'.format(line) for line in lines if line]  # Skip empty lines
    return mark_safe(''.join(wrapped_lines))  # Mark the output as safe

@register.filter(name='add_images')
def add_images(value, post):
    if 'images' in post and post['images'] and len(post['images']) > 0:
        current_image_index = post.get('current_image_index', 0)
        images_html = [
            f'<img class="image-style" src="{post["images"][current_image_index]["image"]}" alt="Image {current_image_index + 1}">'
        ]
        post['current_image_index'] = (current_image_index + 1) % len(post['images'])  # Handle cycling through images
        return value.replace('{image}', ''.join(images_html))
    else:
        return value

@register.filter(name='add_bold')
def add_bold(value):
    pattern = re.compile(r'\{bold\}(.+?)\{/bold\}')
    return pattern.sub(r'<strong>\1</strong>', value)
#
@register.filter(name='add_quote')
def add_quote(value):
    return value.replace('{quote}', '<blockquote>').replace('{/quote}', '</blockquote>')
#
@register.filter(name='add_italic')
def add_italic(value):
    return value.replace('{italic}', '<em>').replace('{/italic}', '</em>')

@register.filter(name='add_underline')
def add_underline(value):
    return value.replace('{underline}', '<u>').replace('{/underline}', '</u>')

@register.filter(name='add_strikethrough')
def add_strikethrough(value):
    return value.replace('{strikethrough}', '<del>').replace('{/strikethrough}', '</del>')

@register.filter(name='add_videos')
def add_videos(value, post):
    if 'videos' in post and post['videos'] and len(post['videos']) > 0:
        current_video_index = post.get('current_video_index', 0)
        videos_html = [
            f'<iframe width="560" height="315" src="{post["videos"][current_video_index]["video"]}" frameborder="0" allowfullscreen></iframe>'
        ]
        post['current_video_index'] = (current_video_index + 1) % len(post['videos'])  # Handle cycling through videos
        return value.replace('{video}', ''.join(videos_html))
    else:
        return value


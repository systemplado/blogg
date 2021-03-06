from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class SectionBlock(blocks.StructBlock):
    feats = [
        'bold', 'italic', 'ol', 'ul', 'link', 'code',
        'superscript', 'subscript', 'strikethrough' 'blockquote'
    ]
    title = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(required=True, features=feats, help_text='Tip: Use the "line break" button to retain new line formatting in post')

    class Meta:
        template = 'streams/section_block.html'

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'streams/image_block.html'

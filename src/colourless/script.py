"""ColourLess
Create a colour.less file from a colourlovers palette.

Usage: colourless --config <file>

Options:
  -h --help         Show this screen.
  --config <file>   Specify a palette config file to use.
  
"""

#from optparse import OptionParser
import os
import os.path
import re
import ConfigParser

from docopt import docopt
from colourlovers import ColourLovers
from pystache.renderer import Renderer
from pystache.context import ContextStack


def main():
    args = docopt(__doc__)

    config = ConfigParser.SafeConfigParser()
    config.read(args['--config'])
    palette_urls = config.get('palettes', 'url')
    palette_ids = [int(x) for x in re.findall('palette/([0-9]+)/', palette_urls)]

    renderer = Renderer()

    if config.has_option('palettes', 'template'):
        template_file = config.get('palettes', 'template')
        f = open(template_file, 'r')
        template = f.read()
        f.close()
    else:
        template = """
{{#palettes}}
/** Colourlovers Palette
    {{title}}
    {{url}}
    by: {{user_name}}
    {{description}}
**/
{{#colors}}
/* {{title}} */
@color-{{normalized_title}}: {{hex}};
{{/colors}}

{{/palettes}}
        """

    d = { 'palettes':[] }

    cl = ColourLovers()
    for palette_id in palette_ids:
        for palette in cl.palette(palette_id):
            colors = []
            for hexcolor in palette.colours:
                c = cl.color(hexcolor)[0]
                a_colour = {
                        'badge_url': c.badge_url,
                        'date_created': c.date_created,
                        'description': c.description,
                        'hex': c.hex,
                        'hsv': c.hsv,
                        'id': c.id,
                        'image_url': c.image_url,
                        'rgb': c.rgb,
                        'title': c.title,
                        'normalized_title': re.sub('[^a-z_-]', '', c.title.lower()),
                        'url': c.url,
                        'user_name': c.user_name,
                        }
                colors.append(a_colour)
            d['palettes'].append({
                'badge_url': palette.badge_url,
                'date_created': palette.date_created,
                'description': palette.description,
                'id': palette.id,
                'image_url': palette.image_url,
                'title': palette.title,
                'normalized_title': re.sub('[^a-z_-]', '', palette.title.lower()),
                'url': palette.url,
                'user_name': palette.user_name,
                'colors':colors,
                })


    ctx = ContextStack(d)
    css_file = config.get('palettes', 'css')
    c = open(css_file, 'w')
    c.write( renderer.render(template, ctx) )
    c.close()

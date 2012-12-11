==========
ColourLess
==========

A simple script to create a colour.less file from a ColourLover's palette.

A more semantic color management
================================

It's assumed that when using .less you use variables to hold your colors.  The
names of these variables should probably be semantic so if the colour changes
the variable name doesn't need to.

The old way
-----------

Changing a color on a website is usually a pretty simple process.  Just do a
find and replace for the color and you're done.  Except that isn't very fun.
Sometimes the color is not just one color, and it impacts other colors if
changed. An example would be changing a background color and not updating the
text color to contrast with it.

A short story
*************

*This short story is actually longer then the included script.py*

Client: I want a website made that is fun, light and very summer like.

Designer: Ok.
Starts creating something in photoshop with a range of blues, yellows, and
greens. After weeks of creative hours designing the right balance using his
wide knowledge of color theory; has produced a summer like website that is both
fun and light.

Designer: Does this look good?

Client: Uhm, I'd like a darker blue here.

Designer: Ok.
Goes through all the different layers of graphics that have blue in them and
darkens it.

Designer: Here is your revised comp.

Client: Love it.
Continues with their day to day stuff, knowing that they contributed to the
design in some way.

Designer: Here are the photoshop comps of the website complete with all the
info you need to make the website to the Client's specifications.

Developer: Great.
Filters through all the photoshop layers and graphics and pieces together all
the colors that will be used on the website.  Starts coding in all the colors
to their respective borders, backgrounds, text colors, etc.

Developer: Finished.

Designer: Ok.
Sends the website to the Client.

Client: Oh, I don't like some of the colors here.  Can you change those?

Designer: Ok.
Makes the requested color changes in his photoshop comps.  Sends revision to
the Developer.

Developer: Ack.  I don't like doing things twice! Grr...
Settles in for a "color by number" session.


The new and improved way using A Semantic Coloring method.
----------------------------------------------------------

Nothing changes much for the Client or Designer other then updating the colour
palettes.  The Developer has it the easiest assuming all the ducks are colored
correctly.

Client: I want a website made that is fun, light and very summer like.

Designer: Ok.
Creates some colour palettes on ColourLovers and sends them to the Client.

Client: Love the colours!

Designer: Ok.
Starts creating something in photoshop with the colour palettes chosen. After
weeks of creative hours designing the right balance using his wide knowledge of
color theory; has produced a summer like website that is both fun and light.

Designer: Does this look good?

Client: Uhm, I'd like a darker blue here.

Designer: Ok.
Updates the colour palette on ColourLovers.  Goes through all the different
layers of graphics that have blue in them and darkens it. (Thinks - Isn't there
a better way?)

Designer: Here is your revised comp.

Client: Love it.
Continues with their day to day stuff, knowing that they contributed to the
design in some way.  Also, becomes a fan of ColourLovers.

Designer: Here are the photoshop comps of the website complete with all the
info you need to make the website to the Client's specifications. Includes
links to the colour palettes used.

Developer: Great.
Filters through all the photoshop layers and graphics. Converts the colours to
semantic names and uses them as "less variables".  Starts coding in all the
semanticified colors to their respective borders, backgrounds, text colors,
etc.

Developer: Finished.

Designer: Ok.
Sends the website to the Client.

Client: Oh, I don't like some of the colors here.  Can you change those?

Designer: Ok.
Makes the requested color changes in his photoshop comps. (Why?)  Sends
revision to the Developer.  Updates the color palette on ColourLovers.

Developer: Ack. Simply updates the link to the colour palette if it's a new
palette, otherwise just runs *buildout*.


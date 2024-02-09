
# Houdini Graph Editor Tools
## [de]amplify_keyframes.py 

Amplifies or deamplifies the selected keyframes by ten percent.

I hotkey map these to **Ctrl+>** to amplify and **Ctrl+<** to deamplify.
You can already do this with the box handle or, more recently, the Pull Push tool in the Animation Toolbar.

This is just a little faster and more comfortable; it is a little more "no-look" so you can keep your eyes on the animation and relax your stylus hand.

## copy_and_offset.py

Copies the selected curve onto its parent node's children and offsets the time by five frames per child.

I hotkey map this to **Ctrl+Shift+O**.

For example, if you have `/obj/sphere1/tx` selected in the channel list it will copy and paste the `tx` curve onto `/obj/sphere2/tx`, `/obj/sphere3/tx`, `/obj/sphere4/tx`, etc. ofsetting the curve forward in time five frames, ten frames, fifteen frames, etc.

This could be a useful starting point for animating overlap on mechanical chains, mechanical tails or mechanical snouts.

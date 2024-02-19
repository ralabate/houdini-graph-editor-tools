
# Houdini Graph Editor Tools
## [de]amplify_keyframes.py 

Amplifies or deamplifies the selected keyframes by ten percent.

I hotkey map these to **Ctrl+>** to amplify and **Ctrl+<** to deamplify.

Although the box handle and pull push tool both do the same thing, I find this method faster and more comfortable. It is a little more "no-look" so you can keep your eyes on the animation and relax your stylus hand.

## negate_keyframes.py

Multiplies keyframes the selected keyframes by negative one.

I hotkey map this to **Ctrl+?**.

This is faster than mousing around and typing *=-1 in the value box.

## set_playback_range.py

Sets the playback range based on the selected keyframes.

I hotkey map this to **Ctrl+Shift+R**.

This is much faster than mousing around and typing in a pair of numbers. If there are no keyframes selected it sets the playback range to the global frame range.

## copy_and_offset.py

Copies the selected curve onto its parent node's children and offsets the time by five frames per child.

I hotkey map this to **Ctrl+Shift+O**.

For example, if you have `/obj/sphere1/tx` selected in the channel list it will copy and paste the `tx` curve onto `/obj/sphere2/tx`, `/obj/sphere3/tx`, `/obj/sphere4/tx`, etc. ofsetting the curve forward in time five frames, ten frames, fifteen frames, etc.

This could be a useful starting point for animating overlap on mechanical chains, mechanical tails or mechanical snouts.

# inspired by michal makarewicz at animation collaborative

import hou

# get that panetab
channel_editor = None
channel_editor = hou.ui.paneTabOfType(hou.paneTabType.ChannelEditor)

# get that panetab's delicious graph editor innards
if channel_editor == None:
    pass
else:
    channel_graph = channel_editor.graph()
    selected_keyframes = channel_graph.selectedKeyframes()
    if len(selected_keyframes) > 0:
        for parm, keys in selected_keyframes.items():
            for key in keys:
                key.setValue(-1 * key.value())
                key.setSlope(-1 * key.slope())
                if (key.isSlopeTied() == False):
                    key.setInSlope(-1 * key.inSlope())
                parm.setKeyframe(key)
    else:
        pass

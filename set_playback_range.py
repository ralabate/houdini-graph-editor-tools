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
    first_frame = 9999
    last_frame = -9999
    if len(selected_keyframes) > 0:
        for parm, keys in selected_keyframes.items():
            for key in keys:
                if key.frame() <= first_frame:
                    first_frame = key.frame()
                if key.frame() >= last_frame:
                    last_frame = key.frame()
        hou.playbar.setPlaybackRange(first_frame, last_frame)      
    else:
        global_first_frame = hou.playbar.frameRange()[0]
        global_last_frame = hou.playbar.frameRange()[1]
        hou.playbar.setPlaybackRange(global_first_frame, global_last_frame)

#WIP MAYBE IF NOTHING HIGHLIGHTED CLEAR FRAME RANGE


import hou

# get that panetab
channel_editor = None
channel_editor = hou.ui.paneTabOfType(hou.paneTabType.ChannelEditor)

# get that panetab's delicious graph editor innards
if channel_editor == None:
    pass
    #print("ERROR: Could not find paneTab of type ChannelEditor")
else:
    channel_graph = channel_editor.graph()
    selected_keyframes = channel_graph.selectedKeyframes()
    first_frame = 999
    last_frame = -999
    if len(selected_keyframes) > 0:
        for parm, keys in selected_keyframes.items():
            for key in keys:
                if key.frame() <= first_frame:
                    first_frame = key.frame()
                    print("updating first: " + str(first_frame))
                if key.frame() >= last_frame:
                    last_frame = key.frame()
                    print("updating last: " + str(last_frame))
        print("CALLING WITH: " + str(first_frame) + " " + str(last_frame))                    
        hou.playbar.setPlaybackRange(first_frame, last_frame)      
    else:
        pass
        #print("ERROR: No keyframes selected")

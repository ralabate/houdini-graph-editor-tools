import hou

def get_all_outputs(node):
    outputs = []
    immediate_outputs = node.outputs()
    outputs.extend(immediate_outputs)
    for output_node in immediate_outputs:
        outputs.extend(get_all_outputs(output_node))
    return outputs        

# get that panetab
channel_editor = None
channel_editor = hou.ui.paneTabOfType(hou.paneTabType.ChannelEditor)

# get that panetab's delicious graph editor innards
if channel_editor == None:
    pass
    print("ERROR: Could not find paneTabl of type ChannelEditor")
else:
    channel_list = channel_editor.channelList()
    if len(channel_list.selected()) > 0:
        selected_parm = channel_list.selected()[0]
        outputs = get_all_outputs(selected_parm.node())
        i = 0
        if len(outputs) > 0:
            for output in outputs:
                i = i + 5
                parm = output.parm(selected_parm.name())
                parm.deleteAllKeyframes()
                for key in selected_parm.keyframes():
                    key.setFrame(key.frame() + i)
                    parm.setKeyframe(key)
                channel_list.addParm(parm)
            hou.playbar.setChannelList(channel_list)
        else:
            print("ERROR: Selected channel's Op has no outputs!")
        
    else:
        print("ERROR: No channel selected")

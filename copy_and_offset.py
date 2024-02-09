import hou

print("\n" * 100)

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
        master_parm = channel_list.selected()[0]
        print(master_parm)
        master_parm_name = master_parm.name()
        print(master_parm_name)
        node = master_parm.node()
        print(node)
        #top_level_children = [child for child in node.allSubChildren() if child.type().category() == hou.sopNodeTypeCategory()]
        top_level_children = node.children()
        if len(top_level_children) > 0:
            for child in top_level_children:
                print(child.name())
                print(child.path())
                channel_list.addParm(child.parm(master_parm_name), False, False, False)
            hou.playbar.setChannelList(channel_list)
        else:
            print("ERROR: Selected channel's Op has no children!")
        
    else:
        print("ERROR: No channel selected")


import nuke
import nukescripts

####################################################################################
#//////////////////////////////////BACKDROP/////////////////////////////////////////
####################################################################################

def backdrop():
	selections = nuke.selectedNodes()

	bd_name = nuke.getInput('Set Backdrop name', '<center><b> ')
	if selections:
		backdrop = nukescripts.autoBackdrop()
		backdrop['label'].setValue(bd_name)
		# for node in selections:
			# if node.Class() == 'Read':
				# Name backdrop after Read node
				# backdrop.setName(node.name(), uncollide=True)
				# break
	else:
		nuke.message("No node selected")

####################################################################################
#//////////////////////////////// AOV BUILDER///////////////////////////////////////
####################################################################################

# read = nuke.nodes.Read(file='E:/WORK/GOLDEN CAKE/COCINA/PRODUCTS/ARA/TEST/RENDER_CAM/ARA_BEAUTY_v001_0001.exr')
# read['name'].setValue('Read_1')

# def template():
# 	read = nuke.nodes.Read(file='E:/WORK/GOLDEN CAKE/COCINA/PRODUCTS/ARA/TEST/RENDER_CAM/ARA_BEAUTY_v001_0001.exr')
# 	read['name'].setValue('Read_1')
# 	for node in nuke.allNodes():
# 		node_name = node['name'].value()
# 		if 'Read'in node_name:
# 			read = node
# 			aovs = read.channels()
# 			aovs = list(set([i.split('.')[0] for i in aovs]))

# 			# for aov_name in aovs:
# 		if '_lgt' and 'transmission' in aovs:
# 				shuffle_tr = nuke.nodes.Shuffle()
# 				shuffle_tr['name'].setValue(aov_name)
# 				shuffle_tr['in'].setValue(read)

				
# try: 
def template():
	pm_d = None
	pm_T = None
	pm_sp = None
	pm_c = None
	m_d = None
	m_t = None
	m_sp = None
	m_c = None
	lgt = nuke.getInput('Set Light Group name', '')
	read = nuke.selectedNode()
	#checks the class of selected node

	if read and read.Class() == "Read":
		aovs = read.channels()
		aovs = list(set([i.split('.')[0] for i in aovs]))
		# print(aovs)
	
		#creates a shuffle node for each AOV
		for aov_name in aovs:
			if aov_name.startswith(lgt) and 'diffuse' in aov_name:

				shuffle = nuke.nodes.Shuffle()
				shuffle['name'].setValue(aov_name)
				# shuffle['label'].setValue(aov_name)
				shuffle['in'].setValue(aov_name)
				shuffle.setInput(0, read)
				shuffle['in2'].setValue('rgba')
				grade = nuke.nodes.Grade()#name= 'Grade_' + aov_name)
				grade.setInput(0, shuffle)

				if pm_d:
					merge_diff = nuke.nodes.Merge(name = 'Merge_Diffuse_key')
					merge_diff['operation'].setValue('plus')
					merge_diff.setInput(1, pm_d)
					merge_diff.setInput(0, grade)
					grade_diff = nuke.nodes.Grade(name = 'Grade_Diffuse')
					grade_diff.setInput(0, merge_diff)
					pm_d = grade
				else:
					pm_d = grade

			elif aov_name.startswith(lgt) and 'transmission' in aov_name:
				shuffle = nuke.nodes.Shuffle()
				shuffle['name'].setValue(aov_name)
				# shuffle['label'].setValue(aov_name)
				shuffle['in'].setValue(aov_name)
				shuffle.setInput(0, read)
				shuffle['in2'].setValue('rgba')
				grade = nuke.nodes.Grade()#name= 'Grade_' + aov_name)
				grade.setInput(0, shuffle)

				if pm_T:
					merge_trans = nuke.nodes.Merge(name = 'Merge_Transmission_key')
					merge_trans['operation'].setValue('plus')
					merge_trans.setInput(1, pm_T)
					merge_trans.setInput(0, grade)
					grade_trans = nuke.nodes.Grade(name = 'Grade_Transmission')
					grade_trans.setInput(0, merge_trans)
					# merges_1 = nuke.nodes.Merge()
					# merges_1.setInput(0, merge_diff)
					# merges_1.setInput(1, merge_trans)
					# merges_1['operation'].setValue('plus')
					pm_T = grade
				else:
					pm_T = grade

			elif aov_name.startswith(lgt) and 'specular' in aov_name:
				shuffle = nuke.nodes.Shuffle()
				shuffle.setInput(0, read)
				shuffle['name'].setValue(aov_name)
				# shuffle['label'].setValue(aov_name)
				shuffle['in'].setValue(aov_name)
				shuffle['in2'].setValue('rgba')
				grade = nuke.nodes.Grade()#name= 'Grade_' + aov_name)
				grade.setInput(0, shuffle)

				if pm_sp:
					merge_spec = nuke.nodes.Merge(name = 'Merge_Specular_key')
					merge_spec['operation'].setValue('plus')
					merge_spec.setInput(1, pm_sp)
					merge_spec.setInput(0, grade)
					grade_spec = nuke.nodes.Grade(name = 'Grade_Specular')
					grade_spec.setInput(0, merge_spec)
					pm_sp = grade
					# merges_2 = nuke.nodes.Merge()
					# merges_2.setInput(0, merge_spec)
					# merges_2.setInput(0, merges_1)
					# merges_2['operation'].setValue('plus')

				else:
					pm_sp = grade

			elif aov_name.startswith(lgt) and 'coat' in aov_name:
				shuffle = nuke.nodes.Shuffle()
				shuffle.setInput(0, read)
				shuffle['name'].setValue(aov_name)
				# shuffle['label'].setValue(aov_name)
				shuffle['in'].setValue(aov_name)
				shuffle['in2'].setValue('rgba')
				grade = nuke.nodes.Grade()#name= 'Grade_' + aov_name)
				grade.setInput(0, shuffle)

				if pm_c:
					merge_coat = nuke.nodes.Merge(name = 'Merge_Coat_key')
					merge_coat['operation'].setValue('plus')
					merge_coat.setInput(1, pm_c)
					merge_coat.setInput(0, grade)
					grade_coat = nuke.nodes.Grade(name = 'Grade_Coat')
					grade_coat.setInput(0, merge_coat)
					pm_c = grade
					# merges_2 = nuke.nodes.Merge()
					# merges_2.setInput(0, merge_spec)
					# merges_2.setInput(0, merges_1)
					# merges_2['operation'].setValue('plus')

				else:
					pm_c = grade

		merges_1 = nuke.nodes.Merge()
		merges_1.setInput(0, grade_diff)
		merges_1.setInput(1, grade_trans)
		merges_1['operation'].setValue('plus')
		merges_2 = nuke.nodes.Merge()
		merges_2.setInput(0, merges_1)
		merges_2.setInput(1, grade_spec)
		merges_2['operation'].setValue('plus')
		merges_3 = nuke.nodes.Merge()
		merges_3.setInput(0, grade_coat)
		merges_3.setInput(1, merges_2)
		merges_3['operation'].setValue('plus')





				# merge_diff.setInput(0, key_lgt_diffuse_indirect)
				# merge_diff.setInput(1, key_lgt_diffuse_direct)
			# else:
			# 	pass
		 	 #  shuffle['postage_stamp'].setValue(1)
	else:
		nuke.message("Please select a read node")
# except:
# 	nuke.message("Please select a read node")
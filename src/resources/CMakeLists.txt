
SET(RESOURCES_URDF
	urdf/env11.xml
	urdf/env11.dae

	urdf/env12.xml
	urdf/env12.dae

	urdf/env1.xml
	urdf/env1.dae

	urdf/ground.xml
	urdf/ground.dae
	urdf/ground_phy_50mm.dae

	urdf/kuka.xml


	urdf/kuka_simple.xml

	urdf/sphere.xml

	urdf/rx90.xml
	urdf/rx90.dae

	urdf/icub.xml
	urdf/icub.dae
	urdf/icub_simple.xml
	urdf/icub_simple.dae
	urdf/icub_simple_collision.dae
	urdf/icub_simple_compensated_viscous.xml
	urdf/icub_simple_identified_viscous.xml
	
	urdf/cube.dae

urdf/iCubGenova03_compensatedViscousFriction.xml
urdf/iCubGenova03_identifiedViscousFriction.xml
urdf/iCubGenova03_noViscousFriction.xml

urdf/icub_chest.dae
urdf/icub_head.dae
urdf/icub_l_ankle_1.dae
urdf/icub_lap_belt_1.dae
urdf/icub_l_arm.dae
urdf/icub_l_foot.dae
urdf/icub_l_forearm.dae
urdf/icub_l_hand.dae
urdf/icub_l_hip_1.dae
urdf/icub_l_hip_2.dae
urdf/icub_l_shank.dae
urdf/icub_l_shoulder_1.dae
urdf/icub_l_shoulder_2.dae
urdf/icub_l_thigh.dae
urdf/icub_neck_1.dae
urdf/icub_neck_2.dae
urdf/icub_r_ankle_1.dae
urdf/icub_r_arm.dae
urdf/icub_r_foot.dae
urdf/icub_r_forearm.dae
urdf/icub_r_hand.dae
urdf/icub_r_hip_1.dae
urdf/icub_r_hip_2.dae
urdf/icub_root_link.dae
urdf/icub_r_shank.dae
urdf/icub_r_shoulder_1.dae
urdf/icub_r_shoulder_2.dae
urdf/icub_r_thigh.dae
urdf/icub_simple_collision_chest.dae
urdf/icub_simple_collision.dae
urdf/icub_simple_collision_head.dae
urdf/icub_simple_collision_l_ankle_1.dae
urdf/icub_simple_collision_lap_belt_1.dae
urdf/icub_simple_collision_l_arm.dae
urdf/icub_simple_collision_l_foot.dae
urdf/icub_simple_collision_l_forearm.dae
urdf/icub_simple_collision_l_hand.dae
urdf/icub_simple_collision_l_hip_1.dae
urdf/icub_simple_collision_l_hip_2.dae
urdf/icub_simple_collision_l_shank.dae
urdf/icub_simple_collision_l_shoulder_1.dae
urdf/icub_simple_collision_l_shoulder_2.dae
urdf/icub_simple_collision_l_thigh.dae
urdf/icub_simple_collision_neck_1.dae
urdf/icub_simple_collision_neck_2.dae
urdf/icub_simple_collision_r_ankle_1.dae
urdf/icub_simple_collision_r_arm.dae
urdf/icub_simple_collision_r_foot.dae
urdf/icub_simple_collision_r_forearm.dae
urdf/icub_simple_collision_r_hand.dae
urdf/icub_simple_collision_r_hip_1.dae
urdf/icub_simple_collision_r_hip_2.dae
urdf/icub_simple_collision_root_link.dae
urdf/icub_simple_collision_r_shank.dae
urdf/icub_simple_collision_r_shoulder_1.dae
urdf/icub_simple_collision_r_shoulder_2.dae
urdf/icub_simple_collision_r_thigh.dae
	
)

SET(RESOURCES_LWR_COLLADA
	urdf/lwr/base.dae
	urdf/lwr/link1.dae
	urdf/lwr/link2.dae
	urdf/lwr/link3.dae
	urdf/lwr/link4.dae
	urdf/lwr/link5.dae
	urdf/lwr/link6.dae
	urdf/lwr/link7.dae
)

FOREACH(SOURCE ${RESOURCES_URDF})
	INSTALL(FILES ${SOURCE}
		DESTINATION ${XDE_RESOURCES_PATH}
		PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ)
ENDFOREACH(SOURCE ${RESOURCES_URDF})

FOREACH(SOURCE ${RESOURCES_LWR_COLLADA})
	INSTALL(FILES ${SOURCE}
		DESTINATION ${XDE_RESOURCES_PATH}/lwr
		PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ)
ENDFOREACH(SOURCE ${RESOURCES_LWR_COLLADA})



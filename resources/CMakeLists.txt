
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
	urdf/kuka_lwr.dae

	urdf/sphere.xml
	urdf/sphere.dae
)

FOREACH(SOURCE ${RESOURCES_URDF})
	INSTALL(FILES ${SOURCE}
		DESTINATION ${XDE_RESOURCES_PATH}
		PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ)
ENDFOREACH(SOURCE ${RESOURCES_URDF})

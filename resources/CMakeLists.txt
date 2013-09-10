
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
	urdf/lwr/base.dae
	urdf/lwr/link1.dae
	urdf/lwr/link2.dae
	urdf/lwr/link3.dae
	urdf/lwr/link4.dae
	urdf/lwr/link5.dae
	urdf/lwr/link6.dae
	urdf/lwr/link7.dae

	urdf/kuka_simple.xml

	urdf/sphere.xml

	urdf/rx90.xml
	urdf/rx90.dae

	urdf/icub.xml
	urdf/icub.dae
	urdf/icub_simple.xml
	urdf/icub_simple.dae
	urdf/icub_simple_collision.dae
)

FOREACH(SOURCE ${RESOURCES_URDF})
	INSTALL(FILES ${SOURCE}
		DESTINATION ${XDE_RESOURCES_PATH}
		PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ)
ENDFOREACH(SOURCE ${RESOURCES_URDF})

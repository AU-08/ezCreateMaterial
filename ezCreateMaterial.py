import pymel.core as pm


def selectDiff(ws):
    imgFilter = "ImageFiles (*.*)"
    mapDiff = pm.fileDialog2(ff=imgFilter, ds=1, fm=1)
    global txDiff
    txDiff = mapDiff[0]
    pm.textField("tfDiffuse", edit=1, text=txDiff, bgc=([0.9, 0.9, 0.9]))


def selectMetal(ws):
    imgFilter = "ImageFiles (*.*)"
    mapMetal = pm.fileDialog2(ff=imgFilter, ds=1, fm=1)
    global txMetal
    txMetal = mapMetal[0]
    pm.textField("tfMetalness", edit=1, text=txMetal, bgc=([0.9, 0.9, 0.9]))


def selectRough(ws):
    imgFilter = "ImageFiles (*.*)"
    mapRough = pm.fileDialog2(ff=imgFilter, ds=1, fm=1)
    global txRough
    txRough = mapRough[0]
    pm.textField("tfRoughness", edit=1, text=txRough, bgc=([0.9, 0.9, 0.9]))


def selectNormal(ws):
    imgFilter = "ImageFiles (*.*)"
    mapNormal = pm.fileDialog2(ff=imgFilter, ds=1, fm=1)
    global txNormal
    txNormal = mapNormal[0]
    pm.textField("tfNormal", edit=1, text=txNormal, bgc=([0.9, 0.9, 0.9]))


def importTextureFile(ws):
    coord2d = pm.shadingNode("place2dTexture", asUtility=True, name="Coords")

    global file_diff
    file_diff = pm.shadingNode("file", asTexture=True, name="Diffuse")
    pm.defaultNavigation(ce=True, s=coord2d, d=file_diff)

    global file_metal
    file_metal = pm.shadingNode("file", asTexture=True, name="Metalness")
    pm.defaultNavigation(ce=True, s=coord2d, d=file_metal)

    global file_rough
    file_rough = pm.shadingNode("file", asTexture=True, name="Roughness")
    pm.defaultNavigation(ce=True, s=coord2d, d=file_rough)

    global file_normal
    file_normal = pm.shadingNode("file", asTexture=True, name="Normal")
    pm.defaultNavigation(ce=True, s=coord2d, d=file_normal)


def materialSetup(ws):
    ai_mat = pm.shadingNode("aiStandardSurface", asShader=True, name="_Mat")

    # Diffuse
    pm.defaultNavigation(ce=True, s=file_diff + ".outColor",
                         d=ai_mat + ".baseColor")
    pm.setAttr(file_diff + ".ignoreColorSpaceFileRules", 1)
    pm.setAttr(file_diff + ".fileTextureName", txDiff, type="string")

    # Metalness
    pm.defaultNavigation(ce=True, s=file_metal + ".outAlpha",
                         d=ai_mat + ".metalness")
    pm.setAttr(file_metal + ".colorSpace", "Raw", type="string")
    pm.setAttr(file_metal + ".alphaIsLuminance", 1)
    pm.setAttr(file_metal + ".ignoreColorSpaceFileRules", 1)
    pm.setAttr(file_metal + ".fileTextureName", txMetal, type="string")

    # Roughness
    pm.defaultNavigation(ce=True, s=file_rough + ".outAlpha",
                         d=ai_mat + ".specularRoughness")
    pm.setAttr(file_rough + ".colorSpace", "Raw", type="string")
    pm.setAttr(file_rough + ".alphaIsLuminance", 1)
    pm.setAttr(file_rough + ".ignoreColorSpaceFileRules", 1)
    pm.setAttr(file_rough + ".fileTextureName", txRough, type="string")

    # Normal
    ai_normal = pm.shadingNode("aiNormalMap", asShader=True, name="_NormalMap")
    pm.defaultNavigation(ce=True, s=file_normal +
                         ".outColor", d=ai_normal + ".input")
    pm.defaultNavigation(ce=True, s=ai_normal + ".outValue",
                         d=ai_mat + ".normalCamera")
    pm.setAttr(file_normal + ".colorSpace", "Raw", type="string")
    pm.setAttr(file_normal + ".ignoreColorSpaceFileRules", 1)
    pm.setAttr(file_normal + ".fileTextureName", txNormal, type="string")


def createAll(ws):
    importTextureFile(ws)
    materialSetup(ws)


def run():
    with pm.window(t="EzMaterialCreate") as wn:
        with pm.columnLayout(w=400):
            ws = {}
            with pm.frameLayout(l="Select Maps", w=400):
                pm.separator()
                with pm.horizontalLayout():
                    pm.text(l="Diffuse", al="left")
                    pm.textField("tfDiffuse", text="not selected", w=200)
                    pm.button(label="Select",
                              command=pm.Callback(selectDiff, ws))
                pm.separator()
                with pm.horizontalLayout():
                    pm.text(l="Metalness", al="left")
                    pm.textField("tfMetalness", text="not selected", w=200)
                    pm.button(label="Select",
                              command=pm.Callback(selectMetal, ws))
                pm.separator()
                with pm.horizontalLayout():
                    pm.text(l="Roughness", al="left")
                    pm.textField("tfRoughness", text="not selected", w=200)
                    pm.button(label="Select",
                              command=pm.Callback(selectRough, ws))
                pm.separator()
                with pm.horizontalLayout():
                    pm.text(l="Normal", al="left")
                    pm.textField("tfNormal", text="not selected", w=200)
                    pm.button(label="Select",
                              command=pm.Callback(selectNormal, ws))
                pm.separator()
                with pm.autoLayout():
                    pm.button(label="Create Rig",
                              command=pm.Callback(createAll, ws))

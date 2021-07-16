import pymel.core as pm


# Open explorer
def browserDiff(ws):
    try:
        imgFilter = "ImageFiles (*.*)"
        mapDiff = pm.fileDialog2(ff=imgFilter, ds=1, fm=1)
        textDiff = mapDiff[0]
        pm.textField("tfDiffuse", edit=1, text=textDiff)
    except TypeError:
        pass


def browserMetal(ws):
    try:
        imgFilter = "ImageFiles (*.*)"
        mapMetal = pm.fileDialog2(ff=imgFilter, ds=1, fm=1)
        textMetal = mapMetal[0]
        pm.textField("tfMetalness", edit=1, text=textMetal)
    except TypeError:
        pass


def browserRough(ws):
    try:
        imgFilter = "ImageFiles (*.*)"
        mapRough = pm.fileDialog2(ff=imgFilter, ds=1, fm=1)
        textRough = mapRough[0]
        pm.textField("tfRoughness", edit=1, text=textRough)
    except TypeError:
        pass


def browserNormal(ws):
    try:
        imgFilter = "ImageFiles (*.*)"
        mapNormal = pm.fileDialog2(ff=imgFilter, ds=1, fm=1)
        textNormal = mapNormal[0]
        pm.textField("tfNormal", edit=1, text=textNormal)
    except TypeError:
        pass


# Get file path
def setDiffMapPath(ws):
    global txDiff
    txDiff = ""
    text_in_d = pm.textField('tfDiffuse', q=True, text=True)
    txDiff = text_in_d


def setMetalMapPath(ws):
    global txMetal
    txMetal = ""
    text_in_m = pm.textField('tfMetalness', q=True, text=True)
    txMetal = text_in_m


def setRoughMapPath(ws):
    global txRough
    txRough = ""
    text_in_r = pm.textField('tfRoughness', q=True, text=True)
    txRough = text_in_r


def setNormalMapPath(ws):
    global txNormal
    txNormal = ""
    text_in_n = pm.textField('tfNormal', q=True, text=True)
    txNormal = text_in_n


def selectDiff(ws):
    browserDiff(ws)
    setDiffMapPath(ws)


def selectMetal(ws):
    browserMetal(ws)
    setMetalMapPath(ws)


def selectRough(ws):
    browserRough(ws)
    setRoughMapPath(ws)


def selectNormal(ws):
    browserNormal(ws)
    setNormalMapPath(ws)


# Import textures
def importTextureFile(ws):
    if pm.checkBox("cbDif", q=True, v=True) or pm.checkBox("cbMet", q=True, v=True) or pm.checkBox("cbRou", q=True, v=True) or pm.checkBox("cbNor", q=True, v=True):
        coord2d = pm.shadingNode(
            "place2dTexture", asUtility=True, name="Coords")
        if pm.checkBox("cbDif", q=True, v=True):
            global file_diff
            file_diff = pm.shadingNode("file", asTexture=True, name="Diffuse")
            pm.defaultNavigation(ce=True, s=coord2d, d=file_diff)

        if pm.checkBox("cbMet", q=True, v=True):
            global file_metal
            file_metal = pm.shadingNode(
                "file", asTexture=True, name="Metalness")
            pm.defaultNavigation(ce=True, s=coord2d, d=file_metal)

        if pm.checkBox("cbRou", q=True, v=True):
            global file_rough
            file_rough = pm.shadingNode(
                "file", asTexture=True, name="Roughness")
            pm.defaultNavigation(ce=True, s=coord2d, d=file_rough)

        if pm.checkBox("cbNor", q=True, v=True):
            global file_normal
            file_normal = pm.shadingNode("file", asTexture=True, name="Normal")
            pm.defaultNavigation(ce=True, s=coord2d, d=file_normal)

        else:
            pass
    else:
        pm.warning(
            "None of the checkboxes are checked. Please select some checkbox.")


# Setup aiStandardSurface
def materialSetup(ws):
    if pm.checkBox("cbDif", q=True, v=True) or pm.checkBox("cbMet", q=True, v=True) or pm.checkBox("cbRou", q=True, v=True) or pm.checkBox("cbNor", q=True, v=True):
        ai_mat = pm.shadingNode("aiStandardSurface",
                                asShader=True, name="_Mat")

        # Diffuse
        if pm.checkBox("cbDif", q=True, v=True):
            try:
                pm.defaultNavigation(
                    ce=True, s=file_diff + ".outColor", d=ai_mat + ".baseColor")
                pm.setAttr(file_diff + ".ignoreColorSpaceFileRules", 1)
                pm.setAttr(file_diff + ".fileTextureName",
                           txDiff, type="string")
            except NameError:
                pm.warning(
                    "DiffuseMap is not selected. Please select DiffuseMap and click OK button")
        print txDiff

        # Metalness
        if pm.checkBox("cbMet", q=True, v=True):
            try:
                pm.defaultNavigation(
                    ce=True, s=file_metal + ".outAlpha", d=ai_mat + ".metalness")
                pm.setAttr(file_metal + ".colorSpace", "Raw", type="string")
                pm.setAttr(file_metal + ".alphaIsLuminance", 1)
                pm.setAttr(file_metal + ".ignoreColorSpaceFileRules", 1)
                pm.setAttr(file_metal + ".fileTextureName",
                           txMetal, type="string")
            except NameError:
                pm.warning(
                    "MetalnessMap is not selected. Please select MetalnessMap and click OK button")

        # Roughness
        if pm.checkBox("cbRou", q=True, v=True):
            try:
                pm.defaultNavigation(ce=True, s=file_rough + ".outAlpha",
                                     d=ai_mat + ".specularRoughness")
                pm.setAttr(file_rough + ".colorSpace", "Raw", type="string")
                pm.setAttr(file_rough + ".alphaIsLuminance", 1)
                pm.setAttr(file_rough + ".ignoreColorSpaceFileRules", 1)
                pm.setAttr(file_rough + ".fileTextureName",
                           txRough, type="string")
            except NameError:
                pm.warning(
                    "RoughnessMap is not selected. Please select RoughnessMap and click OK button")

        # Normal
        if pm.checkBox("cbNor", q=True, v=True):
            try:
                ai_normal = pm.shadingNode(
                    "aiNormalMap", asShader=True, name="_NormalMap")
                pm.defaultNavigation(ce=True, s=file_normal +
                                     ".outColor", d=ai_normal + ".input")
                pm.defaultNavigation(ce=True, s=ai_normal + ".outValue",
                                     d=ai_mat + ".normalCamera")
                pm.setAttr(file_normal + ".colorSpace", "Raw", type="string")
                pm.setAttr(file_normal + ".ignoreColorSpaceFileRules", 1)
                pm.setAttr(file_normal + ".fileTextureName",
                           txNormal, type="string")
            except NameError:
                pm.warning(
                    "NormalMap is not selected. Please select NormalMap and click OK button")

        else:
            pass

    else:
        pm.warning(
            "None of the checkboxes are checked. Please select some checkbox.")


def createAll(ws):
    importTextureFile(ws)
    materialSetup(ws)


# ui
def run():
    with pm.window(t="EzCreateMaterial") as wn:
        global txDiff, txMetal, txRough, txNormal
        txDiff = ""
        txMetal = ""
        txRough = ""
        txNormal = ""
        with pm.columnLayout(w=400):
            ws = {}
            with pm.frameLayout(l="Select Maps", w=400):
                pm.separator()
                with pm.horizontalLayout():
                    pm.checkBox("cbDif", l="Diffuse", v=True)
                    pm.textField("tfDiffuse", text="not selected",
                                 cc=pm.Callback(setDiffMapPath, ws), w=230)
                    pm.symbolButton("browser1", image="navButtonBrowse.png",
                                    command=pm.Callback(selectDiff, ws))
                pm.separator()
                with pm.horizontalLayout():
                    pm.checkBox("cbMet", l="Metalness", v=True)
                    pm.textField("tfMetalness", text="not selected",
                                 cc=pm.Callback(setMetalMapPath, ws), w=230)
                    pm.symbolButton("browser2", image="navButtonBrowse.png",
                                    command=pm.Callback(selectMetal, ws))
                pm.separator()
                with pm.horizontalLayout():
                    pm.checkBox("cbRou", l="Roughness", v=True)
                    pm.textField("tfRoughness", text="not selected",
                                 cc=pm.Callback(setRoughMapPath, ws), w=230)
                    pm.symbolButton("browser3", image="navButtonBrowse.png",
                                    command=pm.Callback(selectRough, ws))
                pm.separator()
                with pm.horizontalLayout():
                    pm.checkBox("cbNor", l="Normal", v=True)
                    pm.textField("tfNormal", text="not selected",
                                 cc=pm.Callback(setNormalMapPath, ws), w=230)
                    pm.symbolButton("browser4", image="navButtonBrowse.png",
                                    command=pm.Callback(selectNormal, ws))
                pm.separator()
                with pm.autoLayout():
                    pm.button(label="Create Material",
                              command=pm.Callback(createAll, ws))


run()

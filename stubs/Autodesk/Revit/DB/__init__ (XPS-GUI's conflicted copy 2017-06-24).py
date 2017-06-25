# encoding:utf-8
# module Autodesk.Revit.DB calls itself DB
# from RevitAPI,Version=17.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports
# no functions
# classes
# JEDI_FIX

class BaseExportOptions(object):
    def Dispose(self):
        pass
    def GetExportFontTable(self):
        pass
    def GetExportLayerTable(self):
        pass
    def GetExportLinetypeTable(self):
        pass
    def GetExportPatternTable(self):
        pass
    @staticmethod
    def GetPredefinedSetupNames(document):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetExportFontTable(self,fontTable):
        pass
    def SetExportLayerTable(self,layerTable):
        pass
    def SetExportLinetypeTable(self,linetypeTable):
        pass
    def SetExportPatternTable(self,patternTable):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Colors=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HatchPatternsFileName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HideReferencePlane=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HideScopeBox=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HideUnreferenceViewTags=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LayerMapping=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreserveCoincidentLines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PropOverrides=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ACADExportOptions(BaseExportOptions):
    def Dispose(self):
        pass
    ACAPreference=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportingAreas=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportOfSolids=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FileVersion=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineScaling=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LinetypesFileName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MarkNonplotLayers=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NonplotSuffix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SharedCoords=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TargetUnit=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextTreatment=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ACADVersion(Enum):
    Default=None
    R2007=None
    R2010=None
    R2013=None
    value__=None
class ACAObjectPreference(Enum):
    Geometry=None
    Object=None
    value__=None
class AdaptiveComponentFamilyUtils(object):
    @staticmethod
    def GetNumberOfAdaptivePoints(family):
        pass
    @staticmethod
    def GetNumberOfPlacementPoints(family):
        pass
    @staticmethod
    def GetNumberOfShapeHandlePoints(family):
        pass
    @staticmethod
    def GetPlacementNumber(doc,refPointId):
        pass
    @staticmethod
    def GetPointConstraintType(doc,refPointId):
        pass
    @staticmethod
    def GetPointOrientationType(doc,refPointId):
        pass
    @staticmethod
    def IsAdaptiveComponentFamily(family):
        pass
    @staticmethod
    def IsAdaptivePlacementPoint(doc,refPointId):
        pass
    @staticmethod
    def IsAdaptivePoint(doc,refPointId):
        pass
    @staticmethod
    def IsAdaptiveShapeHandlePoint(doc,refPointId):
        pass
    @staticmethod
    def MakeAdaptivePoint(doc,refPointId,type):
        pass
    @staticmethod
    def SetPlacementNumber(doc,refPointId,placementNumber):
        pass
    @staticmethod
    def SetPointConstraintType(doc,refPointId,constraintType):
        pass
    @staticmethod
    def SetPointOrientationType(doc,refPointId,orientationType):
        pass
    __all__=[
        'GetNumberOfAdaptivePoints',
        'GetNumberOfPlacementPoints',
        'GetNumberOfShapeHandlePoints',
        'GetPlacementNumber',
        'GetPointConstraintType',
        'GetPointOrientationType',
        'IsAdaptiveComponentFamily',
        'IsAdaptivePlacementPoint',
        'IsAdaptivePoint',
        'IsAdaptiveShapeHandlePoint',
        'MakeAdaptivePoint',
        'SetPlacementNumber',
        'SetPointConstraintType',
        'SetPointOrientationType',
    ]
class AdaptiveComponentInstanceUtils(object):
    @staticmethod
    def CreateAdaptiveComponentInstance(doc,famSymb):
        pass
    @staticmethod
    def GetInstancePlacementPointElementRefIds(famInst):
        pass
    @staticmethod
    def GetInstancePointElementRefIds(famInst):
        pass
    @staticmethod
    def GetInstanceShapeHandlePointElementRefIds(famInst):
        pass
    @staticmethod
    def HasAdaptiveFamilySymbol(famInst):
        pass
    @staticmethod
    def IsAdaptiveComponentInstance(famInst):
        pass
    @staticmethod
    def IsAdaptiveFamilySymbol(famSymb):
        pass
    @staticmethod
    def IsInstanceFlipped(famInst):
        pass
    @staticmethod
    def MoveAdaptiveComponentInstance(famInst,trf,unHost):
        pass
    @staticmethod
    def SetInstanceFlipped(famInst,flip):
        pass
    __all__=[
        'CreateAdaptiveComponentInstance',
        'GetInstancePlacementPointElementRefIds',
        'GetInstancePointElementRefIds',
        'GetInstanceShapeHandlePointElementRefIds',
        'HasAdaptiveFamilySymbol',
        'IsAdaptiveComponentInstance',
        'IsAdaptiveFamilySymbol',
        'IsInstanceFlipped',
        'MoveAdaptiveComponentInstance',
        'SetInstanceFlipped',
    ]
class AdaptivePointConstraintType(Enum):
    Axis_X=None
    Axis_Y=None
    Axis_Z=None
    None_JEDIFIX=None
    Plane_XY=None
    Plane_YZ=None
    Plane_ZX=None
    value__=None
class AdaptivePointOrientationType(Enum):
    ToGlobalXYZ=None
    ToGlobalZthenHost=None
    ToHost=None
    ToHostAndLoopSystem=None
    ToInstance=None
    ToInstanceZthenHost=None
    value__=None
class AdaptivePointType(Enum):
    PlacementPoint=None
    ReferencePoint=None
    ShapeHandlePoint=None
    value__=None
class AddInId(object):
    def Dispose(self):
        pass
    def GetAddInName(self):
        pass
    def GetAddInNameFromDocument(self,aDoc):
        pass
    def GetGUID(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,val):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AllowedValues(Enum):
    All=None
    NonNegative=None
    Positive=None
    value__=None
class AlphanumericRevisionSettings(object):
    def Dispose(self):
        pass
    def GetSequence(self):
        pass
    def IsEqual(self,other):
        pass
    def IsValid(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetSequence(self,sequence):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Prefix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Suffix=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AlternateUnits(Enum):
    Below=None
    None_JEDIFIX=None
    Right=None
    value__=None
class AnalyzesAsType(Enum):
    AA_Gravity=None
    AA_GravityLateral=None
    AA_Hanger=None
    AA_Lateral=None
    AA_Mat=None
    AA_Not_For_Analysis=None
    AA_SlabOneWay=None
    AA_SlabOnGrade=None
    AA_SlabTwoWay=None
    value__=None
class Element(object):
    def ArePhasesModifiable(self):
        pass
    def CanBeHidden(self,pView):
        pass
    def CanBeLocked(self):
        pass
    def CanHaveAnalyticalModel(self):
        pass
    @staticmethod
    def CanHaveTypeAssigned(document=None,elementIds=None):
        pass
    @staticmethod
    def ChangeTypeId(*__args):
        pass
    def DeleteEntity(self,schema):
        pass
    def Dispose(self):
        pass
    def GetAnalyticalModel(self):
        pass
    def GetAnalyticalModelId(self):
        pass
    def getBoundingBox(self,*args):
        pass
    @staticmethod
    def GetChangeTypeAny():
        pass
    @staticmethod
    def GetChangeTypeElementAddition():
        pass
    @staticmethod
    def GetChangeTypeElementDeletion():
        pass
    @staticmethod
    def GetChangeTypeGeometry():
        pass
    @staticmethod
    def GetChangeTypeParameter(*__args):
        pass
    def GetEntity(self,schema):
        pass
    def GetEntitySchemaGuids(self):
        pass
    def GetExternalFileReference(self):
        pass
    def GetExternalResourceReference(self,resourceType):
        pass
    def GetExternalResourceReferences(self):
        pass
    def GetGeneratingElementIds(self,geometryObject):
        pass
    def GetGeometryObjectFromReference(self,reference):
        pass
    def GetMaterialArea(self,materialId,usePaintMaterial):
        pass
    def GetMaterialIds(self,returnPaintMaterials):
        pass
    def GetMaterialVolume(self,materialId):
        pass
    def GetMonitoredLinkElementIds(self):
        pass
    def GetMonitoredLocalElementIds(self):
        pass
    def GetOrderedParameters(self):
        pass
    def GetParameterFormatOptions(self,parameterId):
        pass
    def GetParameters(self,name):
        pass
    def GetPhaseStatus(self,phaseId):
        pass
    def GetTypeId(self):
        pass
    @staticmethod
    def GetValidTypes(document=None,elementIds=None):
        pass
    def HasPhases(self):
        pass
    def IsExternalFileReference(self):
        pass
    def IsHidden(self,pView):
        pass
    def IsMonitoringLinkElement(self):
        pass
    def IsMonitoringLocalElement(self):
        pass
    def IsPhaseCreatedValid(self,createdPhaseId):
        pass
    def IsPhaseDemolishedValid(self,demolishedPhaseId):
        pass
    @staticmethod
    def IsValidType(*__args):
        pass
    def LookupParameter(self,name):
        pass
    def RefersToExternalResourceReference(self,resourceType):
        pass
    def RefersToExternalResourceReferences(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def setElementType(self,*args):
        pass
    def SetEntity(self,entity):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AssemblyInstanceId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Category=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CreatedPhaseId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DemolishedPhaseId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DesignOption=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Document=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GroupId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTransient=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LevelId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OwnerViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Parameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParametersMap=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Pinned=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UniqueId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewSpecific=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WorksetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Dimension(Element):
    def Dispose(self):
        pass
    def IsTextPositionAdjustable(self):
        pass
    def ResetTextPosition(self):
        pass
    Above=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AreSegmentsEqual=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Below=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Curve=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DimensionShape=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DimensionType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyLabel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsLocked=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderEndPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfSegments=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Prefix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    References=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Segments=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Suffix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Value=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ValueOverride=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ValueString=property(lambda self:object(),lambda self,v:None,lambda self:None)
    View=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AngularDimension(Dimension):
    @staticmethod
    def Create(document,dbView,arc,references,dimensionStyle):
        pass
    def Dispose(self):
        pass
    def SetRadius(self,radius):
        pass
class Instance(Element):
    def Dispose(self):
        pass
    def GetTotalTransform(self):
        pass
    def GetTransform(self):
        pass
class FamilyInstance(Instance):
    def AddCoping(self,cutter):
        pass
    def Dispose(self):
        pass
    def flipFacing(self):
        pass
    def FlipFromToRoom(self):
        pass
    def flipHand(self):
        pass
    def GetCopingIds(self):
        pass
    def GetFamilyPointPlacementReferences(self):
        pass
    def GetOriginalGeometry(self,options):
        pass
    def GetSpatialElementCalculationPoint(self):
        pass
    def GetSpatialElementFromToCalculationPoints(self):
        pass
    def GetSubComponentIds(self):
        pass
    def GetSweptProfile(self):
        pass
    def HasModifiedGeometry(self):
        pass
    def HasSweptProfile(self):
        pass
    def RemoveCoping(self,cutter):
        pass
    def rotate(self):
        pass
    def SetCopingIds(self,cutters):
        pass
    def Split(self,param):
        pass
    def UseInstanceGeometry(self):
        pass
    CanFlipFacing=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanFlipHand=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanFlipWorkPlane=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanRotate=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanSplit=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExtensionUtility=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FacingFlipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FacingOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HandFlipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HandOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasSpatialElementCalculationPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasSpatialElementFromToCalculationPoints=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Host=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HostFace=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HostParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Invisible=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsSlantedColumn=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsWorkPlaneFlipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MEPModel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Mirrored=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralMaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralMaterialType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralUsage=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SuperComponent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Symbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UsesInstanceGeometry=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AnnotationSymbol(FamilyInstance):
    def addLeader(self):
        pass
    def Dispose(self):
        pass
    def duplicate(self):
        pass
    def GetLeaders(self):
        pass
    def removeLeader(self):
        pass
    AnnotationSymbolType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementType(Element):
    def Dispose(self):
        pass
    def Duplicate(self,name):
        pass
    def GetPreviewImage(self,size):
        pass
    def GetSimilarTypes(self):
        pass
    def IsSimilarType(self,typeId):
        pass
    def IsValidDefaultFamilyType(self,familyCategoryId):
        pass
    CanBeCopied=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanBeDeleted=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanBeRenamed=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class InsertableObject(ElementType):
    def Dispose(self):
        pass
class FamilySymbol(InsertableObject):
    def Activate(self):
        pass
    def CanHaveStructuralSection(self):
        pass
    def Dispose(self):
        pass
    def GetFamilyPointLocations(self):
        pass
    def GetStructuralSection(self):
        pass
    def GetThermalProperties(self):
        pass
    def HasThermalProperties(self):
        pass
    def SetStructuralSection(self,structuralSection):
        pass
    def SetThermalProperties(self,thermalProperties):
        pass
    Family=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsActive=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralMaterialType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AnnotationSymbolType(FamilySymbol):
    def Dispose(self):
        pass
class APIObject(object):
    def Dispose(self):
        pass
    def ReleaseManagedResources(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsReadOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AppearanceAssetElement(Element):
    @staticmethod
    def Create(document,name,asset):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetAppearanceAssetElementByName(doc,name):
        pass
    def GetRenderingAsset(self):
        pass
    def SetRenderingAsset(self,asset):
        pass
class GeometryObject(APIObject):
    def Dispose(self):
        pass
    def Equals(self,obj):
        pass
    def GetHashCode(self):
        pass
    def __eq__(self,*args):
        pass
    def __ne__(self,*args):
        pass
    GraphicsStyleId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsElementGeometry=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visibility=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Curve(GeometryObject):
    def Clone(self):
        pass
    def ComputeDerivatives(self,parameter,normalized):
        pass
    def ComputeNormalizedParameter(self,rawParameter):
        pass
    def ComputeRawParameter(self,normalizedParameter):
        pass
    def CreateOffset(self,offsetDist,referenceVector):
        pass
    def CreateReversed(self):
        pass
    def CreateTransformed(self,transform):
        pass
    def Dispose(self):
        pass
    def Distance(self,point):
        pass
    def Evaluate(self,parameter,normalized):
        pass
    def GetEndParameter(self,index):
        pass
    def GetEndPoint(self,index):
        pass
    def GetEndPointReference(self,index):
        pass
    def Intersect(self,curve,resultArray=None):
        pass
    def IsInside(self,parameter,end=None):
        pass
    def MakeBound(self,startParameter,endParameter):
        pass
    def MakeUnbound(self):
        pass
    def Project(self,point):
        pass
    def SetGraphicsStyleId(self,id):
        pass
    def Tessellate(self):
        pass
    ApproximateLength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsBound=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCyclic=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Length=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Period=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Reference=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Arc(Curve):
    @staticmethod
    def Create(*__args):
        pass
    def Dispose(self):
        pass
    Center=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Normal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Radius=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElement(Element):
    def Dispose(self):
        pass
    def GetBoundarySegments(self,options):
        pass
    Area=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Level=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Number=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Perimeter=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Area(SpatialElement):
    def Dispose(self):
        pass
    AreaScheme=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsGrossInterior=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AreaElemType(Enum):
    BOMAArea=None
    GrossArea=None
    value__=None
class ElementFilter(object):
    def Dispose(self):
        pass
    def PassesFilter(self,*__args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Inverted=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementSlowFilter(ElementFilter):
    def Dispose(self):
        pass
class AreaFilter(ElementSlowFilter):
    def Dispose(self):
        pass
class AreaScheme(Element):
    def Dispose(self):
        pass
    IsGrossBuildingArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElementTag(Element):
    def Dispose(self):
        pass
    HasLeader=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsOrphaned=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTaggingLink=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderElbow=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderEnd=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagHeadPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    View=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AreaTag(SpatialElementTag):
    def Dispose(self):
        pass
    Area=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AreaTagType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AreaTagFilter(ElementSlowFilter):
    def Dispose(self):
        pass
class AreaTagType(FamilySymbol):
    def Dispose(self):
        pass
class AreaVolumeSettings(Element):
    def Dispose(self):
        pass
    @staticmethod
    def GetAreaVolumeSettings(aDoc):
        pass
    def GetSpatialElementBoundaryLocation(self,spType):
        pass
    def SetSpatialElementBoundaryLocation(self,spatialElementBoundaryLocation,spType):
        pass
    ComputeVolumes=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ArrayAnchorMember(Enum):
    Last=None
    Second=None
    value__=None
class KeyBasedTreeEntryTable(Element):
    def Dispose(self):
        pass
    def GetKeyBasedTreeEntries(self):
        pass
    def LoadFrom(self,desiredResourceReference,loadResults):
        pass
    def Reload(self,loadResults):
        pass
    def ServerSupports(self,extRef):
        pass
class AssemblyCodeTable(KeyBasedTreeEntryTable):
    def Dispose(self):
        pass
    @staticmethod
    def GetAssemblyCodeTable(doc):
        pass
class AssemblyDetailViewOrientation(Enum):
    DetailSectionA=None
    DetailSectionB=None
    ElevationBack=None
    ElevationBottom=None
    ElevationFront=None
    ElevationLeft=None
    ElevationRight=None
    ElevationTop=None
    HorizontalDetail=None
    value__=None
class AssemblyDifference(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AssemblyDifferenceConfiguration(AssemblyDifference):
    def Dispose(self):
        pass
class AssemblyDifferenceMemberCount(AssemblyDifference):
    def Dispose(self):
        pass
    Count1=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Count2=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AssemblyDifferenceMemberDifference(AssemblyDifference):
    def Dispose(self):
        pass
    MemberDifference=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MemberId1=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MemberId2=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AssemblyDifferenceNamingCategory(AssemblyDifference):
    def Dispose(self):
        pass
    NamingCategoryId1=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NamingCategoryId2=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AssemblyDifferenceNone(AssemblyDifference):
    def Dispose(self):
        pass
class AssemblyInstance(Element):
    def AddMemberIds(self,memberIds):
        pass
    def AllowsAssemblyViewCreation(self):
        pass
    @staticmethod
    def AreElementsValidForAssembly(document,assemblyMemberIds,assemblyId):
        pass
    @staticmethod
    def CanRemoveElementsFromAssembly(assemblyInstance,memberIds):
        pass
    @staticmethod
    def CompareAssemblyInstances(instance1,instance2):
        pass
    @staticmethod
    def Create(document,assemblyMemberIds,namingCategoryId):
        pass
    def Disassemble(self):
        pass
    def Dispose(self):
        pass
    def GetCenter(self):
        pass
    def GetMemberIds(self):
        pass
    def GetTransform(self):
        pass
    @staticmethod
    def IsValidNamingCategory(document,namingCategoryId,assemblyMemberIds):
        pass
    @staticmethod
    def PlaceInstance(document,assemblyTypeId,location):
        pass
    def RemoveMemberIds(self,memberIds):
        pass
    def SetMemberIds(self,memberIds):
        pass
    def SetTransform(self,trf):
        pass
    AssemblyTypeName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NamingCategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AssemblyMemberDifference(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AssemblyMemberDifferentCategory(AssemblyMemberDifference):
    def Dispose(self):
        pass
    CategoryId1=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CategoryId2=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AssemblyMemberDifferentGeometry(AssemblyMemberDifference):
    def Dispose(self):
        pass
class AssemblyMemberDifferentParameters(AssemblyMemberDifference):
    def Dispose(self):
        pass
class AssemblyMemberDifferentType(AssemblyMemberDifference):
    def Dispose(self):
        pass
    TypeId1=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TypeId2=property(lambda self:object(),lambda self,v:None,lambda self:None)
class AssemblyType(ElementType):
    def Dispose(self):
        pass
class AssemblyViewUtils(object):
    @staticmethod
    def AcquireAssemblyViews(document,sourceAssemblyInstanceId,targetAssemblyInstanceId):
        pass
    @staticmethod
    def Create3DOrthographic(document,assemblyInstanceId,viewTemplateId=None,isAssigned=None):
        pass
    @staticmethod
    def CreateDetailSection(document,assemblyInstanceId,direction,viewTemplateId=None,isAssigned=None):
        pass
    @staticmethod
    def CreateMaterialTakeoff(document,assemblyInstanceId,viewTemplateId=None,isAssigned=None):
        pass
    @staticmethod
    def CreatePartList(document,assemblyInstanceId,viewTemplateId=None,isAssigned=None):
        pass
    @staticmethod
    def CreateSheet(document,assemblyInstanceId,titleBlockId):
        pass
    @staticmethod
    def CreateSingleCategorySchedule(document,assemblyInstanceId,scheduleCategoryId,viewTemplateId=None,isAssigned=None):
        pass
    __all__=[
        'AcquireAssemblyViews',
        'Create3DOrthographic',
        'CreateDetailSection',
        'CreateMaterialTakeoff',
        'CreatePartList',
        'CreateSheet',
        'CreateSingleCategorySchedule',
    ]
class AttachmentType(Enum):
    Attachment=None
    Overlay=None
    value__=None
class AutomaticConnectionBehaviorType(Enum):
    Accepting=None
    Active=None
    Exclude=None
    Forced=None
    Full=None
    value__=None
class BackgroundImageFit(Enum):
    Horizontal=None
    None_JEDIFIX=None
    Stretch=None
    value__=None
    Vertical=None
class BackgroundSettings(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BackgroundStyle(Enum):
    Color=None
    Image=None
    SkyCloudy=None
    SkyFewClouds=None
    SkyNoClouds=None
    SkyVeryCloudy=None
    SkyVeryFewClouds=None
    Transparent=None
    value__=None
class BaseArray(Element):
    def Dispose(self):
        pass
    def GetCopiedMemberIds(self):
        pass
    def GetOriginalMemberIds(self):
        pass
    Label=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumMembers=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BaseImportOptions(object):
    def Dispose(self):
        pass
    def GetLayerSelection(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetLayerSelection(self,layerSelection):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AutoCorrectAlmostVHLines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ColorMode=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CustomScale=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OrientToView=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Placement=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReferencePoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThisViewOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Unit=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VisibleLayersOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BaseLoadOn(Enum):
    kNoOfBaseLoadOnMethods=None
    kUseActualLoad=None
    kUseCalculatedLoad=None
    kUseDefaultLoad=None
    kUseEnteredLoad=None
    value__=None
class BasePoint(Element):
    def Dispose(self):
        pass
    IsShared=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BasicFileInfo(object):
    def Dispose(self):
        pass
    @staticmethod
    def Extract(file):
        pass
    def GetDocumentVersion(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AllLocalChangesSavedToCentral=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CentralPath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCentral=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCreatedLocal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsInProgress=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsLocal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsSavedInCurrentVersion=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsSavedInLaterVersion=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsWorkshared=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LanguageWhenSaved=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LatestCentralEpisodeGUID=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LatestCentralVersion=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SavedInVersion=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Username=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BeamSystem(Element):
    @staticmethod
    def BeamBelongsTo(beam):
        pass
    @staticmethod
    def Create(document,profile,*__args):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def DropBeamSystem(beamSystem):
        pass
    def GetBeamIds(self):
        pass
    BeamSystemType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BeamType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Direction=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Elevation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LayoutRule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Level=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Profile=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BeamSystemJustifyType(Enum):
    Beginning=None
    Center=None
    DirectionLine=None
    End=None
    value__=None
class BeamSystemType(ElementType):
    def Dispose(self):
        pass
class BehaviorType(Enum):
    BaseObject=None
    Bend=None
    Branch=None
    BreakInto=None
    Coupling=None
    ElectricalBaseObject=None
    EndCap=None
    Flange=None
    Flat_Tap=None
    Flex=None
    Hanger=None
    Inline=None
    Intersection=None
    Invalid=None
    MechanicalCoupling=None
    Normal=None
    OrientToCenterLine=None
    OrientToFace=None
    OrientToObject=None
    Oval_CentreLine_Tap=None
    Round_CentreLine_Tap=None
    Straight=None
    SystemMember=None
    value__=None
    Valve=None
    VerticalBend=None
class Binding(APIObject):
    def Dispose(self):
        pass
class DefinitionBindingMap(APIObject):
    def Clear(self):
        pass
    def Contains(self,key):
        pass
    def Dispose(self):
        pass
    def Erase(self,key):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,key,item):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BindingMap(DefinitionBindingMap):
    def Clear(self):
        pass
    def Contains(self,key):
        pass
    def Dispose(self):
        pass
    def Erase(self,key):
        pass
    def Insert(self,key,item,parameterGroup=None):
        pass
    def ReInsert(self,key,item,parameterGroup=None):
        pass
    def Remove(self,key):
        pass
class CombinableElement(Element):
    def Dispose(self):
        pass
    Combinations=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GenericForm(CombinableElement):
    def Dispose(self):
        pass
    def GetVisibility(self):
        pass
    def SetVisibility(self,visibility):
        pass
    IsSolid=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Subcategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visible=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Blend(GenericForm):
    def Dispose(self):
        pass
    def GetVertexConnectionMap(self):
        pass
    def SetVertexConnectionMap(self,vertexMap):
        pass
    BottomOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BottomProfile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BottomSketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopProfile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopSketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BooleanOperationsType(Enum):
    Difference=None
    Intersect=None
    Union=None
    value__=None
class BooleanOperationsUtils(object):
    @staticmethod
    def CutWithHalfSpace(solid,plane):
        pass
    @staticmethod
    def CutWithHalfSpaceModifyingOriginalSolid(solid,plane):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def ExecuteBooleanOperation(solid0,solid1,booleanType):
        pass
    @staticmethod
    def ExecuteBooleanOperationModifyingOriginalSolid(solid0,solid1,booleanType):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BorderTile(Enum):
    Empty=None
    Overhanging=None
    Partial=None
    value__=None
class BoundarySegment(object):
    def Dispose(self):
        pass
    def GetCurve(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LinkElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementQuickFilter(ElementFilter):
    def Dispose(self):
        pass
class BoundingBoxContainsPointFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,point,*__args):
        pass
    Point=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Tolerance=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BoundingBoxIntersectsFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    def GetBoundingBox(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,outline,*__args):
        pass
    Tolerance=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BoundingBoxIsInsideFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    def GetBoundingBox(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,outline,*__args):
        pass
    Tolerance=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BoundingBoxUV(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,min_u=None,min_v=None,max_u=None,max_v=None):
        pass
    Max=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Min=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BoundingBoxXYZ(APIObject):
    def Dispose(self):
        pass
    Enabled=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Max=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Min=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transform=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BoxPlacement(Enum):
    BottomLeft=None
    BottomRight=None
    Center=None
    TopLeft=None
    TopRight=None
    value__=None
class ShapeBuilder(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BRepBuilder(ShapeBuilder):
    def AddCoEdge(self,loopId,edgeId,bCoEdgeIsReversed):
        pass
    def AddEdge(self,edgeGeom):
        pass
    def AddFace(self,surfaceGeom,bFaceIsReversed):
        pass
    def AddLoop(self,faceId):
        pass
    def AllowRemovalOfProblematicFaces(self):
        pass
    def CanAddGeometry(self):
        pass
    def Dispose(self):
        pass
    def Finish(self):
        pass
    def FinishFace(self,faceId):
        pass
    def FinishLoop(self,loopId):
        pass
    def GetResult(self):
        pass
    @staticmethod
    def IsPermittedSurfaceType(surface):
        pass
    def IsResultAvailable(self):
        pass
    def IsValidEdgeId(self,edgeId):
        pass
    def IsValidFaceId(self,faceId):
        pass
    def IsValidLoopId(self,loopId):
        pass
    def RemovedSomeFaces(self):
        pass
    def SetAllowShortEdges(self):
        pass
    def SetFaceMaterialId(self,faceId,materialId):
        pass
    @staticmethod # known case of __new__
    def __new__(self,geomType):
        pass
class BRepBuilderEdgeGeometry(object):
    @staticmethod
    def Create(*__args):
        pass
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BRepBuilderGeometryId(object):
    def Dispose(self):
        pass
    @staticmethod
    def InvalidGeometryId():
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BRepBuilderOutcome(Enum):
    Failure=None
    Success=None
    value__=None
class BRepBuilderState(Enum):
    AcceptingData=None
    Completed=None
    InvalidState=None
    value__=None
class BRepBuilderSurfaceGeometry(object):
    @staticmethod
    def Create(surface,surfaceEnvelope):
        pass
    @staticmethod
    def CreateNURBSSurface(degreeU,degreeV,knotsU,knotsV,controlPoints,*__args):
        pass
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BRepType(Enum):
    OpenShell=None
    Solid=None
    value__=None
    Void=None
class BrowserOrganization(ElementType):
    def AreFiltersSatisfied(self,elementId):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetCurrentBrowserOrganizationForSheets(document):
        pass
    @staticmethod
    def GetCurrentBrowserOrganizationForViews(document):
        pass
    def GetFolderItems(self,elementId):
        pass
    SortingOrder=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SortingParameterId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BrowserOrganizationType(Enum):
    Families=None
    Sheets=None
    value__=None
    Views=None
class HostObjAttributes(ElementType):
    def Dispose(self):
        pass
    def GetCompoundStructure(self):
        pass
    def SetCompoundStructure(self,compoundStructure):
        pass
class BuildingPadType(HostObjAttributes):
    @staticmethod
    def CreateDefault(document):
        pass
    def Dispose(self):
        pass
    ThermalProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BuildingSiteExportOptions(object):
    AreaPerPerson=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PropertyLine=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PropertyLineOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TotalGrossArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TotalOccupancy=property(lambda self:object(),lambda self,v:None,lambda self:None)
class BuildingType(Enum):
    kAutomotiveFacility=None
    kConventionCenter=None
    kCourthouse=None
    kDiningBarLoungeOrLeisure=None
    kDiningCafeteriaFastFood=None
    kDiningFamily=None
    kDormitory=None
    kExerciseCenter=None
    kFireStation=None
    kGymnasium=None
    kHospitalOrHealthcare=None
    kHotel=None
    kLibrary=None
    kManufacturing=None
    kMotel=None
    kMotionPictureTheatre=None
    kMultiFamily=None
    kMuseum=None
    kNoOfBuildingTypes=None
    kOffice=None
    kParkingGarage=None
    kPenitentiary=None
    kPerformingArtsTheater=None
    kPoliceStation=None
    kPostOffice=None
    kReligiousBuilding=None
    kRetail=None
    kSchoolOrUniversity=None
    kSportsArena=None
    kTownHall=None
    kTransportation=None
    kWarehouse=None
    kWorkshop=None
    value__=None
class BuiltInCategory(Enum):
    INVALID=None
    OST_AdaptivePoints=None
    OST_AdaptivePoints_HiddenLines=None
    OST_AdaptivePoints_Lines=None
    OST_AdaptivePoints_Planes=None
    OST_AdaptivePoints_Points=None
    OST_AlwaysExcludedInAllViews=None
    OST_Analemma=None
    OST_AnalysisDisplayStyle=None
    OST_AnalysisResults=None
    OST_AnalyticalNodes=None
    OST_AnalyticalNodes_Lines=None
    OST_AnalyticalNodes_Planes=None
    OST_AnalyticalNodes_Points=None
    OST_AnalyticalRigidLinks=None
    OST_AnalyticSpaces=None
    OST_AnalyticSurfaces=None
    OST_AnnotationCrop=None
    OST_AnnotationCropSpecial=None
    OST_AppearanceAsset=None
    OST_ArcWallRectOpening=None
    OST_AreaColorFill=None
    OST_AreaInteriorFill=None
    OST_AreaInteriorFillVisibility=None
    OST_AreaLoads=None
    OST_AreaLoadTags=None
    OST_AreaPolylines=None
    OST_AreaReference=None
    OST_AreaReferenceVisibility=None
    OST_AreaRein=None
    OST_AreaReinBoundary=None
    OST_AreaReinSketchOverride=None
    OST_AreaReinSpanSymbol=None
    OST_AreaReinTags=None
    OST_AreaReinXVisibility=None
    OST_AreaReport_Arc_Minus=None
    OST_AreaReport_Arc_Plus=None
    OST_AreaReport_Boundary=None
    OST_AreaReport_Triangle=None
    OST_Areas=None
    OST_AreaSchemeLines=None
    OST_AreaSchemes=None
    OST_AreaTags=None
    OST_Assemblies=None
    OST_AssemblyOrigin=None
    OST_AssemblyOrigin_Lines=None
    OST_AssemblyOrigin_Planes=None
    OST_AssemblyOrigin_Points=None
    OST_AssemblyTags=None
    OST_Automatic=None
    OST_AxisOfRotation=None
    OST_AxisX=None
    OST_AxisY=None
    OST_AxisZ=None
    OST_BasePointAxisX=None
    OST_BasePointAxisY=None
    OST_BasePointAxisZ=None
    OST_BeamAnalytical=None
    OST_BeamAnalyticalTags=None
    OST_BeamEndSegment=None
    OST_BeamLocalCoordSys=None
    OST_BeamStartSegment=None
    OST_BeamSystemTags=None
    OST_Blocks=None
    OST_BoundaryConditions=None
    OST_BraceAnalytical=None
    OST_BraceAnalyticalTags=None
    OST_BraceEndSegment=None
    OST_BraceLocalCoordSys=None
    OST_BraceStartSegment=None
    OST_BranchPanelScheduleTemplates=None
    OST_BrokenSectionLine=None
    OST_BuildingPad=None
    OST_CableTray=None
    OST_CableTrayCenterLine=None
    OST_CableTrayDrop=None
    OST_CableTrayFitting=None
    OST_CableTrayFittingCenterLine=None
    OST_CableTrayFittingTags=None
    OST_CableTrayRiseDrop=None
    OST_CableTrayRun=None
    OST_CableTrayTags=None
    OST_Cage=None
    OST_CalloutBoundary=None
    OST_CalloutHeads=None
    OST_CalloutLeaderLine=None
    OST_Callouts=None
    OST_Cameras=None
    OST_Camera_Lines=None
    OST_Casework=None
    OST_CaseworkHiddenLines=None
    OST_CaseworkTags=None
    OST_Catalogs=None
    OST_CeilingOpening=None
    OST_Ceilings=None
    OST_CeilingsCut=None
    OST_CeilingsCutPattern=None
    OST_CeilingsDefault=None
    OST_CeilingsFinish1=None
    OST_CeilingsFinish2=None
    OST_CeilingsHiddenLines=None
    OST_CeilingsInsulation=None
    OST_CeilingsMembrane=None
    OST_CeilingsProjection=None
    OST_CeilingsStructure=None
    OST_CeilingsSubstrate=None
    OST_CeilingsSurfacePattern=None
    OST_CeilingTags=None
    OST_CenterLines=None
    OST_CLines=None
    OST_CloudLines=None
    OST_ColorFillLegends=None
    OST_ColorFillSchema=None
    OST_ColumnAnalytical=None
    OST_ColumnAnalyticalGeometry=None
    OST_ColumnAnalyticalRigidLinks=None
    OST_ColumnAnalyticalTags=None
    OST_ColumnEndSegment=None
    OST_ColumnLocalCoordSys=None
    OST_ColumnOpening=None
    OST_Columns=None
    OST_ColumnsHiddenLines=None
    OST_ColumnStartSegment=None
    OST_CommunicationDevices=None
    OST_CommunicationDeviceTags=None
    OST_CompassInner=None
    OST_CompassOuter=None
    OST_CompassPrimaryMonth=None
    OST_CompassSecondaryMonth=None
    OST_CompassSection=None
    OST_CompassSectionFilled=None
    OST_ComponentRepeater=None
    OST_ComponentRepeaterSlot=None
    OST_Conduit=None
    OST_ConduitCenterLine=None
    OST_ConduitDrop=None
    OST_ConduitFitting=None
    OST_ConduitFittingCenterLine=None
    OST_ConduitFittingTags=None
    OST_ConduitRiseDrop=None
    OST_ConduitRun=None
    OST_ConduitStandards=None
    OST_ConduitTags=None
    OST_ConnectorElem=None
    OST_ConnectorElemXAxis=None
    OST_ConnectorElemYAxis=None
    OST_ConnectorElemZAxis=None
    OST_Constraints=None
    OST_ContourLabels=None
    OST_ControlAxisX=None
    OST_ControlAxisY=None
    OST_ControlAxisZ=None
    OST_ControlLocal=None
    OST_CoordinateSystem=None
    OST_Cornices=None
    OST_Coupler=None
    OST_CouplerHiddenLines=None
    OST_CouplerTags=None
    OST_CoverType=None
    OST_CropBoundary=None
    OST_CropBoundarySpecial=None
    OST_CurtainGrids=None
    OST_CurtainGridsCurtaSystem=None
    OST_CurtainGridsRoof=None
    OST_CurtainGridsSystem=None
    OST_CurtainGridsWall=None
    OST_CurtainWallMullions=None
    OST_CurtainWallMullionsCut=None
    OST_CurtainWallMullionsHiddenLines=None
    OST_CurtainWallPanels=None
    OST_CurtainWallPanelsHiddenLines=None
    OST_CurtainWallPanelTags=None
    OST_Curtain_Systems=None
    OST_CurtaSystem=None
    OST_CurtaSystemFaceManager=None
    OST_CurtaSystemHiddenLines=None
    OST_CurtaSystemTags=None
    OST_Curves=None
    OST_CurvesMediumLines=None
    OST_CurvesThinLines=None
    OST_CurvesWideLines=None
    OST_CutOutlines=None
    OST_DataDevices=None
    OST_DataDeviceTags=None
    OST_DataPanelScheduleTemplates=None
    OST_DecalElement=None
    OST_DecalType=None
    OST_DemolishedLines=None
    OST_DesignOptions=None
    OST_DesignOptionSets=None
    OST_DetailComponents=None
    OST_DetailComponentsHiddenLines=None
    OST_DetailComponentTags=None
    OST_Dimensions=None
    OST_DimLockControlLeader=None
    OST_DirectionEdgeLines=None
    OST_DisplacementElements=None
    OST_DisplacementPath=None
    OST_DividedPath=None
    OST_DividedSurface=None
    OST_DividedSurfaceBelt=None
    OST_DividedSurface_DiscardedDivisionLines=None
    OST_DividedSurface_Gridlines=None
    OST_DividedSurface_Nodes=None
    OST_DividedSurface_PatternFill=None
    OST_DividedSurface_PatternLines=None
    OST_DividedSurface_PreDividedSurface=None
    OST_DividedSurface_TransparentFace=None
    OST_DivisionProfile=None
    OST_DivisionRules=None
    OST_Divisions=None
    OST_Doors=None
    OST_DoorsFrameMullionCut=None
    OST_DoorsFrameMullionProjection=None
    OST_DoorsGlassCut=None
    OST_DoorsGlassProjection=None
    OST_DoorsHiddenLines=None
    OST_DoorsOpeningCut=None
    OST_DoorsOpeningProjection=None
    OST_DoorsPanelCut=None
    OST_DoorsPanelProjection=None
    OST_DoorTags=None
    OST_DormerOpeningIncomplete=None
    OST_DSR_ArrowHeadStyleId=None
    OST_DSR_CenterlinePatternCatId=None
    OST_DSR_CenterlineTickMarkStyleId=None
    OST_DSR_DimStyleHeavyEndCategoryId=None
    OST_DSR_DimStyleHeavyEndCatId=None
    OST_DSR_DimStyleTickCategoryId=None
    OST_DSR_InteriorTickMarkStyleId=None
    OST_DSR_LeaderTickMarkStyleId=None
    OST_DSR_LineAndTextAttrCategoryId=None
    OST_DSR_LineAndTextAttrFontId=None
    OST_DuctAccessory=None
    OST_DuctAccessoryTags=None
    OST_DuctColorFillLegends=None
    OST_DuctColorFills=None
    OST_DuctCurves=None
    OST_DuctCurvesCenterLine=None
    OST_DuctCurvesContour=None
    OST_DuctCurvesDrop=None
    OST_DuctCurvesInsulation=None
    OST_DuctCurvesLining=None
    OST_DuctCurvesRiseDrop=None
    OST_DuctFitting=None
    OST_DuctFittingCenterLine=None
    OST_DuctFittingInsulation=None
    OST_DuctFittingLining=None
    OST_DuctFittingTags=None
    OST_DuctInsulations=None
    OST_DuctInsulationsTags=None
    OST_DuctLinings=None
    OST_DuctLiningsTags=None
    OST_DuctSystem=None
    OST_DuctSystem_Reference=None
    OST_DuctSystem_Reference_Visibility=None
    OST_DuctTags=None
    OST_DuctTerminal=None
    OST_DuctTerminalTags=None
    OST_EAConstructions=None
    OST_EdgeSlab=None
    OST_EditCutProfile=None
    OST_ElecDistributionSys=None
    OST_ElectricalCircuit=None
    OST_ElectricalCircuitTags=None
    OST_ElectricalDemandFactor=None
    OST_ElectricalDemandFactorDefinitions=None
    OST_ElectricalEquipment=None
    OST_ElectricalEquipmentHiddenLines=None
    OST_ElectricalEquipmentTags=None
    OST_ElectricalFixtures=None
    OST_ElectricalFixturesHiddenLines=None
    OST_ElectricalFixtureTags=None
    OST_ElectricalInternalCircuits=None
    OST_ElectricalLoadClassifications=None
    OST_ElectricalVoltage=None
    OST_Elev=None
    OST_ElevationMarks=None
    OST_Entourage=None
    OST_EntourageHiddenLines=None
    OST_EPS_Demolished=None
    OST_EPS_Existing=None
    OST_EPS_Future=None
    OST_EPS_New=None
    OST_EPS_Temporary=None
    OST_Extrusions=None
    OST_FabricAreaBoundary=None
    OST_FabricAreas=None
    OST_FabricAreaSketchEnvelopeLines=None
    OST_FabricAreaSketchSheetsLines=None
    OST_FabricAreaTags=None
    OST_FabricationContainment=None
    OST_FabricationContainmentCenterLine=None
    OST_FabricationContainmentDrop=None
    OST_FabricationContainmentRise=None
    OST_FabricationContainmentSymbology=None
    OST_FabricationContainmentTags=None
    OST_FabricationDuctwork=None
    OST_FabricationDuctworkCenterLine=None
    OST_FabricationDuctworkDrop=None
    OST_FabricationDuctworkInsulation=None
    OST_FabricationDuctworkLining=None
    OST_FabricationDuctworkRise=None
    OST_FabricationDuctworkSymbology=None
    OST_FabricationDuctworkTags=None
    OST_FabricationHangers=None
    OST_FabricationHangerTags=None
    OST_FabricationPartsTmpGraphicDrag=None
    OST_FabricationPartsTmpGraphicEnd=None
    OST_FabricationPipework=None
    OST_FabricationPipeworkCenterLine=None
    OST_FabricationPipeworkDrop=None
    OST_FabricationPipeworkInsulation=None
    OST_FabricationPipeworkRise=None
    OST_FabricationPipeworkSymbology=None
    OST_FabricationPipeworkTags=None
    OST_FabricationServiceElements=None
    OST_FabricReinforcement=None
    OST_FabricReinforcementBoundary=None
    OST_FabricReinforcementTags=None
    OST_FabricReinforcementWire=None
    OST_FabricReinSpanSymbol=None
    OST_FaceSplitter=None
    OST_Fascia=None
    OST_FilledRegion=None
    OST_FillPatterns=None
    OST_FireAlarmDevices=None
    OST_FireAlarmDeviceTags=None
    OST_Fixtures=None
    OST_FlexDuctCurves=None
    OST_FlexDuctCurvesCenterLine=None
    OST_FlexDuctCurvesContour=None
    OST_FlexDuctCurvesInsulation=None
    OST_FlexDuctCurvesPattern=None
    OST_FlexDuctTags=None
    OST_FlexPipeCurves=None
    OST_FlexPipeCurvesCenterLine=None
    OST_FlexPipeCurvesContour=None
    OST_FlexPipeCurvesInsulation=None
    OST_FlexPipeCurvesPattern=None
    OST_FlexPipeTags=None
    OST_FloorAnalytical=None
    OST_FloorAnalyticalTags=None
    OST_FloorLocalCoordSys=None
    OST_FloorOpening=None
    OST_Floors=None
    OST_FloorsAnalyticalGeometry=None
    OST_FloorsCut=None
    OST_FloorsCutPattern=None
    OST_FloorsDefault=None
    OST_FloorsFinish1=None
    OST_FloorsFinish2=None
    OST_FloorsInsulation=None
    OST_FloorsInteriorEdges=None
    OST_FloorsMembrane=None
    OST_FloorsProjection=None
    OST_FloorsStructure=None
    OST_FloorsSubstrate=None
    OST_FloorsSurfacePattern=None
    OST_FloorTags=None
    OST_Fluids=None
    OST_FndSlabLocalCoordSys=None
    OST_FootingAnalyticalGeometry=None
    OST_FootingSpanDirectionSymbol=None
    OST_FoundationSlabAnalytical=None
    OST_FoundationSlabAnalyticalTags=None
    OST_FramingAnalyticalGeometry=None
    OST_Furniture=None
    OST_FurnitureHiddenLines=None
    OST_FurnitureSystems=None
    OST_FurnitureSystemsHiddenLines=None
    OST_FurnitureSystemTags=None
    OST_FurnitureTags=None
    OST_GbXMLFaces=None
    OST_gbXML_Ceiling=None
    OST_gbXML_ExteriorWall=None
    OST_gbXML_FixedSkylight=None
    OST_gbXML_FixedWindow=None
    OST_gbXML_InteriorFloor=None
    OST_gbXML_InteriorWall=None
    OST_gbXML_NonSlidingDoor=None
    OST_GbXML_Opening=None
    OST_gbXML_OpeningAir=None
    OST_gbXML_OperableSkylight=None
    OST_gbXML_OperableWindow=None
    OST_gbXML_RaisedFloor=None
    OST_gbXML_Roof=None
    OST_gbXML_Shade=None
    OST_gbXML_SlabOnGrade=None
    OST_gbXML_SlidingDoor=None
    OST_GbXML_SType_Exterior=None
    OST_GbXML_SType_Interior=None
    OST_GbXML_SType_Shade=None
    OST_GbXML_SType_Underground=None
    OST_gbXML_SurfaceAir=None
    OST_gbXML_UndergroundCeiling=None
    OST_gbXML_UndergroundSlab=None
    OST_gbXML_UndergroundWall=None
    OST_GenericAnnotation=None
    OST_GenericLines=None
    OST_GenericModel=None
    OST_GenericModelHiddenLines=None
    OST_GenericModelTags=None
    OST_Girder=None
    OST_GraphicalWarning_OpenConnector=None
    OST_GridChains=None
    OST_GridHeads=None
    OST_Grids=None
    OST_GuideGrid=None
    OST_Gutter=None
    OST_HiddenFloorLines=None
    OST_HiddenLines=None
    OST_HiddenStructuralColumnLines=None
    OST_HiddenStructuralConnectionLines_Deprecated=None
    OST_HiddenStructuralFoundationLines=None
    OST_HiddenStructuralFramingLines=None
    OST_HiddenWallLines=None
    OST_HorizontalBracing=None
    OST_HostFin=None
    OST_HostFinCeiling=None
    OST_HostFinFloor=None
    OST_HostFinHF=None
    OST_HostFinRoof=None
    OST_HostFinTags=None
    OST_HostFinWall=None
    OST_HostTemplate=None
    OST_HVAC_Load_Building_Types=None
    OST_HVAC_Load_Schedules=None
    OST_HVAC_Load_Space_Types=None
    OST_HVAC_Zones=None
    OST_HVAC_Zones_Boundary=None
    OST_HVAC_Zones_ColorFill=None
    OST_HVAC_Zones_InteriorFill=None
    OST_HVAC_Zones_InteriorFill_Visibility=None
    OST_HVAC_Zones_Reference=None
    OST_HVAC_Zones_Reference_Visibility=None
    OST_ImportObjectStyles=None
    OST_InstanceDrivenLineStyle=None
    OST_InsulationLines=None
    OST_InternalAreaLoads=None
    OST_InternalAreaLoadTags=None
    OST_InternalLineLoads=None
    OST_InternalLineLoadTags=None
    OST_InternalLoads=None
    OST_InternalPointLoads=None
    OST_InternalPointLoadTags=None
    OST_InvisibleLines=None
    OST_IOS=None
    OST_IOSAligningLine=None
    OST_IOSAlignmentGraphics=None
    OST_IOSArrays=None
    OST_IOSAttachedDetailGroups=None
    OST_IOSBackedUpElements=None
    OST_IOSBBoxScreenSize=None
    OST_IOSConstructionLine=None
    OST_IOSCrashGraphics=None
    OST_IOSCuttingGeometry=None
    OST_IOSDatumPlane=None
    OST_IOSDetailGroups=None
    OST_IOSDragBox=None
    OST_IOSDragBoxInverted=None
    OST_IOSFabricReinSpanSymbolCtrl=None
    OST_IOSFlipControl=None
    OST_IOSFreeSnapLine=None
    OST_IOSGhost=None
    OST_IOSGroups=None
    OST_IOSMeasureLine=None
    OST_IOSMeasureLineScreenSize=None
    OST_IOSModelGroups=None
    OST_IOSNavWheelPivotBall=None
    OST_IOSNotSilhouette=None
    OST_IOSOpening=None
    OST_IOSRebarSystemSpanSymbolCtrl=None
    OST_IOSRegeneratedElements=None
    OST_IOSRegenerationFailure=None
    OST_IOSRoomCalculationPoint=None
    OST_IOSRoomComputationHeight=None
    OST_IOSRoomPerimeterLines=None
    OST_IOSRoomTagToRoomLines=None
    OST_IOSRoomUpperLowerLines=None
    OST_IOSSketchGrid=None
    OST_IOSSlabShapeEditorAutoCrease=None
    OST_IOSSlabShapeEditorBoundary=None
    OST_IOSSlabShapeEditorExplitCrease=None
    OST_IOSSlabShapeEditorPointBoundary=None
    OST_IOSSlabShapeEditorPointInterior=None
    OST_IOSSuspendedSketch=None
    OST_IOSSuspendedSketch_obsolete=None
    OST_IOSThinPixel=None
    OST_IOSThinPixel_Dash=None
    OST_IOSThinPixel_DashDot=None
    OST_IOSThinPixel_Dot=None
    OST_IOSTilePatternGrid=None
    OST_IOSWallCoreBoundary=None
    OST_IOS_GeoLocations=None
    OST_IOS_GeoSite=None
    OST_IsolatedFoundationAnalytical=None
    OST_IsolatedFoundationAnalyticalTags=None
    OST_Joist=None
    OST_KeynoteTags=None
    OST_KickerBracing=None
    OST_LayoutNodes=None
    OST_LayoutPathBase_Pipings=None
    OST_LayoutPath_Bases=None
    OST_LegendComponents=None
    OST_LevelHeads=None
    OST_Levels=None
    OST_LightingDevices=None
    OST_LightingDeviceTags=None
    OST_LightingFixtures=None
    OST_LightingFixturesHiddenLines=None
    OST_LightingFixtureSource=None
    OST_LightingFixtureTags=None
    OST_LightLine=None
    OST_Lights=None
    OST_LineLoads=None
    OST_LineLoadTags=None
    OST_Lines=None
    OST_LinesBeyond=None
    OST_LinesHiddenLines=None
    OST_LinkAnalyticalTags=None
    OST_LinksAnalytical=None
    OST_LoadCases=None
    OST_LoadCasesAccidental=None
    OST_LoadCasesDead=None
    OST_LoadCasesLive=None
    OST_LoadCasesRoofLive=None
    OST_LoadCasesSeismic=None
    OST_LoadCasesSnow=None
    OST_LoadCasesTemperature=None
    OST_LoadCasesWind=None
    OST_Loads=None
    OST_MaskingRegion=None
    OST_Mass=None
    OST_MassAreaFaceTags=None
    OST_MassCutter=None
    OST_MassExteriorWall=None
    OST_MassExteriorWallUnderground=None
    OST_MassFaceSplitter=None
    OST_MassFloor=None
    OST_MassFloorsAll=None
    OST_MassFloor_Obsolete_IdInWrongRange=None
    OST_MassForm=None
    OST_MassGlazing=None
    OST_MassGlazingAll=None
    OST_MassHiddenLines=None
    OST_Massing=None
    OST_MassingCutOutlines=None
    OST_MassingProjectionOutlines=None
    OST_MassInteriorWall=None
    OST_MassOpening=None
    OST_MassRoof=None
    OST_MassShade=None
    OST_MassSkylights=None
    OST_MassSlab=None
    OST_MassSurface_Obsolete_IdInWrongRange=None
    OST_MassTags=None
    OST_MassTags_Obsolete_IdInWrongRange=None
    OST_MassWallsAll=None
    OST_MassZone=None
    OST_Mass_Obsolete_IdInWrongRange=None
    OST_MatchAll=None
    OST_MatchAnnotation=None
    OST_MatchDetail=None
    OST_Matchline=None
    OST_MatchModel=None
    OST_MatchProfile=None
    OST_MatchSiteComponent=None
    OST_Materials=None
    OST_MaterialTags=None
    OST_MechanicalEquipment=None
    OST_MechanicalEquipmentHiddenLines=None
    OST_MechanicalEquipmentTags=None
    OST_MEPSpaceColorFill=None
    OST_MEPSpaceInteriorFill=None
    OST_MEPSpaceInteriorFillVisibility=None
    OST_MEPSpaceReference=None
    OST_MEPSpaceReferenceVisibility=None
    OST_MEPSpaces=None
    OST_MEPSpaceSeparationLines=None
    OST_MEPSpaceTags=None
    OST_ModelText=None
    OST_MultiCategoryTags=None
    OST_MultiReferenceAnnotations=None
    OST_MultistoryStairs=None
    OST_MultiSurface=None
    OST_NodeAnalyticalTags=None
    OST_NumberingSchemas=None
    OST_NurseCallDevices=None
    OST_NurseCallDeviceTags=None
    OST_OBSOLETE_ElemArrayHiddenLines=None
    OST_OBSOLETE_FabricationPartsTmpGraphicDrop=None
    OST_OBSOLETE_FabricationPartsTmpGraphicDropDrag=None
    OST_OverheadLines=None
    OST_PanelScheduleGraphics=None
    OST_ParamElemElectricalLoadClassification=None
    OST_Parking=None
    OST_ParkingHiddenLines=None
    OST_ParkingTags=None
    OST_PartHiddenLines=None
    OST_Parts=None
    OST_PartTags=None
    OST_PathRein=None
    OST_PathReinBoundary=None
    OST_PathReinSpanSymbol=None
    OST_PathReinTags=None
    OST_Phases=None
    OST_PipeAccessory=None
    OST_PipeAccessoryTags=None
    OST_PipeColorFillLegends=None
    OST_PipeColorFills=None
    OST_PipeConnections=None
    OST_PipeCurves=None
    OST_PipeCurvesCenterLine=None
    OST_PipeCurvesContour=None
    OST_PipeCurvesDrop=None
    OST_PipeCurvesInsulation=None
    OST_PipeCurvesRiseDrop=None
    OST_PipeFitting=None
    OST_PipeFittingCenterLine=None
    OST_PipeFittingInsulation=None
    OST_PipeFittingTags=None
    OST_PipeInsulations=None
    OST_PipeInsulationsTags=None
    OST_PipeMaterials=None
    OST_PipeSchedules=None
    OST_PipeSegments=None
    OST_PipeTags=None
    OST_PipingSystem=None
    OST_PipingSystem_Reference=None
    OST_PipingSystem_Reference_Visibility=None
    OST_PlaceHolderDucts=None
    OST_PlaceHolderPipes=None
    OST_PlanRegion=None
    OST_Planting=None
    OST_PlantingHiddenLines=None
    OST_PlantingTags=None
    OST_PlumbingFixtures=None
    OST_PlumbingFixturesHiddenLines=None
    OST_PlumbingFixtureTags=None
    OST_PointClouds=None
    OST_PointLoads=None
    OST_PointLoadTags=None
    OST_PreviewLegendComponents=None
    OST_ProfileFamilies=None
    OST_ProjectBasePoint=None
    OST_ProjectInformation=None
    OST_Property=None
    OST_PropertySet=None
    OST_Purlin=None
    OST_RailingBalusterRail=None
    OST_RailingBalusterRailCut=None
    OST_RailingHandRail=None
    OST_RailingHandRailAboveCut=None
    OST_RailingRailPathExtensionLines=None
    OST_RailingRailPathLines=None
    OST_Railings=None
    OST_RailingSupport=None
    OST_RailingSystem=None
    OST_RailingSystemBaluster=None
    OST_RailingSystemBalusterHiddenLines_Deprecated=None
    OST_RailingSystemHandRail=None
    OST_RailingSystemHandRailBracket=None
    OST_RailingSystemHandRailBracketHiddenLines_Deprecated=None
    OST_RailingSystemHandRailHiddenLines_Deprecated=None
    OST_RailingSystemHardware=None
    OST_RailingSystemHiddenLines_Deprecated=None
    OST_RailingSystemPanel=None
    OST_RailingSystemPanelBracketHiddenLines_Deprecated=None
    OST_RailingSystemPanelHiddenLines_Deprecated=None
    OST_RailingSystemPost=None
    OST_RailingSystemPostHiddenLines_Deprecated=None
    OST_RailingSystemRail=None
    OST_RailingSystemRailHiddenLines_Deprecated=None
    OST_RailingSystemSegment=None
    OST_RailingSystemSegmentHiddenLines_Deprecated=None
    OST_RailingSystemTags=None
    OST_RailingSystemTermination=None
    OST_RailingSystemTerminationHiddenLines_Deprecated=None
    OST_RailingSystemTopRail=None
    OST_RailingSystemTopRailHiddenLines_Deprecated=None
    OST_RailingSystemTransition=None
    OST_RailingSystemTransitionHiddenLines_Deprecated=None
    OST_RailingTermination=None
    OST_RailingTopRail=None
    OST_RailingTopRailAboveCut=None
    OST_Ramps=None
    OST_RampsAboveCut=None
    OST_RampsDownArrow=None
    OST_RampsDownText=None
    OST_RampsHiddenLines=None
    OST_RampsIncomplete=None
    OST_RampsStringer=None
    OST_RampsStringerAboveCut=None
    OST_RampsUpArrow=None
    OST_RampsUpText=None
    OST_RasterImages=None
    OST_Rebar=None
    OST_RebarCover=None
    OST_RebarHiddenLines=None
    OST_RebarLines=None
    OST_RebarSetToggle=None
    OST_RebarShape=None
    OST_RebarSketchLines=None
    OST_RebarTags=None
    OST_ReferenceLines=None
    OST_ReferencePoints=None
    OST_ReferencePoints_HiddenLines=None
    OST_ReferencePoints_Lines=None
    OST_ReferencePoints_Planes=None
    OST_ReferencePoints_Points=None
    OST_ReferenceViewer=None
    OST_ReferenceViewerSymbol=None
    OST_RemovedGridSeg=None
    OST_RemovedGridSeg_Obsolete_IdInWrongRange=None
    OST_RenderRegions=None
    OST_RepeatingDetailLines=None
    OST_Reveals=None
    OST_RevisionClouds=None
    OST_RevisionCloudTags=None
    OST_Revisions=None
    OST_RigidLinksAnalytical=None
    OST_Roads=None
    OST_RoadsHiddenLines=None
    OST_RoofOpening=None
    OST_Roofs=None
    OST_RoofsCut=None
    OST_RoofsCutPattern=None
    OST_RoofsDefault=None
    OST_RoofsFinish1=None
    OST_RoofsFinish2=None
    OST_RoofsHiddenLines=None
    OST_RoofsInsulation=None
    OST_RoofsInteriorEdges=None
    OST_RoofsMembrane=None
    OST_RoofSoffit=None
    OST_RoofsProjection=None
    OST_RoofsStructure=None
    OST_RoofsSubstrate=None
    OST_RoofsSurfacePattern=None
    OST_RoofTags=None
    OST_RoomColorFill=None
    OST_RoomInteriorFill=None
    OST_RoomInteriorFillVisibility=None
    OST_RoomPolylines=None
    OST_RoomReference=None
    OST_RoomReferenceVisibility=None
    OST_Rooms=None
    OST_RoomSeparationLines=None
    OST_RoomTags=None
    OST_RouteCurve=None
    OST_RouteCurveBranch=None
    OST_RouteCurveMain=None
    OST_RoutingPreferences=None
    OST_RvtLinks=None
    OST_ScheduleGraphics=None
    OST_ScheduleViewParamGroup=None
    OST_SecondaryTopographyContours=None
    OST_SectionBox=None
    OST_SectionHeadMediumLines=None
    OST_SectionHeads=None
    OST_SectionHeadThinLines=None
    OST_SectionHeadWideLines=None
    OST_SectionLine=None
    OST_Sections=None
    OST_SecurityDevices=None
    OST_SecurityDeviceTags=None
    OST_Sewer=None
    OST_ShaftOpening=None
    OST_ShaftOpeningHiddenLines=None
    OST_SharedBasePoint=None
    OST_Sheets=None
    OST_Site=None
    OST_SiteHiddenLines=None
    OST_SitePoint=None
    OST_SitePointBoundary=None
    OST_SiteProperty=None
    OST_SitePropertyLineSegment=None
    OST_SitePropertyLineSegmentTags=None
    OST_SitePropertyTags=None
    OST_SiteRegion=None
    OST_SiteSurface=None
    OST_SiteTags=None
    OST_SketchLines=None
    OST_SpanDirectionSymbol=None
    OST_SpecialityEquipment=None
    OST_SpecialityEquipmentHiddenLines=None
    OST_SpecialityEquipmentTags=None
    OST_SplitterProfile=None
    OST_SpotCoordinates=None
    OST_SpotCoordinateSymbols=None
    OST_SpotElevations=None
    OST_SpotElevSymbols=None
    OST_SpotSlopes=None
    OST_SpotSlopesSymbols=None
    OST_Sprinklers=None
    OST_SprinklerTags=None
    OST_StackedWalls=None
    OST_StackedWalls_Obsolete_IdInWrongRange=None
    OST_Stair2012_Deprecated=None
    OST_StairLanding2012HiddenLines_Deprecated=None
    OST_StairRun2012HiddenLines_Deprecated=None
    OST_Stairs=None
    OST_Stairs2012HiddenLines_Deprecated=None
    OST_StairsAboveCut_ToBeDeprecated=None
    OST_StairsCutMarks=None
    OST_StairsCutMarksAboveCut=None
    OST_StairsDownArrows=None
    OST_StairsDownText=None
    OST_StairsHiddenLines=None
    OST_StairsIncomplete_Deprecated=None
    OST_StairsLandings=None
    OST_StairsLandingTags=None
    OST_StairsNosingLines=None
    OST_StairsNosingLinesAboveCut=None
    OST_StairsOutlines=None
    OST_StairsOutlinesAboveCut=None
    OST_StairsPaths=None
    OST_StairsPathsAboveCut=None
    OST_StairsRailing=None
    OST_StairsRailingAboveCut=None
    OST_StairsRailingBaluster=None
    OST_StairsRailingHiddenLines=None
    OST_StairsRailingRail=None
    OST_StairsRailingTags=None
    OST_StairsRiserLines=None
    OST_StairsRiserLinesAboveCut=None
    OST_StairsRuns=None
    OST_StairsRunTags=None
    OST_StairsSketchBoundaryLines=None
    OST_StairsSketchLandingCenterLines=None
    OST_StairsSketchPathLines=None
    OST_StairsSketchRiserLines=None
    OST_StairsSketchRunLines=None
    OST_StairsStringerCarriage=None
    OST_StairsSupports=None
    OST_StairsSupportsAboveCut=None
    OST_StairsSupportTags=None
    OST_StairsTags=None
    OST_StairStringer2012HiddenLines_Deprecated=None
    OST_StairStringer2012_Deprecated=None
    OST_StairsTriserNumbers=None
    OST_StairsTrisers=None
    OST_StairsTriserTags=None
    OST_StairsUpArrows=None
    OST_StairsUpText=None
    OST_StairTread2012HiddenLines_Deprecated=None
    OST_StickSymbols_Obsolete_IdInWrongRange=None
    OST_StructConnectionAnchors=None
    OST_StructConnectionBolts=None
    OST_StructConnectionFailed=None
    OST_StructConnectionHiddenLines=None
    OST_StructConnectionOthers=None
    OST_StructConnectionPlates=None
    OST_StructConnectionProfiles=None
    OST_StructConnectionReference=None
    OST_StructConnections=None
    OST_StructConnectionStale=None
    OST_StructConnectionSymbol=None
    OST_StructConnectionSymbols=None
    OST_StructConnectionTags=None
    OST_StructLocationLineControl=None
    OST_StructuralAnnotations=None
    OST_StructuralBracePlanReps=None
    OST_StructuralColumnLocationLine=None
    OST_StructuralColumns=None
    OST_StructuralColumnStickSymbols=None
    OST_StructuralColumnTags=None
    OST_StructuralConnectionHandlerTags_Deprecated=None
    OST_StructuralConnectionHandler_Deprecated=None
    OST_StructuralFoundation=None
    OST_StructuralFoundationTags=None
    OST_StructuralFraming=None
    OST_StructuralFramingLocationLine=None
    OST_StructuralFramingOpening=None
    OST_StructuralFramingOther=None
    OST_StructuralFramingSystem=None
    OST_StructuralFramingSystemHiddenLines_Obsolete=None
    OST_StructuralFramingTags=None
    OST_StructuralStiffener=None
    OST_StructuralStiffenerHiddenLines=None
    OST_StructuralStiffenerTags=None
    OST_StructuralTruss=None
    OST_StructuralTrussHiddenLines=None
    OST_StructuralTrussStickSymbols=None
    OST_StructWeldLines=None
    OST_Sun=None
    OST_SunPath1=None
    OST_SunPath2=None
    OST_SunriseText=None
    OST_SunsetText=None
    OST_SunStudy=None
    OST_SunSurface=None
    OST_SWallRectOpening=None
    OST_SwitchboardScheduleTemplates=None
    OST_SwitchSystem=None
    OST_Tags=None
    OST_TelephoneDevices=None
    OST_TelephoneDeviceTags=None
    OST_TextNotes=None
    OST_TilePatterns=None
    OST_TitleBlockMediumLines=None
    OST_TitleBlocks=None
    OST_TitleBlockThinLines=None
    OST_TitleBlockWideLines=None
    OST_Topography=None
    OST_TopographyContours=None
    OST_TopographyHiddenLines=None
    OST_TopographySurface=None
    OST_Truss=None
    OST_TrussBottomChordCurve=None
    OST_TrussChord=None
    OST_TrussDiagWebCurve=None
    OST_TrussDummy=None
    OST_TrussTags=None
    OST_TrussTopChordCurve=None
    OST_TrussVertWebCurve=None
    OST_TrussWeb=None
    OST_VerticalBracing=None
    OST_Viewers=None
    OST_ViewportLabel=None
    OST_Viewports=None
    OST_Views=None
    OST_VolumeOfInterest=None
    OST_WallAnalytical=None
    OST_WallAnalyticalTags=None
    OST_WallFoundationAnalytical=None
    OST_WallFoundationAnalyticalTags=None
    OST_WallLocalCoordSys=None
    OST_WallRefPlanes=None
    OST_WallRefPlanes_Obsolete_IdInWrongRange=None
    OST_Walls=None
    OST_WallsAnalyticalGeometry=None
    OST_WallsCutOutlines=None
    OST_WallsCutPattern=None
    OST_WallsDefault=None
    OST_WallsFinish1=None
    OST_WallsFinish2=None
    OST_WallsInsulation=None
    OST_WallsMembrane=None
    OST_WallsProjectionOutlines=None
    OST_WallsStructure=None
    OST_WallsSubstrate=None
    OST_WallsSurfacePattern=None
    OST_WallTags=None
    OST_WeakDims=None
    OST_Windows=None
    OST_WindowsFrameMullionCut=None
    OST_WindowsFrameMullionProjection=None
    OST_WindowsGlassCut=None
    OST_WindowsGlassProjection=None
    OST_WindowsHiddenLines=None
    OST_WindowsOpeningCut=None
    OST_WindowsOpeningProjection=None
    OST_WindowsSillHeadCut=None
    OST_WindowsSillHeadProjection=None
    OST_WindowTags=None
    OST_Wire=None
    OST_WireHomeRunArrows=None
    OST_WireInsulations=None
    OST_WireMaterials=None
    OST_WireTags=None
    OST_WireTemperatureRatings=None
    OST_WireTickMarks=None
    OST_XRayConstrainedProfileEdge=None
    OST_XRayImplicitPathCurve=None
    OST_XRayPathCurve=None
    OST_XRayPathPoint=None
    OST_XRayProfileEdge=None
    OST_XRaySideEdge=None
    OST_ZoneSchemes=None
    OST_ZoneTags=None
    OST_ZoningEnvelope=None
    value__=None
class BuiltInFailures(object):
    AnalyticalModelFailures=None
    ArrayFailures=None
    AssemblyFailures=None
    AutoJoinFailures=None
    AutoRouteFailures=None
    BeamFailures=None
    BeamSystemFailures=None
    BendFailures=None
    BlendFailures=None
    ColorFillFailures=None
    ColumnFailures=None
    ColumnInsideWallFailures=None
    ComponentRepeaterFailures=None
    ComponentRepeaterSlotFailures=None
    ConnectorFailures=None
    ConstraintFailures=None
    ConversionFailures=None
    CopyMonitorFailures=None
    CopyPasteFailures=None
    CreationFailures=None
    CurtainGridFamilyFailures=None
    CurtainWallFailures=None
    CurveByPointFailures=None
    CurveFailures=None
    CutFailures=None
    CutterFailures=None
    CuttingFailures=None
    DatumPlaneFailures=None
    DebugTabBindingFailures=None
    DecalFailures=None
    DesignOptionFailures=None
    DetailFailures=None
    DimensionFailures=None
    DisplacementElementFailures=None
    DividedPathFailures=None
    DividedSurfaceFailures=None
    DocumentFailures=None
    DPartFailures=None
    DuctFailures=None
    EditingFailures=None
    ElectricalFailures=None
    ElectricityFailures=None
    ElementFailures=None
    ElementTypeFailures=None
    ElevationFailures=None
    EnergyAnalysisFailures=None
    EnergyAnalysisUtilitiesDBFailures=None
    ExportFailures=None
    ExtrusionFailures=None
    FabricAreaFailures=None
    FabricationShapeFailures=None
    FabricFailures=None
    FabricSheetFailures=None
    FaceSplitterFailures=None
    FamilyFailures=None
    FilledRegionFailures=None
    FloorFailures=None
    FluidFailures=None
    FormFailures=None
    GeneralFailures=None
    GenericFailures=None
    GenericMEPFailures=None
    GeometryFailures=None
    GlobalParameterFailures=None
    GridChainSketchFailures=None
    GridFailures=None
    GroupFailures=None
    HostObjFailures=None
    HvacFailures=None
    IlluminationFailures=None
    ImageFailures=None
    ImportExportFailures=None
    ImportFailures=None
    InaccurateFailures=None
    InfillFailures=None
    InterferenceFailures=None
    JoinElementsFailures=None
    KeyBasedTreeEntryFailures=None
    KeyBasedTreeFileFailures=None
    KeynoteFailures=None
    KeynoteTagFailures=None
    LegendFailures=None
    LevelFailures=None
    LinkFailures=None
    LoadFailures=None
    LooseDimensionFailures=None
    MassFailures=None
    MatchlineFailures=None
    MechanicalFailures=None
    MEPCalculationFailures=None
    MEPFabricationFailures=None
    MirrorFailures=None
    MultiReferenceAnnotationFailures=None
    NumberingFailures=None
    OffsetFacesCellLegacyFailures=None
    OpeningFailures=None
    OverlapFailures=None
    ParameterFailures=None
    PartMakerMethodForFamilyInstanceFailures=None
    PartMakerMethodForMergePartFailures=None
    PartMakerMethodForWallFailures=None
    PathFailures=None
    PerformanceFailures=None
    PipingFailures=None
    PlanRegionFailures=None
    PointFailures=None
    ProfileFailures=None
    PropertySetElementFailures=None
    RebarCouplerFailures=None
    RebarFailures=None
    RebarShapeFailures=None
    RebarSystemFailures=None
    RefPlaneFailures=None
    RegenFailures=None
    RenderFailures=None
    RevisionCloudFailures=None
    RevisionFailures=None
    RevolutionFailures=None
    RoofFailures=None
    RoomFailures=None
    ScheduleViewFailures=None
    SculptingFailures=None
    SectionViewFailures=None
    SelectionFailures=None
    SheetFailures=None
    SiteFailures=None
    SiteImportFailures=None
    SketchFailures=None
    SkylightFailures=None
    SlabFailures=None
    SlabShapeFailures=None
    SlantedColumnFailures=None
    SpanDirectionSymbolFailures=None
    SplineFailures=None
    StairRampFailures=None
    StructuralAssetFailures=None
    StructuralConnectionFailures=None
    StructuralLoadFailures=None
    SweepFailures=None
    SweptBlendFailures=None
    SystemNavigatorFailures=None
    SystemsFailures=None
    TagFailures=None
    TextFailures=None
    TilePatternTileFailures=None
    ToggleViewFailures=None
    TrussFailures=None
    UniqueElementFailures=None
    ViewFailures=None
    WallFailures=None
    WallJoinFailures=None
    WallJoinRoofFailures=None
    WorksharingFailures=None
    __all__=[
        'AnalyticalModelFailures',
        'ArrayFailures',
        'AssemblyFailures',
        'AutoJoinFailures',
        'AutoRouteFailures',
        'BeamFailures',
        'BeamSystemFailures',
        'BendFailures',
        'BlendFailures',
        'ColorFillFailures',
        'ColumnFailures',
        'ColumnInsideWallFailures',
        'ComponentRepeaterFailures',
        'ComponentRepeaterSlotFailures',
        'ConnectorFailures',
        'ConstraintFailures',
        'ConversionFailures',
        'CopyMonitorFailures',
        'CopyPasteFailures',
        'CreationFailures',
        'CurtainGridFamilyFailures',
        'CurtainWallFailures',
        'CurveByPointFailures',
        'CurveFailures',
        'CutFailures',
        'CutterFailures',
        'CuttingFailures',
        'DatumPlaneFailures',
        'DebugTabBindingFailures',
        'DecalFailures',
        'DesignOptionFailures',
        'DetailFailures',
        'DimensionFailures',
        'DisplacementElementFailures',
        'DividedPathFailures',
        'DividedSurfaceFailures',
        'DocumentFailures',
        'DPartFailures',
        'DuctFailures',
        'EditingFailures',
        'ElectricalFailures',
        'ElectricityFailures',
        'ElementFailures',
        'ElementTypeFailures',
        'ElevationFailures',
        'EnergyAnalysisFailures',
        'EnergyAnalysisUtilitiesDBFailures',
        'ExportFailures',
        'ExtrusionFailures',
        'FabricAreaFailures',
        'FabricationShapeFailures',
        'FabricFailures',
        'FabricSheetFailures',
        'FaceSplitterFailures',
        'FamilyFailures',
        'FilledRegionFailures',
        'FloorFailures',
        'FluidFailures',
        'FormFailures',
        'GeneralFailures',
        'GenericFailures',
        'GenericMEPFailures',
        'GeometryFailures',
        'GlobalParameterFailures',
        'GridChainSketchFailures',
        'GridFailures',
        'GroupFailures',
        'HostObjFailures',
        'HvacFailures',
        'IlluminationFailures',
        'ImageFailures',
        'ImportExportFailures',
        'ImportFailures',
        'InaccurateFailures',
        'InfillFailures',
        'InterferenceFailures',
        'JoinElementsFailures',
        'KeyBasedTreeEntryFailures',
        'KeyBasedTreeFileFailures',
        'KeynoteFailures',
        'KeynoteTagFailures',
        'LegendFailures',
        'LevelFailures',
        'LinkFailures',
        'LoadFailures',
        'LooseDimensionFailures',
        'MassFailures',
        'MatchlineFailures',
        'MechanicalFailures',
        'MEPCalculationFailures',
        'MEPFabricationFailures',
        'MirrorFailures',
        'MultiReferenceAnnotationFailures',
        'NumberingFailures',
        'OffsetFacesCellLegacyFailures',
        'OpeningFailures',
        'OverlapFailures',
        'ParameterFailures',
        'PartMakerMethodForFamilyInstanceFailures',
        'PartMakerMethodForMergePartFailures',
        'PartMakerMethodForWallFailures',
        'PathFailures',
        'PerformanceFailures',
        'PipingFailures',
        'PlanRegionFailures',
        'PointFailures',
        'ProfileFailures',
        'PropertySetElementFailures',
        'RebarCouplerFailures',
        'RebarFailures',
        'RebarShapeFailures',
        'RebarSystemFailures',
        'RefPlaneFailures',
        'RegenFailures',
        'RenderFailures',
        'RevisionCloudFailures',
        'RevisionFailures',
        'RevolutionFailures',
        'RoofFailures',
        'RoomFailures',
        'ScheduleViewFailures',
        'SculptingFailures',
        'SectionViewFailures',
        'SelectionFailures',
        'SheetFailures',
        'SiteFailures',
        'SiteImportFailures',
        'SketchFailures',
        'SkylightFailures',
        'SlabFailures',
        'SlabShapeFailures',
        'SlantedColumnFailures',
        'SpanDirectionSymbolFailures',
        'SplineFailures',
        'StairRampFailures',
        'StructuralAssetFailures',
        'StructuralConnectionFailures',
        'StructuralLoadFailures',
        'SweepFailures',
        'SweptBlendFailures',
        'SystemNavigatorFailures',
        'SystemsFailures',
        'TagFailures',
        'TextFailures',
        'TilePatternTileFailures',
        'ToggleViewFailures',
        'TrussFailures',
        'UniqueElementFailures',
        'ViewFailures',
        'WallFailures',
        'WallJoinFailures',
        'WallJoinRoofFailures',
        'WorksharingFailures',
    ]
class BuiltInParameter(Enum):
    ACTUAL_MAX_RIDGE_HEIGHT_PARAM=None
    ALLOW_AUTO_EMBED=None
    ALL_GRID_ROTATION_FOR_DIVISION_RULE=None
    ALL_MODEL_COST=None
    ALL_MODEL_DESCRIPTION=None
    ALL_MODEL_FAMILY_NAME=None
    ALL_MODEL_IMAGE=None
    ALL_MODEL_INSTANCE_COMMENTS=None
    ALL_MODEL_MANUFACTURER=None
    ALL_MODEL_MARK=None
    ALL_MODEL_MODEL=None
    ALL_MODEL_TYPE_COMMENTS=None
    ALL_MODEL_TYPE_IMAGE=None
    ALL_MODEL_TYPE_MARK=None
    ALL_MODEL_TYPE_NAME=None
    ALL_MODEL_URL=None
    ALTERNATE_UNITS=None
    ALTERNATE_UNITS_PREFIX=None
    ALTERNATE_UNITS_SUFFIX=None
    ALWAYS_ZERO_LENGTH=None
    ANALYTICAL_ABSORPTANCE=None
    ANALYTICAL_GEOMETRY_IS_VALID=None
    ANALYTICAL_HEAT_TRANSFER_COEFFICIENT=None
    ANALYTICAL_LINK_RELEASE_ROTATION_X=None
    ANALYTICAL_LINK_RELEASE_ROTATION_Y=None
    ANALYTICAL_LINK_RELEASE_ROTATION_Z=None
    ANALYTICAL_LINK_RELEASE_TRANSLATION_X=None
    ANALYTICAL_LINK_RELEASE_TRANSLATION_Y=None
    ANALYTICAL_LINK_RELEASE_TRANSLATION_Z=None
    ANALYTICAL_MEMBER_FORCE_END_ALL_NON_ZERO=None
    ANALYTICAL_MEMBER_FORCE_END_FX=None
    ANALYTICAL_MEMBER_FORCE_END_FY=None
    ANALYTICAL_MEMBER_FORCE_END_FZ=None
    ANALYTICAL_MEMBER_FORCE_END_MX=None
    ANALYTICAL_MEMBER_FORCE_END_MY=None
    ANALYTICAL_MEMBER_FORCE_END_MZ=None
    ANALYTICAL_MEMBER_FORCE_START_ALL_NON_ZERO=None
    ANALYTICAL_MEMBER_FORCE_START_FX=None
    ANALYTICAL_MEMBER_FORCE_START_FY=None
    ANALYTICAL_MEMBER_FORCE_START_FZ=None
    ANALYTICAL_MEMBER_FORCE_START_MX=None
    ANALYTICAL_MEMBER_FORCE_START_MY=None
    ANALYTICAL_MEMBER_FORCE_START_MZ=None
    ANALYTICAL_MODEL_AREA=None
    ANALYTICAL_MODEL_BASE_ALIGNMENT_METHOD=None
    ANALYTICAL_MODEL_BASE_EXTENSION_METHOD=None
    ANALYTICAL_MODEL_BASE_Y_PROJECTION=None
    ANALYTICAL_MODEL_BASE_Z_PROJECTION=None
    ANALYTICAL_MODEL_CODE_CHECKING=None
    ANALYTICAL_MODEL_COLUMN_BASE_EXTENSION=None
    ANALYTICAL_MODEL_COLUMN_TOP_EXTENSION=None
    ANALYTICAL_MODEL_END_ALIGNMENT_METHOD=None
    ANALYTICAL_MODEL_END_Y_PROJECTION=None
    ANALYTICAL_MODEL_END_Z_PROJECTION=None
    ANALYTICAL_MODEL_FLOOR_ALIGNMENT_METHOD=None
    ANALYTICAL_MODEL_FLOOR_PROJECTION=None
    ANALYTICAL_MODEL_FOUNDATIONS_MARK=None
    ANALYTICAL_MODEL_LENGTH=None
    ANALYTICAL_MODEL_MANUALLY_ADJUSTED=None
    ANALYTICAL_MODEL_NODES_MARK=None
    ANALYTICAL_MODEL_PERIMETER=None
    ANALYTICAL_MODEL_PHYSICAL_TYPE=None
    ANALYTICAL_MODEL_ROTATION=None
    ANALYTICAL_MODEL_SKETCH_ALIGNMENT_METHOD=None
    ANALYTICAL_MODEL_SKETCH_PROJECTION=None
    ANALYTICAL_MODEL_START_ALIGNMENT_METHOD=None
    ANALYTICAL_MODEL_START_Y_PROJECTION=None
    ANALYTICAL_MODEL_START_Z_PROJECTION=None
    ANALYTICAL_MODEL_STICK_ELEMENTS_MARK=None
    ANALYTICAL_MODEL_SURFACE_ELEMENTS_MARK=None
    ANALYTICAL_MODEL_TOP_ALIGNMENT_METHOD=None
    ANALYTICAL_MODEL_TOP_EXTENSION_METHOD=None
    ANALYTICAL_MODEL_TOP_Y_PROJECTION=None
    ANALYTICAL_MODEL_TOP_Z_PROJECTION=None
    ANALYTICAL_MODEL_WALL_ALIGNMENT_METHOD=None
    ANALYTICAL_MODEL_WALL_BASE_PROJECTION=None
    ANALYTICAL_MODEL_WALL_PROJECTION=None
    ANALYTICAL_MODEL_WALL_TOP_PROJECTION=None
    ANALYTICAL_ROUGHNESS=None
    ANALYTICAL_SOLAR_HEAT_GAIN_COEFFICIENT=None
    ANALYTICAL_THERMAL_MASS=None
    ANALYTICAL_THERMAL_RESISTANCE=None
    ANALYTICAL_VISUAL_LIGHT_TRANSMITTANCE=None
    ANALYTIC_CONSTRUCTION_GBXML_TYPEID=None
    ANALYTIC_CONSTRUCTION_LOOKUP_TABLE=None
    ANY_PATTERN_ID_PARAM=None
    ANY_PATTERN_ID_PARAM_NO_NO=None
    ARC_CENTER_MARK=None
    ARC_CURVE_CNTR_MRK_VISIBLE=None
    ARC_LEADER_PARAM=None
    ARC_WALL_CNTR_MRK_VISIBLE=None
    AREA_SCHEME_ID=None
    AREA_SCHEME_NAME=None
    AREA_TYPE=None
    AREA_TYPE_TEXT=None
    ARROWHEAD_END_AT_RISER=None
    ARROWHEAD_TYPE=None
    ARROW_CLOSED=None
    ARROW_FILLED=None
    ARROW_SIZE=None
    ARROW_TYPE=None
    ASSEMBLY_NAME=None
    ASSEMBLY_NAMING_CATEGORY=None
    ASSIGN_TEMPLATE_ON_VIEW_CREATION=None
    AUTO_JOIN_CONDITION=None
    AUTO_JOIN_CONDITION_WALL=None
    AUTO_MULLION_BORDER1_GRID1=None
    AUTO_MULLION_BORDER1_GRID2=None
    AUTO_MULLION_BORDER1_HORIZ=None
    AUTO_MULLION_BORDER1_VERT=None
    AUTO_MULLION_BORDER2_GRID1=None
    AUTO_MULLION_BORDER2_GRID2=None
    AUTO_MULLION_BORDER2_HORIZ=None
    AUTO_MULLION_BORDER2_VERT=None
    AUTO_MULLION_INTERIOR_GRID1=None
    AUTO_MULLION_INTERIOR_GRID2=None
    AUTO_MULLION_INTERIOR_HORIZ=None
    AUTO_MULLION_INTERIOR_VERT=None
    AUTO_PANEL=None
    AUTO_PANEL_WALL=None
    BASELINE_DIM_OFFSET=None
    BASEPOINT_ANGLETON_PARAM=None
    BASEPOINT_EASTWEST_PARAM=None
    BASEPOINT_ELEVATION_PARAM=None
    BASEPOINT_NORTHSOUTH_PARAM=None
    BEAM_H_JUSTIFICATION=None
    BEAM_SYSTEM_3D_PARAM=None
    BEAM_SYSTEM_TAG_INST_PARAM_ANGLE=None
    BEAM_SYSTEM_TAG_PARAM_LEFT=None
    BEAM_SYSTEM_TAG_PARAM_RIGHT=None
    BEAM_V_JUSTIFICATION=None
    BEAM_V_JUSTIFICATION_OTHER_VALUE=None
    BENT_FABRIC_PARAM_BEND_DIRECTION=None
    BENT_FABRIC_PARAM_LONGITUDINAL_CUT_LENGTH=None
    BENT_FABRIC_PARAM_STRAIGHT_WIRES_LOCATION=None
    BLEND_END_PARAM=None
    BLEND_START_PARAM=None
    BOUNDARY_AREA_RESTRAINT_X=None
    BOUNDARY_AREA_RESTRAINT_Y=None
    BOUNDARY_AREA_RESTRAINT_Z=None
    BOUNDARY_BEARING=None
    BOUNDARY_CONDITIONS_IS_EXT=None
    BOUNDARY_CONDITIONS_TYPE=None
    BOUNDARY_DIRECTION_ROT_X=None
    BOUNDARY_DIRECTION_ROT_Y=None
    BOUNDARY_DIRECTION_ROT_Z=None
    BOUNDARY_DIRECTION_X=None
    BOUNDARY_DIRECTION_Y=None
    BOUNDARY_DIRECTION_Z=None
    BOUNDARY_DISTANCE=None
    BOUNDARY_LINEAR_RESTRAINT_ROT_X=None
    BOUNDARY_LINEAR_RESTRAINT_X=None
    BOUNDARY_LINEAR_RESTRAINT_Y=None
    BOUNDARY_LINEAR_RESTRAINT_Z=None
    BOUNDARY_PARAM_PRESET=None
    BOUNDARY_PARAM_PRESET_AREA=None
    BOUNDARY_PARAM_PRESET_LINEAR=None
    BOUNDARY_RADIUS=None
    BOUNDARY_RESTRAINT_ROT_X=None
    BOUNDARY_RESTRAINT_ROT_Y=None
    BOUNDARY_RESTRAINT_ROT_Z=None
    BOUNDARY_RESTRAINT_X=None
    BOUNDARY_RESTRAINT_Y=None
    BOUNDARY_RESTRAINT_Z=None
    BOUNDARY_X_ROTATION_FIXED=None
    BOUNDARY_X_ROTATION_SPRING=None
    BOUNDARY_X_TRANSLATION_FIXED=None
    BOUNDARY_X_TRANSLATION_SPRING=None
    BOUNDARY_Y_ROTATION_FIXED=None
    BOUNDARY_Y_ROTATION_SPRING=None
    BOUNDARY_Y_TRANSLATION_FIXED=None
    BOUNDARY_Y_TRANSLATION_SPRING=None
    BOUNDARY_Z_ROTATION_FIXED=None
    BOUNDARY_Z_ROTATION_SPRING=None
    BOUNDARY_Z_TRANSLATION_FIXED=None
    BOUNDARY_Z_TRANSLATION_SPRING=None
    BR_ORG_FILTER=None
    BR_ORG_FOLDERS=None
    BUILDINGPAD_HEIGHTABOVELEVEL_PARAM=None
    BUILDINGPAD_THICKNESS=None
    BUILDING_CLOSING_TIME_PARAM=None
    BUILDING_CURVE_GSTYLE=None
    BUILDING_CURVE_GSTYLE_PLUS_INVISIBLE=None
    BUILDING_OPENING_TIME_PARAM=None
    BUILDING_UNOCCUPIED_COOLING_SET_POINT_PARAM=None
    BUILIDING_PAD_STRUCTURE_ID_PARAM=None
    CABLETRAY_MINBENDMULTIPLIER_PARAM=None
    CALLOUT_ATTR_HEAD_TAG=None
    CALLOUT_CORNER_SHEET_RADIUS=None
    CALLOUT_SYNCRONIZE_BOUND_OFFSET_FAR=None
    CALLOUT_TAG=None
    CASEWORK_CONSTRUCTION_TYPE=None
    CASEWORK_DEPTH=None
    CASEWORK_FINISH=None
    CASEWORK_HEIGHT=None
    CASEWORK_WIDTH=None
    CEILING_ATTR_DEFAULT_HEIGHT_PARAM=None
    CEILING_ATTR_PATTERN_PARAM=None
    CEILING_ATTR_SPACING1_PARAM=None
    CEILING_ATTR_SPACING2_PARAM=None
    CEILING_ATTR_SYSTEMNAME_PARAM=None
    CEILING_HAS_THICKNESS_PARAM=None
    CEILING_HEIGHTABOVELEVEL_PARAM=None
    CEILING_STRUCTURE_ID_PARAM=None
    CEILING_THICKNESS=None
    CEILING_THICKNESS_PARAM=None
    CENTER_MARK_SIZE=None
    CIRCUIT_LOAD_CLASSIFICATION_PARAM=None
    CIRC_MULLION_RADIUS=None
    CLEAR_COVER=None
    CLEAR_COVER_BOTTOM=None
    CLEAR_COVER_EXTERIOR=None
    CLEAR_COVER_INTERIOR=None
    CLEAR_COVER_OTHER=None
    CLEAR_COVER_TOP=None
    CLIENT_NAME=None
    CLINE_SUBCATEGORY=None
    COARSE_SCALE_FILL_PATTERN_COLOR=None
    COARSE_SCALE_FILL_PATTERN_ID_PARAM=None
    COLOR_FILL_FILTERED_PARAM=None
    COLOR_FILL_SWATCH_HEIGHT_PARAM=None
    COLOR_FILL_SWATCH_WIDTH_PARAM=None
    COLOR_SCHEME_LOCATION=None
    COLUMN_BASE_ATTACHED_PARAM=None
    COLUMN_BASE_ATTACHMENT_OFFSET_PARAM=None
    COLUMN_BASE_ATTACH_CUT_PARAM=None
    COLUMN_BASE_ATTACH_JUSTIFICATION_PARAM=None
    COLUMN_LOCATION_MARK=None
    COLUMN_TOP_ATTACHED_PARAM=None
    COLUMN_TOP_ATTACHMENT_OFFSET_PARAM=None
    COLUMN_TOP_ATTACH_CUT_PARAM=None
    COLUMN_TOP_ATTACH_JUSTIFICATION_PARAM=None
    CONCEPTUAL_CONSTRUCTION_MATERIAL=None
    CONDUIT_STANDARD_TYPE_PARAM=None
    CONNECTOR_ANGLE=None
    CONNECTOR_ANGLE_OF_DEFLECTION=None
    CONNECTOR_DIAMETER=None
    CONNECTOR_ENGAGEMENT_LENGTH=None
    CONNECTOR_GENDER_TYPE=None
    CONNECTOR_HEIGHT=None
    CONNECTOR_INDEX=None
    CONNECTOR_INSIDE_DIAMETER=None
    CONNECTOR_JOINT_TYPE=None
    CONNECTOR_LENGTH=None
    CONNECTOR_PROFILE_TYPE=None
    CONNECTOR_RADIUS=None
    CONNECTOR_REFERENCE_INDEX=None
    CONNECTOR_UTILITY_PARAM=None
    CONNECTOR_VISIBLE_SIZE=None
    CONNECTOR_WIDTH=None
    CONSTRAINT_FIXED_OFFSET=None
    CONTINUOUSRAIL_BEGINNING_TERMINATION_ATTACHMENT_PARAM=None
    CONTINUOUSRAIL_BEGINNING_TERMINATION_TYPE_PARAM=None
    CONTINUOUSRAIL_DEFAULT_JOIN_TYPE_PARAM=None
    CONTINUOUSRAIL_END_EXTENSION_LENGTH_PARAM=None
    CONTINUOUSRAIL_END_TERMINATION_ATTACHMENT_PARAM=None
    CONTINUOUSRAIL_END_TERMINATION_TYPE_PARAM=None
    CONTINUOUSRAIL_EXTENSION_LENGTH_PARAM=None
    CONTINUOUSRAIL_FILLET_RADIUS_PARAM=None
    CONTINUOUSRAIL_JOIN_TYPE_PARAM=None
    CONTINUOUSRAIL_LENGTH_PARAM=None
    CONTINUOUSRAIL_MATERIALS_PARAM=None
    CONTINUOUSRAIL_PLUS_TREAD_DEPTH_PARAM=None
    CONTINUOUSRAIL_PROFILE_TYPE_PARAM=None
    CONTINUOUSRAIL_TRANSITION_TYPE_PARAM=None
    CONTINUOUS_FOOTING_BEARING_WIDTH=None
    CONTINUOUS_FOOTING_BOTTOM_HEEL=None
    CONTINUOUS_FOOTING_BOTTOM_TOE=None
    CONTINUOUS_FOOTING_BREAK_AT_INSERTS_DISABLE=None
    CONTINUOUS_FOOTING_DEFAULT_END_EXTENSION_LENGTH=None
    CONTINUOUS_FOOTING_ECCENTRICITY=None
    CONTINUOUS_FOOTING_LENGTH=None
    CONTINUOUS_FOOTING_STRUCTURAL_USAGE=None
    CONTINUOUS_FOOTING_TOP_HEEL=None
    CONTINUOUS_FOOTING_TOP_TOE=None
    CONTINUOUS_FOOTING_WIDTH=None
    CONTOUR_ELEVATION=None
    CONTOUR_ELEVATION_STEP=None
    CONTOUR_LABELS_ELEV_BASE_TYPE=None
    CONTOUR_LABELS_LINEAR_UNITS=None
    CONTOUR_LABELS_PRIMARY_ONLY=None
    CONTOUR_LABELS_RELATIVE_BASE=None
    CONTOUR_SUBCATEGORY_ID=None
    COUPLER_CODE=None
    COUPLER_COUPLED_BAR_SIZE=None
    COUPLER_COUPLED_ENDTREATMENT=None
    COUPLER_COUPLED_ENGAGEMENT=None
    COUPLER_LENGTH=None
    COUPLER_MAIN_BAR_SIZE=None
    COUPLER_MAIN_ENDTREATMENT=None
    COUPLER_MAIN_ENGAGEMENT=None
    COUPLER_MARK=None
    COUPLER_NUMBER=None
    COUPLER_QUANTITY=None
    COUPLER_WEIGHT=None
    COUPLER_WIDTH=None
    COVER_TYPE_LENGTH=None
    COVER_TYPE_NAME=None
    CURTAINGRID_ADJUST_BORDER_1=None
    CURTAINGRID_ADJUST_BORDER_2=None
    CURTAINGRID_ADJUST_BORDER_HORIZ=None
    CURTAINGRID_ADJUST_BORDER_U=None
    CURTAINGRID_ADJUST_BORDER_V=None
    CURTAINGRID_ADJUST_BORDER_VERT=None
    CURTAINGRID_ANGLE_1=None
    CURTAINGRID_ANGLE_2=None
    CURTAINGRID_ANGLE_HORIZ=None
    CURTAINGRID_ANGLE_U=None
    CURTAINGRID_ANGLE_V=None
    CURTAINGRID_ANGLE_VERT=None
    CURTAINGRID_BELT_1=None
    CURTAINGRID_BELT_2=None
    CURTAINGRID_BELT_HORIZ=None
    CURTAINGRID_BELT_RATIO_1=None
    CURTAINGRID_BELT_RATIO_2=None
    CURTAINGRID_BELT_RATIO_U=None
    CURTAINGRID_BELT_RATIO_V=None
    CURTAINGRID_BELT_U=None
    CURTAINGRID_BELT_V=None
    CURTAINGRID_BELT_VERT=None
    CURTAINGRID_ORIGIN_1=None
    CURTAINGRID_ORIGIN_2=None
    CURTAINGRID_ORIGIN_HORIZ=None
    CURTAINGRID_ORIGIN_U=None
    CURTAINGRID_ORIGIN_V=None
    CURTAINGRID_ORIGIN_VERT=None
    CURTAINGRID_USE_CURVE_DIST=None
    CURTAINGRID_USE_CURVE_DIST_1=None
    CURTAINGRID_USE_CURVE_DIST_2=None
    CURTAINGRID_USE_CURVE_DIST_HORIZ=None
    CURTAINGRID_USE_CURVE_DIST_U=None
    CURTAINGRID_USE_CURVE_DIST_V=None
    CURTAINGRID_USE_CURVE_DIST_VERT=None
    CURTAIN_GRID_BASE_ORIENTATION=None
    CURTAIN_VERSION_PARAM=None
    CURTAIN_WALL_PANELS_CONSTRUCTION_TYPE=None
    CURTAIN_WALL_PANELS_FINISH=None
    CURTAIN_WALL_PANELS_HEIGHT=None
    CURTAIN_WALL_PANELS_WIDTH=None
    CURTAIN_WALL_PANEL_HOST_ID=None
    CURTAIN_WALL_SYSPANEL_OFFSET=None
    CURTAIN_WALL_SYSPANEL_THICKNESS=None
    CURVE_BY_POINTS_PROJECTION_TYPE=None
    CURVE_DETERMINES_ORIENTATION=None
    CURVE_EDGE_OFFSET=None
    CURVE_ELEM_ARC_END_ANGLE=None
    CURVE_ELEM_ARC_RADIUS=None
    CURVE_ELEM_ARC_RANGE=None
    CURVE_ELEM_ARC_START_ANGLE=None
    CURVE_ELEM_DEFINES_SLOPE=None
    CURVE_ELEM_LENGTH=None
    CURVE_ELEM_LINE_ANGLE=None
    CURVE_HEIGHT_OFFSET=None
    CURVE_IS_DETAIL=None
    CURVE_IS_FILLED=None
    CURVE_IS_REFERENCE_LINE=None
    CURVE_IS_SLOPE_DEFINING=None
    CURVE_LEVEL=None
    CURVE_NUMBER_OF_SEGMENTS=None
    CURVE_PARAM_CONCRETE_CANTILEVER=None
    CURVE_PARAM_STEEL_CANTILEVER=None
    CURVE_SUPPORT_OFFSET=None
    CURVE_VISIBILITY_PARAM=None
    CURVE_WALL_OFFSET=None
    CURVE_WALL_OFFSET_ROOFS=None
    CUST_MULLION_THICK=None
    CUST_MULLION_WIDTH1=None
    CUST_MULLION_WIDTH2=None
    CUT_LINE_ANGLE=None
    CUT_LINE_DISTANCE=None
    CUT_LINE_EXTENSION=None
    CUT_LINE_TYPE=None
    CUT_MARK_SYMBOL=None
    CUT_MARK_SYMBOL_SIZE=None
    CWP_ADD_GRID_PREFIX=None
    CWP_ADD_GRID_SUFFIX=None
    CWP_ADD_LEVEL_PREFIX=None
    CWP_ADD_LEVEL_SUFFIX=None
    CWP_COPY_FLOOR_INSERTS=None
    CWP_COPY_ROOF_INSERTS=None
    CWP_COPY_WALL_INSERTS=None
    CWP_LEVEL_OFFSET=None
    CWP_LINKED_ROOM_PARAMS=None
    CWP_LINKED_ROOM_PHASES=None
    CWP_REUSE_EXISTING_GRIDS=None
    CWP_REUSE_EXISTING_LEVELS=None
    CWP_REUSE_GRIDS_SAME_NAME=None
    CWP_REUSE_LEVELS_SAME_NAME=None
    CWP_SPLIT_COLUMNS_AT_LEVELS=None
    DATUM_BUBBLE_END_1=None
    DATUM_BUBBLE_END_2=None
    DATUM_BUBBLE_LOCATION_IN_ELEV=None
    DATUM_PLANE_DEFINES_ORIGIN=None
    DATUM_PLANE_DEFINES_WALL_CLOSURE=None
    DATUM_TEXT=None
    DATUM_VOLUME_OF_INTEREST=None
    DEBUGTAB_DATABOUNDCONTROLSDEMO_BOOLEAN=None
    DEBUGTAB_DATABOUNDCONTROLSDEMO_DOUBLE=None
    DEBUGTAB_DATABOUNDCONTROLSDEMO_ENUM=None
    DEBUGTAB_DATABOUNDCONTROLSDEMO_INTEGER=None
    DECAL_ATTRIBUTES=None
    DECAL_HEIGHT=None
    DECAL_LOCK_PROPORTIONS=None
    DECAL_SUBCATEGORY_ID=None
    DECAL_WIDTH=None
    DEFAULT_CONSTRUCTION_EXT_WALL_UNDERGROUND=None
    DEFAULT_CONSTRUCTION_MASS_EXTERIOR_WALL=None
    DEFAULT_CONSTRUCTION_MASS_FLOOR=None
    DEFAULT_CONSTRUCTION_MASS_GLAZING=None
    DEFAULT_CONSTRUCTION_MASS_INTERIOR_WALL=None
    DEFAULT_CONSTRUCTION_MASS_OPENING=None
    DEFAULT_CONSTRUCTION_MASS_ROOF=None
    DEFAULT_CONSTRUCTION_MASS_SHADE=None
    DEFAULT_CONSTRUCTION_MASS_SKYLIGHT=None
    DEFAULT_CONSTRUCTION_MASS_SLAB=None
    DEFAULT_VIEW_TEMPLATE=None
    DEFINES_CONSTANT_HEIGHT=None
    DESIGN_OPTION_ID=None
    DESIGN_OPTION_PARAM=None
    DIAMETER_SYMBOL_LOCATION=None
    DIAMETER_SYMBOL_TEXT=None
    DIM_DISPLAY_EQ=None
    DIM_ISREPORTING=None
    DIM_LABEL=None
    DIM_LABEL_GP_SHOW=None
    DIM_LABEL_IS_INSTANCE=None
    DIM_LEADER=None
    DIM_LEADER_ARROWHEAD=None
    DIM_LEADER_DISPLAY_CONDITION=None
    DIM_LEADER_SHOULDER_LENGTH=None
    DIM_LEADER_TYPE=None
    DIM_LINE_EXTENSION=None
    DIM_NOT_MODIFIABLE=None
    DIM_REFERENCE_COUNT=None
    DIM_STYLE_ANGULAR_UNITS=None
    DIM_STYLE_ANGULAR_UNITS_ALT=None
    DIM_STYLE_CENTERLINE_PATTERN=None
    DIM_STYLE_CENTERLINE_SYMBOL=None
    DIM_STYLE_CENTERLINE_TICK_MARK=None
    DIM_STYLE_DIM_LINE_SNAP_DIST=None
    DIM_STYLE_FLIPPED_DIM_LINE_EXTENSION=None
    DIM_STYLE_INTERIOR_TICK_MARK=None
    DIM_STYLE_LEADER_TICK_MARK=None
    DIM_STYLE_LINEAR_UNITS=None
    DIM_STYLE_LINEAR_UNITS_ALT=None
    DIM_STYLE_READ_CONVENTION=None
    DIM_STYLE_SHOW_OPENING_HT=None
    DIM_STYLE_SUPPRESS_SPACES=None
    DIM_TEXT_BACKGROUND=None
    DIM_TEXT_LOCATION_FOR_LEADER=None
    DIM_TOTAL_LENGTH=None
    DIM_TO_INSERTS=None
    DIM_TO_INSERT_TYPE=None
    DIM_TO_INTERSECTING_GRIDS=None
    DIM_TO_INTERSECTING_WALLS=None
    DIM_VALUE_ANGLE=None
    DIM_VALUE_LENGTH=None
    DIM_WITNS_LINE_CNTRL=None
    DIM_WITNS_LINE_EXTENSION_BELOW=None
    DISPLACED_ELEMENT_DISPLACEMENT_X=None
    DISPLACED_ELEMENT_DISPLACEMENT_Y=None
    DISPLACED_ELEMENT_DISPLACEMENT_Z=None
    DISPLACEMENT_PATH_DEPTH=None
    DISPLACEMENT_PATH_STYLE=None
    DISTANCE_TO_CUT_MARK=None
    DIVIDEDPATH_BEGINNING_INDENT=None
    DIVIDEDPATH_DISPLAY_NODES=None
    DIVIDEDPATH_DISPLAY_NODE_NUMBERS=None
    DIVIDEDPATH_DISPLAY_REFERENCE_CURVES=None
    DIVIDEDPATH_DISTANCE=None
    DIVIDEDPATH_END_INDENT=None
    DIVIDEDPATH_FLIP_DIRECTION=None
    DIVIDEDPATH_JUSTIFICATION=None
    DIVIDEDPATH_LAYOUT=None
    DIVIDEDPATH_LAYOUT_FIXED_NUM_POINT=None
    DIVIDEDPATH_MAX_DISTANCE=None
    DIVIDEDPATH_MEASUREMENT_TYPE=None
    DIVIDEDPATH_MERGED_POINT_NUM=None
    DIVIDEDPATH_MIN_DISTANCE=None
    DIVIDEDPATH_TOTAL_PATH_LENGTH=None
    DIVIDED_SURFACE_ALL_GRID_ROTATION=None
    DIVIDED_SURFACE_ALL_POINTS=None
    DIVIDED_SURFACE_COMPONENT_TRIM_TYPE=None
    DIVIDED_SURFACE_COVER_FACE_COMPLETELY=None
    DIVIDED_SURFACE_DISPLAY_COMPONENTS=None
    DIVIDED_SURFACE_DISPLAY_DISCARDEDDIVISIONLINES=None
    DIVIDED_SURFACE_DISPLAY_GRIDLINES=None
    DIVIDED_SURFACE_DISPLAY_NODES=None
    DIVIDED_SURFACE_DISPLAY_ORIGINAL_SURFACE=None
    DIVIDED_SURFACE_DISPLAY_PATTERN_FILL=None
    DIVIDED_SURFACE_DISPLAY_PATTERN_LINES=None
    DIVIDED_SURFACE_DISPLAY_SURFACE_OPTION=None
    DIVIDED_SURFACE_EDGE_NUMBER=None
    DIVIDED_SURFACE_FACET_NUMBER=None
    DIVIDED_SURFACE_GRIDLINES_STYLE=None
    DIVIDED_SURFACE_GRID_OPTION_PARAM_1=None
    DIVIDED_SURFACE_GRID_OPTION_PARAM_2=None
    DIVIDED_SURFACE_OFFSET_FROM_SURFACE=None
    DIVIDED_SURFACE_ORIGINAL_SURFACE_MATERIAL=None
    DIVIDED_SURFACE_PATTERN=None
    DIVIDED_SURFACE_PATTERN_FILL_MATERIAL=None
    DIVIDED_SURFACE_PATTERN_FLIP=None
    DIVIDED_SURFACE_PATTERN_INDENT_1=None
    DIVIDED_SURFACE_PATTERN_INDENT_2=None
    DIVIDED_SURFACE_PATTERN_LINES_STYLE=None
    DIVIDED_SURFACE_PATTERN_MIRROR=None
    DIVIDED_SURFACE_PATTERN_ROTATION_ANGLE=None
    DIVIDED_SURFACE_POINT_NUMBER=None
    DIVIDED_SURFACE_RULE_1_SUSPENSION=None
    DIVIDED_SURFACE_RULE_2_SUSPENSION=None
    DIVIDED_SURFACE_SURFACE_AREA=None
    DIVIDED_SURFACE_TILE_BORDER=None
    DIVIDED_SURFACE_TOTAL_EDGE_LENGTH=None
    DIVISION_PATTERN=None
    DIVISION_PROFILE_WIDTH=None
    DIVISION_RULE_PARAM=None
    DIVISION_SKETCH_CURVE_DIVISION_PARAMS_OVERRIDE_PARAM=None
    DIVISION_SKETCH_CURVE_EXTENTD_TO_SILH_PARAM=None
    DOOR_CONSTRUCTION_TYPE=None
    DOOR_COST=None
    DOOR_FINISH=None
    DOOR_FIRE_RATING=None
    DOOR_FRAME_MATERIAL=None
    DOOR_FRAME_TYPE=None
    DOOR_HEIGHT=None
    DOOR_NUMBER=None
    DOOR_OPERATION_TYPE=None
    DOOR_THICKNESS=None
    DOOR_WIDTH=None
    DPART_AREA_COMPUTED=None
    DPART_BASE_LEVEL=None
    DPART_BASE_LEVEL_BY_ORIGINAL=None
    DPART_CAN_HOST_REBAR=None
    DPART_EXCLUDED=None
    DPART_HEIGHT_COMPUTED=None
    DPART_LAYER_CONSTRUCTION=None
    DPART_LAYER_FUNCTION=None
    DPART_LAYER_WIDTH=None
    DPART_LENGTH_COMPUTED=None
    DPART_MATERIAL_BY_ORIGINAL=None
    DPART_MATERIAL_ID_PARAM=None
    DPART_ORIGINAL_CATEGORY=None
    DPART_ORIGINAL_CATEGORY_ID=None
    DPART_ORIGINAL_FAMILY=None
    DPART_ORIGINAL_TYPE=None
    DPART_PHASE_CREATED_BY_ORIGINAL=None
    DPART_PHASE_DEMOLISHED_BY_ORIGINAL=None
    DPART_SHAPE_MODIFIED=None
    DPART_VOLUME_COMPUTED=None
    DRAW_FOR_EACH_RUN=None
    DUCT_TERMINAL_ENGAGEMENT_LENGTH=None
    EDGE_LINEWORK=None
    EDITED_BY=None
    ELECTICAL_EQUIP_VOLTAGE=None
    ELECTICAL_EQUIP_WATTAGE=None
    ELEMENT_IS_CUTTING=None
    ELEMENT_LOCKED_PARAM=None
    ELEM_CATEGORY_PARAM=None
    ELEM_CATEGORY_PARAM_MT=None
    ELEM_DELETABLE_IN_FAMILY=None
    ELEM_FAMILY_AND_TYPE_PARAM=None
    ELEM_FAMILY_PARAM=None
    ELEM_IS_REFERENCE=None
    ELEM_PARTITION_PARAM=None
    ELEM_REFERENCE_NAME=None
    ELEM_REFERENCE_NAME_2D_XZ=None
    ELEM_ROOM_ID=None
    ELEM_ROOM_NAME=None
    ELEM_ROOM_NUMBER=None
    ELEM_TYPE_LABEL=None
    ELEM_TYPE_PARAM=None
    ELEVATN_TAG=None
    ELEV_ARROW_ANGLE=None
    ELEV_ARROW_FILLED=None
    ELEV_ASSOC_DATUM=None
    ELEV_REFERENCE_LABEL_POS=None
    ELEV_SHAPE=None
    ELEV_SHOW_VIEW_NAME=None
    ELEV_SYMBOL_ID=None
    ELEV_TEXT_POS=None
    ELEV_VIEW_NAME_POS=None
    ELEV_WIDTH=None
    ELLIPSE_FOCUS_MRK_VISIBLE=None
    ELLIPSE_X_PARAM=None
    ELLIPSE_Y_PARAM=None
    END_EXTENSION=None
    END_JOIN_CUTBACK=None
    END_TREATMENT=None
    END_Y_JUSTIFICATION=None
    END_Y_OFFSET_VALUE=None
    END_Z_JUSTIFICATION=None
    END_Z_OFFSET_VALUE=None
    ENERGY_ANALYSIS_ADVANCED_OPTIONS=None
    ENERGY_ANALYSIS_BUILDING_OPERATING_SCHEDULE=None
    ENERGY_ANALYSIS_CONCEPTUAL_CONSTRUCTION=None
    ENERGY_ANALYSIS_CREATE_ANALYTICAL_MODEL=None
    ENERGY_ANALYSIS_GLAZING_IS_SHADED=None
    ENERGY_ANALYSIS_HVAC_SYSTEM=None
    ENERGY_ANALYSIS_MASSZONE_COREOFFSET=None
    ENERGY_ANALYSIS_MASSZONE_DIVIDEPERIMETER=None
    ENERGY_ANALYSIS_MASSZONE_USEENERGYDATASETTINGS=None
    ENERGY_ANALYSIS_MASS_ZONING=None
    ENERGY_ANALYSIS_OUTDOOR_AIR_INFORMATION_PARAM=None
    ENERGY_ANALYSIS_PERCENTAGE_GLAZING=None
    ENERGY_ANALYSIS_PERCENTAGE_SKYLIGHTS=None
    ENERGY_ANALYSIS_SHADE_DEPTH=None
    ENERGY_ANALYSIS_SILL_HEIGHT=None
    ENERGY_ANALYSIS_SKYLIGHT_WIDTH=None
    EQUALITY_FORMULA=None
    EQUALITY_TEXT_FOR_ANGULAR_DIM=None
    EQUALITY_TEXT_FOR_CONTINUOUS_LINEAR_DIM=None
    EQUALITY_WITNESS_DISPLAY=None
    EXTRUSION_AUTO_PARAMS=None
    EXTRUSION_END_PARAM=None
    EXTRUSION_LENGTH=None
    EXTRUSION_START_PARAM=None
    FABRICATION_BOTTOM_ELEVATION_INCLUDE_INSULATION_OF_PART=None
    FABRICATION_BOTTOM_ELEVATION_OF_PART=None
    FABRICATION_BOTTOM_OF_PART=None
    FABRICATION_CENTERLINE_ELEVATION_OF_PART=None
    FABRICATION_DOUBLEWALL_MATERIAL_ABBREVIATION=None
    FABRICATION_END_OFFSET_PARAM=None
    FABRICATION_FITTING_DESCRIPTION=None
    FABRICATION_INSULATION_ABBREVIATION=None
    FABRICATION_INSULATION_SPEC=None
    FABRICATION_INSULATION_SPECIFICATION_ABBREVIATION=None
    FABRICATION_LEVEL_PARAM=None
    FABRICATION_MATERIAL_ABBREVIATION=None
    FABRICATION_OFFSET_PARAM=None
    FABRICATION_PART_ALIAS=None
    FABRICATION_PART_ANGLE=None
    FABRICATION_PART_ANGLE_OPTION=None
    FABRICATION_PART_BOUGHT_OUT=None
    FABRICATION_PART_CUT_TYPE=None
    FABRICATION_PART_DEPTH_IN=None
    FABRICATION_PART_DEPTH_IN_OPTION=None
    FABRICATION_PART_DEPTH_OUT=None
    FABRICATION_PART_DEPTH_OUT_OPTION=None
    FABRICATION_PART_DIAMETER_IN=None
    FABRICATION_PART_DIAMETER_IN_OPTION=None
    FABRICATION_PART_DIAMETER_OUT=None
    FABRICATION_PART_DIAMETER_OUT_OPTION=None
    FABRICATION_PART_DOUBLEWALL_MATERIAL=None
    FABRICATION_PART_DOUBLEWALL_MATERIAL_AREA=None
    FABRICATION_PART_DOUBLEWALL_MATERIAL_THICKNESS=None
    FABRICATION_PART_INSULATION_AREA=None
    FABRICATION_PART_ITEM_NUMBER=None
    FABRICATION_PART_LENGTH=None
    FABRICATION_PART_LENGTH_OPTION=None
    FABRICATION_PART_LINING_AREA=None
    FABRICATION_PART_MATERIAL=None
    FABRICATION_PART_MATERIAL_THICKNESS=None
    FABRICATION_PART_NOTES=None
    FABRICATION_PART_SHEETMETAL_AREA=None
    FABRICATION_PART_TAKEOFF_DIALOG_PARAM=None
    FABRICATION_PART_WEIGHT=None
    FABRICATION_PART_WIDTH_IN=None
    FABRICATION_PART_WIDTH_IN_OPTION=None
    FABRICATION_PART_WIDTH_OUT=None
    FABRICATION_PART_WIDTH_OUT_OPTION=None
    FABRICATION_PIPE_INVERT_ELEVATION=None
    FABRICATION_PRODUCT_CODE=None
    FABRICATION_PRODUCT_DATA_FINISH_DESCRIPTION=None
    FABRICATION_PRODUCT_DATA_INSTALL_TYPE=None
    FABRICATION_PRODUCT_DATA_ITEM_DESCRIPTION=None
    FABRICATION_PRODUCT_DATA_LONG_DESCRIPTION=None
    FABRICATION_PRODUCT_DATA_MATERIAL_DESCRIPTION=None
    FABRICATION_PRODUCT_DATA_OEM=None
    FABRICATION_PRODUCT_DATA_PRODUCT=None
    FABRICATION_PRODUCT_DATA_RANGE=None
    FABRICATION_PRODUCT_DATA_SIZE_DESCRIPTION=None
    FABRICATION_PRODUCT_DATA_SPECIFICATION=None
    FABRICATION_PRODUCT_ENTRY=None
    FABRICATION_RELATIVE_FILENAME=None
    FABRICATION_ROUTING_SOLUTIONS_UI_PARAM=None
    FABRICATION_SERVICE_ABBREVIATION=None
    FABRICATION_SERVICE_NAME=None
    FABRICATION_SERVICE_PARAM=None
    FABRICATION_SET_UP_DOWN_TAG=None
    FABRICATION_SLOPE_PARAM=None
    FABRICATION_SPECIFICATION=None
    FABRICATION_SPECIFICATION_ABBREVIATION=None
    FABRICATION_SPOT_BOTTOM_ELEVATION_INCLUDE_INSULATION_OF_PART=None
    FABRICATION_SPOT_BOTTOM_ELEVATION_OF_PART=None
    FABRICATION_SPOT_TOP_ELEVATION_INCLUDE_INSULATION_OF_PART=None
    FABRICATION_SPOT_TOP_ELEVATION_OF_PART=None
    FABRICATION_START_OFFSET_PARAM=None
    FABRICATION_TOP_ELEVATION_INCLUDE_INSULATION_OF_PART=None
    FABRICATION_TOP_ELEVATION_OF_PART=None
    FABRICATION_TOP_OF_PART=None
    FABRICATION_VENDOR=None
    FABRICATION_VENDOR_CODE=None
    FABRIC_BEND_DIAMETER=None
    FABRIC_NUMBER=None
    FABRIC_PARAM_COVER_OFFSET=None
    FABRIC_PARAM_CUT_BY_HOST=None
    FABRIC_PARAM_CUT_OVERALL_LENGTH=None
    FABRIC_PARAM_CUT_OVERALL_WIDTH=None
    FABRIC_PARAM_CUT_SHEET_MASS=None
    FABRIC_PARAM_LAPSPLICE_POSITION=None
    FABRIC_PARAM_LOCATION_GENERIC=None
    FABRIC_PARAM_LOCATION_SLAB=None
    FABRIC_PARAM_LOCATION_WALL=None
    FABRIC_PARAM_MAJOR_LAPSPLICE_LENGTH=None
    FABRIC_PARAM_MINOR_LAPSPLICE_LENGTH=None
    FABRIC_PARAM_ROUNDING=None
    FABRIC_PARAM_SHARED_FAMILY_KEY=None
    FABRIC_PARAM_SHEET_TYPE=None
    FABRIC_PARAM_SPAN_SYM_BOTTOM=None
    FABRIC_PARAM_SPAN_SYM_D_BOTTOM=None
    FABRIC_PARAM_SPAN_SYM_D_LEFT=None
    FABRIC_PARAM_SPAN_SYM_D_RIGHT=None
    FABRIC_PARAM_SPAN_SYM_D_TOP=None
    FABRIC_PARAM_SPAN_SYM_LEFT=None
    FABRIC_PARAM_SPAN_SYM_RIGHT=None
    FABRIC_PARAM_SPAN_SYM_TOP=None
    FABRIC_PARAM_SPAN_TAG_COMPONENT_REFERENCE=None
    FABRIC_PARAM_TAG_VIEW=None
    FABRIC_PARAM_TOTAL_SHEET_MASS=None
    FABRIC_SHEET_DEFAULT_MAJOR_LAPSPLICE_LENGTH=None
    FABRIC_SHEET_DEFAULT_MINOR_LAPSPLICE_LENGTH=None
    FABRIC_SHEET_LENGTH=None
    FABRIC_SHEET_MAJOR_DIRECTION_WIRE_TYPE=None
    FABRIC_SHEET_MAJOR_END_OVERHANG=None
    FABRIC_SHEET_MAJOR_LAYOUT_PATTERN=None
    FABRIC_SHEET_MAJOR_NUMBER_OF_WIRES=None
    FABRIC_SHEET_MAJOR_REINFORCEMENT_AREA=None
    FABRIC_SHEET_MAJOR_SPACING=None
    FABRIC_SHEET_MAJOR_START_OVERHANG=None
    FABRIC_SHEET_MASS=None
    FABRIC_SHEET_MASSUNIT=None
    FABRIC_SHEET_MINOR_DIRECTION_WIRE_TYPE=None
    FABRIC_SHEET_MINOR_END_OVERHANG=None
    FABRIC_SHEET_MINOR_LAYOUT_PATTERN=None
    FABRIC_SHEET_MINOR_NUMBER_OF_WIRES=None
    FABRIC_SHEET_MINOR_REINFORCEMENT_AREA=None
    FABRIC_SHEET_MINOR_SPACING=None
    FABRIC_SHEET_MINOR_START_OVERHANG=None
    FABRIC_SHEET_OVERALL_LENGTH=None
    FABRIC_SHEET_OVERALL_WIDTH=None
    FABRIC_SHEET_PHYSICAL_MATERIAL_ASSET=None
    FABRIC_SHEET_WIDTH=None
    FABRIC_WIRE_DIAMETER=None
    FABRIC_WIRE_DISTANCE=None
    FABRIC_WIRE_LENGTH=None
    FABRIC_WIRE_TYPE=None
    FACEROOF_LEVEL_PARAM=None
    FACEROOF_OFFSET_PARAM=None
    FAMILY_ALLOW_CUT_WITH_VOIDS=None
    FAMILY_ALWAYS_VERTICAL=None
    FAMILY_AUTOJOIN=None
    FAMILY_BASE_LEVEL_OFFSET_PARAM=None
    FAMILY_BASE_LEVEL_PARAM=None
    FAMILY_CAN_HOST_REBAR=None
    FAMILY_CATEGORY_PSEUDO_PARAM=None
    FAMILY_CONTENT_PART_TYPE=None
    FAMILY_CURVE_ATTACHMENT_PROPORTION=None
    FAMILY_CURVE_GSTYLE_FOR_2010_MASS=None
    FAMILY_CURVE_GSTYLE_PLUS_INVISIBLE=None
    FAMILY_CURVE_GSTYLE_PLUS_INVISIBLE_MINUS_ANALYTICAL=None
    FAMILY_CURVE_GSTYLE_PLUS_INVISIBLE_PLUS_STICK_SYM=None
    FAMILY_CURVE_GSTYLE_PLUS_INVISIBLE_PLUS_STICK_SYM_MINUS_ANALYTICAL=None
    FAMILY_ELECTRICAL_MAINTAIN_ANNOTATION_ORIENTATION=None
    FAMILY_ELEM_SUBCATEGORY=None
    FAMILY_ENABLE_CUTTING_IN_VIEWS=None
    FAMILY_EXPORT_AS_GEOMETRY=None
    FAMILY_HEIGHT_PARAM=None
    FAMILY_HOSTING_BEHAVIOR=None
    FAMILY_IS_ELEVATION_MARK_BODY=None
    FAMILY_IS_PARAMETRIC=None
    FAMILY_KEEP_TEXT_READABLE=None
    FAMILY_KEYWORD_PROTECTED=None
    FAMILY_KEY_EXT_PARAM=None
    FAMILY_LEVEL_PARAM=None
    FAMILY_LINE_LENGTH_PARAM=None
    FAMILY_NAME_PSEUDO_PARAM=None
    FAMILY_RENDERING_TYPE=None
    FAMILY_RFA_PATH_PSEUDO_PARAM=None
    FAMILY_ROTATE_WITH_COMPONENT=None
    FAMILY_ROUGH_HEIGHT_PARAM=None
    FAMILY_ROUGH_WIDTH_PARAM=None
    FAMILY_ROUNDCONNECTOR_DIMENSIONTYPE=None
    FAMILY_SHARED=None
    FAMILY_STRUCT_FOOTING_USE_CAP_TOP=None
    FAMILY_STRUCT_MATERIAL_TYPE=None
    FAMILY_SYMBOLIC_REP=None
    FAMILY_THICKNESS_PARAM=None
    FAMILY_TOP_LEVEL_OFFSET_PARAM=None
    FAMILY_TOP_LEVEL_PARAM=None
    FAMILY_USAGE_PSEUDO_PARAM=None
    FAMILY_USE_PRECUT_SHAPE=None
    FAMILY_WIDTH_PARAM=None
    FAMILY_WINDOW_INSET_PARAM=None
    FAMILY_WORK_PLANE_BASED=None
    FAMILY_WPB_DEFAULT_ELEVATION=None
    FAM_PROFILE_DEFINITION=None
    FAM_PROFILE_USAGE=None
    FASCIA_DEPTH_PARAM=None
    FASCIA_MATERIAL_PARAM=None
    FASCIA_PROFILE_PARAM=None
    FBX_ASSET_TYPE=None
    FBX_LIGHT_AT_A_DISTANCE=None
    FBX_LIGHT_BALLAST_LOSS=None
    FBX_LIGHT_COLOR_FILTER=None
    FBX_LIGHT_DIMMING_LIGHT_COLOR=None
    FBX_LIGHT_EFFICACY=None
    FBX_LIGHT_EMIT_CIRCLE_DIAMETER=None
    FBX_LIGHT_EMIT_LINE_LENGTH=None
    FBX_LIGHT_EMIT_RECTANGLE_LENGTH=None
    FBX_LIGHT_EMIT_RECTANGLE_WIDTH=None
    FBX_LIGHT_EMIT_SHAPE_VISIBLE=None
    FBX_LIGHT_ILLUMINANCE=None
    FBX_LIGHT_INITIAL_COLOR_CTRL=None
    FBX_LIGHT_INITIAL_COLOR_NAME=None
    FBX_LIGHT_INITIAL_COLOR_TEMPERATURE=None
    FBX_LIGHT_INITIAL_INTENSITY=None
    FBX_LIGHT_INITIAL_INTENSITY_INPUT_METHOD=None
    FBX_LIGHT_LAMP_LUMEN_DEPR=None
    FBX_LIGHT_LAMP_TILT_LOSS=None
    FBX_LIGHT_LIMUNOUS_FLUX=None
    FBX_LIGHT_LIMUNOUS_INTENSITY=None
    FBX_LIGHT_LOSS_FACTOR_CTRL=None
    FBX_LIGHT_LOSS_FACTOR_METHOD=None
    FBX_LIGHT_LUMENAIRE_DIRT=None
    FBX_LIGHT_PHOTOMETRICS=None
    FBX_LIGHT_PHOTOMETRICS_FAM=None
    FBX_LIGHT_PHOTOMETRIC_FILE=None
    FBX_LIGHT_PHOTOMETRIC_FILE_CACHE=None
    FBX_LIGHT_SOURCE_DIAMETER=None
    FBX_LIGHT_SOURCE_LENGTH=None
    FBX_LIGHT_SPOT_BEAM_ANGLE=None
    FBX_LIGHT_SPOT_FIELD_ANGLE=None
    FBX_LIGHT_SPOT_TILT_ANGLE=None
    FBX_LIGHT_SURFACE_LOSS=None
    FBX_LIGHT_TEMPERATURE_LOSS=None
    FBX_LIGHT_TOTAL_LIGHT_LOSS=None
    FBX_LIGHT_VOLTAGE_LOSS=None
    FBX_LIGHT_WATTAGE=None
    FILLED_REGION_BACKGROUND=None
    FILL_PATTERN_ID_PARAM=None
    FILL_PATTERN_ID_PARAM_NO_NO=None
    FIRE_RATING=None
    FIXED_ROTATION=None
    FLEXIBLE_INSTANCE_FLIP=None
    FLOOR_ATTR_DEFAULT_HEIGHT_PARAM=None
    FLOOR_ATTR_DEFAULT_THICKNESS_PARAM=None
    FLOOR_ATTR_THICKNESS_PARAM=None
    FLOOR_HEIGHTABOVELEVEL_PARAM=None
    FLOOR_PARAM_IS_STRUCTURAL=None
    FLOOR_PARAM_SPAN_DIRECTION=None
    FLOOR_STRUCTURE_ID_PARAM=None
    FOLLOW_SURFACE=None
    FRAMING_LENGTH_ROUNDOFF=None
    FUNCTION_PARAM=None
    FURNITURE_HEIGHT=None
    FURNITURE_THICKNESS=None
    FURNITURE_WIDTH=None
    GBXML_EDIT_DATA_PARAM=None
    GENERIC_CONSTRUCTION_TYPE=None
    GENERIC_DEPTH=None
    GENERIC_FINISH=None
    GENERIC_HEIGHT=None
    GENERIC_THICKNESS=None
    GENERIC_WIDTH=None
    GEOM_VISIBILITY_PARAM=None
    GEO_LOCATION=None
    GRAPHIC_DISPLAY_OPTIONS=None
    GRAPHIC_DISPLAY_OPTIONS_BACKGROUND=None
    GRAPHIC_DISPLAY_OPTIONS_FOG=None
    GRAPHIC_DISPLAY_OPTIONS_LIGHTING=None
    GRAPHIC_DISPLAY_OPTIONS_MODEL=None
    GRAPHIC_DISPLAY_OPTIONS_PHOTO_EXPOSURE=None
    GRAPHIC_DISPLAY_OPTIONS_SHADOWS=None
    GRAPHIC_DISPLAY_OPTIONS_SKETCHY_LINES=None
    GRAPHIC_DISPLAY_OPTIONS_SS_INTENSITY=None
    GRIDLINE_SPEC_STATUS=None
    GRID_BANK_COL_NUM=None
    GRID_BANK_COL_WIDTH=None
    GRID_BANK_ROW_HEIGHT=None
    GRID_BANK_ROW_NUM=None
    GRID_BUBBLE_END_1=None
    GRID_BUBBLE_END_2=None
    GRID_BUBBLE_LINE_PEN=None
    GRID_CENTER_SEGMENT_COLOR=None
    GRID_CENTER_SEGMENT_PATTERN=None
    GRID_CENTER_SEGMENT_STYLE=None
    GRID_CENTER_SEGMENT_WEIGHT=None
    GRID_END_SEGMENTS_LENGTH=None
    GRID_END_SEGMENT_COLOR=None
    GRID_END_SEGMENT_PATTERN=None
    GRID_END_SEGMENT_WEIGHT=None
    GRID_HEAD_TAG=None
    GROUPNAME_PARAM=None
    GROUP_ALLOWED_VIEW_TYPES=None
    GROUP_ATTACHED_PARENT_NAME=None
    GROUP_LEVEL=None
    GROUP_OFFSET_FROM_LEVEL=None
    GUIDE_GRID_NAME_PARAM=None
    GUIDE_GRID_SPACING_PARAM=None
    GUTTER_MATERIAL_PARAM=None
    GUTTER_PROFILE_PARAM=None
    HANDRAIL_HAND_CLEARANCE_PARAM=None
    HANDRAIL_HEIGHT_PARAM=None
    HANDRAIL_PROJECTION_PARAM=None
    HANDRAIL_SUPPORTS_JUSTIFICATION_PARAM=None
    HANDRAIL_SUPPORTS_LAYOUT_PARAM=None
    HANDRAIL_SUPPORTS_NUMBER_PARAM=None
    HANDRAIL_SUPPORTS_SPACING_PARAM=None
    HANDRAIL_SUPPORTS_TYPE_PARAM=None
    HEAD_ON_PLACEMENT_METHOD=None
    HEAVY_END_PEN=None
    HEAVY_TICK_MARK_PEN=None
    HOST_AREA_COMPUTED=None
    HOST_ID_PARAM=None
    HOST_PANEL_SCHEDULE_AS_PANEL_PARAM=None
    HOST_PERIMETER_COMPUTED=None
    HOST_SSE_CURVED_EDGE_CONDITION_PARAM=None
    HOST_VOLUME_COMPUTED=None
    ICON_INDEX_PARAM=None
    ID_PARAM=None
    IFC_BUILDING_GUID=None
    IFC_GUID=None
    IFC_PROJECT_GUID=None
    IFC_SITE_GUID=None
    IFC_TYPE_GUID=None
    IMPORT_ADT_COMPONENTS_DESC=None
    IMPORT_ADT_ENTITY_HEIGHT=None
    IMPORT_ADT_ENTITY_LENGTH=None
    IMPORT_ADT_ENTITY_ROLL=None
    IMPORT_ADT_ENTITY_STRUCT_TYPE=None
    IMPORT_ADT_ENTITY_STYLE=None
    IMPORT_ADT_ENTITY_THICKNESS=None
    IMPORT_ADT_ENTITY_TYPE=None
    IMPORT_ADT_ENTITY_WIDTH=None
    IMPORT_BACKGROUND=None
    IMPORT_BASE_LEVEL=None
    IMPORT_BASE_LEVEL_OFFSET=None
    IMPORT_DISPLAY_UNITS=None
    IMPORT_INSTANCE_SCALE=None
    IMPORT_SCALE=None
    IMPORT_SYMBOL_NAME=None
    INSTANCE_ELEVATION_PARAM=None
    INSTANCE_FREE_HOST_OFFSET_PARAM=None
    INSTANCE_FREE_HOST_PARAM=None
    INSTANCE_HEAD_HEIGHT_PARAM=None
    INSTANCE_LENGTH_PARAM=None
    INSTANCE_MOVES_WITH_GRID_PARAM=None
    INSTANCE_MOVE_BASE_WITH_GRIDS=None
    INSTANCE_MOVE_TOP_WITH_GRIDS=None
    INSTANCE_OFFSET_POS_PARAM=None
    INSTANCE_REFERENCE_LEVEL_PARAM=None
    INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM=None
    INSTANCE_SILL_HEIGHT_PARAM=None
    INSTANCE_STRUCT_USAGE_PARAM=None
    INSULATION_SCALE=None
    INSULATION_WIDTH=None
    INTERIOR_TICK_DISPLAY=None
    INVALID=None
    IS_VISIBLE_PARAM=None
    JOIN_STRENGTH_ORDER=None
    JOIST_SYSTEM_CLEAR_SPACING_PARAM=None
    JOIST_SYSTEM_ELEM_TAG_NEW_MEMBERS_VIEW=None
    JOIST_SYSTEM_FIXED_SPACING_PARAM=None
    JOIST_SYSTEM_JUSTIFICATION_PARAM=None
    JOIST_SYSTEM_LAYOUT_RULE_PARAM=None
    JOIST_SYSTEM_MAXIMUM_SPACING_PARAM=None
    JOIST_SYSTEM_NEW_BEAM_TYPE_NO_FAM_NAME_PARAM=None
    JOIST_SYSTEM_NEW_BEAM_TYPE_PARAM=None
    JOIST_SYSTEM_NUMBER_OF_LINES_PARAM=None
    JOIST_SYSTEM_NUM_BEAMS_SAME_TYPE=None
    JOIST_SYSTEM_SPACING_PARAM=None
    KEEP_READABLE=None
    KEYNOTE_NUMBER=None
    KEYNOTE_PARAM=None
    KEYNOTE_TEXT=None
    KEY_SOURCE_PARAM=None
    KEY_VALUE=None
    LAYOUTNODE_CURVETYPE_PARAM=None
    LEADER_ARROWHEAD=None
    LEADER_ARROW_WIDTH=None
    LEADER_LEFT_ATTACHMENT=None
    LEADER_LINE=None
    LEADER_OFFSET_SHEET=None
    LEADER_RIGHT_ATTACHMENT=None
    LEGEND_COMPONENT=None
    LEGEND_COMPONENT_DETAIL_LEVEL=None
    LEGEND_COMPONENT_LENGTH=None
    LEGEND_COMPONENT_VIEW=None
    LEVEL_ATTR_ROOM_COMPUTATION_AUTOMATIC=None
    LEVEL_ATTR_ROOM_COMPUTATION_HEIGHT=None
    LEVEL_DATA_FLOOR_AREA=None
    LEVEL_DATA_FLOOR_PERIMETER=None
    LEVEL_DATA_MASS_FAMILY_AND_TYPE_PARAM=None
    LEVEL_DATA_MASS_FAMILY_PARAM=None
    LEVEL_DATA_MASS_INSTANCE_COMMENTS=None
    LEVEL_DATA_MASS_TYPE_COMMENTS=None
    LEVEL_DATA_MASS_TYPE_DESCRIPTION=None
    LEVEL_DATA_MASS_TYPE_PARAM=None
    LEVEL_DATA_OWNING_LEVEL=None
    LEVEL_DATA_SPACE_USAGE=None
    LEVEL_DATA_SURFACE_AREA=None
    LEVEL_DATA_VOLUME=None
    LEVEL_ELEV=None
    LEVEL_HEAD_TAG=None
    LEVEL_IS_BUILDING_STORY=None
    LEVEL_IS_GROUND_PLANE=None
    LEVEL_IS_STRUCTURAL=None
    LEVEL_NAME=None
    LEVEL_PARAM=None
    LEVEL_RELATIVE_BASE_TYPE=None
    LEVEL_ROOM_COMPUTATION_HEIGHT=None
    LEVEL_UP_TO_LEVEL=None
    LIGHTING_FIXTURE_LAMP=None
    LIGHTING_FIXTURE_LIGHT_EMITTER=None
    LIGHTING_FIXTURE_WATTAGE=None
    LINEAR_DIM_TYPE=None
    LINE_COLOR=None
    LINE_PATTERN=None
    LINE_PEN=None
    LINE_SHAPE_AT_CORNER=None
    LOAD_ALL_NON_0_LOADS=None
    LOAD_AREA_AREA=None
    LOAD_AREA_FORCE_FX1=None
    LOAD_AREA_FORCE_FX2=None
    LOAD_AREA_FORCE_FX3=None
    LOAD_AREA_FORCE_FY1=None
    LOAD_AREA_FORCE_FY2=None
    LOAD_AREA_FORCE_FY3=None
    LOAD_AREA_FORCE_FZ1=None
    LOAD_AREA_FORCE_FZ2=None
    LOAD_AREA_FORCE_FZ3=None
    LOAD_AREA_IS_PROJECTED=None
    LOAD_ARROW_SEPARATION=None
    LOAD_ATTR_AREA_FORCE_SCALE_FACTOR=None
    LOAD_ATTR_FORCE_ARROW_TYPE=None
    LOAD_ATTR_FORCE_SCALE_FACTOR=None
    LOAD_ATTR_LINEAR_FORCE_SCALE_FACTOR=None
    LOAD_ATTR_MOMENT_ARROW_ARC=None
    LOAD_ATTR_MOMENT_ARROW_LINE=None
    LOAD_ATTR_MOMENT_SCALE_FACTOR=None
    LOAD_CASE_ID=None
    LOAD_CASE_NAME=None
    LOAD_CASE_NATURE=None
    LOAD_CASE_NATURE_TEXT=None
    LOAD_CASE_NUMBER=None
    LOAD_CASE_SUBCATEGORY=None
    LOAD_COMBINATION_FACTOR=None
    LOAD_COMBINATION_NAME=None
    LOAD_COMMENTS=None
    LOAD_DESCRIPTION=None
    LOAD_FORCE_FX=None
    LOAD_FORCE_FY=None
    LOAD_FORCE_FZ=None
    LOAD_IS_CREATED_BY_API=None
    LOAD_IS_HOSTED=None
    LOAD_IS_PROJECTED=None
    LOAD_IS_REACTION=None
    LOAD_IS_UNIFORM=None
    LOAD_LINEAR_FORCE_FX1=None
    LOAD_LINEAR_FORCE_FX2=None
    LOAD_LINEAR_FORCE_FY1=None
    LOAD_LINEAR_FORCE_FY2=None
    LOAD_LINEAR_FORCE_FZ1=None
    LOAD_LINEAR_FORCE_FZ2=None
    LOAD_LINEAR_LENGTH=None
    LOAD_MOMENT_MX=None
    LOAD_MOMENT_MX1=None
    LOAD_MOMENT_MX2=None
    LOAD_MOMENT_MY=None
    LOAD_MOMENT_MY1=None
    LOAD_MOMENT_MY2=None
    LOAD_MOMENT_MZ=None
    LOAD_MOMENT_MZ1=None
    LOAD_MOMENT_MZ2=None
    LOAD_NATURE_NAME=None
    LOAD_USAGE_NAME=None
    LOAD_USE_LOCAL_COORDINATE_SYSTEM=None
    LOCKED_BASE_OFFSET=None
    LOCKED_END_OFFSET=None
    LOCKED_START_OFFSET=None
    LOCKED_TOP_OFFSET=None
    LV_MULLION_LEG1=None
    LV_MULLION_LEG2=None
    MARKUPS_CREATED=None
    MARKUPS_CREATOR=None
    MARKUPS_HISTORY=None
    MARKUPS_LABEL=None
    MARKUPS_MODIFIED=None
    MARKUPS_NOTES=None
    MARKUPS_PRIVATE=None
    MARKUPS_STATUS=None
    MASSING_INTEGRATION_LEVEL=None
    MASS_DATA_CONCEPTUAL_CONSTRUCTION=None
    MASS_DATA_GLAZING_IS_SHADED=None
    MASS_DATA_MASS_EXTERIOR_WALL_AREA=None
    MASS_DATA_MASS_INTERIOR_WALL_AREA=None
    MASS_DATA_MASS_OPENING_AREA=None
    MASS_DATA_MASS_ROOF_AREA=None
    MASS_DATA_MASS_SKYLIGHT_AREA=None
    MASS_DATA_MASS_WINDOW_AREA=None
    MASS_DATA_PERCENTAGE_GLAZING=None
    MASS_DATA_PERCENTAGE_SKYLIGHTS=None
    MASS_DATA_SHADE_DEPTH=None
    MASS_DATA_SILL_HEIGHT=None
    MASS_DATA_SKYLIGHT_WIDTH=None
    MASS_DATA_SLAB=None
    MASS_DATA_SUBCATEGORY=None
    MASS_DATA_SURFACE_DATA_SOURCE=None
    MASS_DATA_UNDERGROUND=None
    MASS_FLOOR_AREA_LEVELS=None
    MASS_GROSS_AREA=None
    MASS_GROSS_SURFACE_AREA=None
    MASS_GROSS_VOLUME=None
    MASS_SURFACEDATA_MATERIAL=None
    MASS_ZONE_CONDITION_TYPE_PARAM=None
    MASS_ZONE_FLOOR_AREA=None
    MASS_ZONE_MATERIAL=None
    MASS_ZONE_SPACE_TYPE_PARAM=None
    MASS_ZONE_VOLUME=None
    MATCHLINE_BOTTOM_OFFSET=None
    MATCHLINE_BOTTOM_PLANE=None
    MATCHLINE_TOP_OFFSET=None
    MATCHLINE_TOP_PLANE=None
    MATERIAL_AREA=None
    MATERIAL_ASPAINT=None
    MATERIAL_ASSET_PARAM_ASSET_LIB_ID=None
    MATERIAL_ASSET_PARAM_COMMON_SHARED_ASSET=None
    MATERIAL_ASSET_PARAM_EXTERNAL_MATERIAL_ID=None
    MATERIAL_ASSET_PARAM_SOURCE=None
    MATERIAL_ASSET_PARAM_SOURCE_URL=None
    MATERIAL_ID_PARAM=None
    MATERIAL_NAME=None
    MATERIAL_PARAM_COLOR=None
    MATERIAL_PARAM_GLOW=None
    MATERIAL_PARAM_SHININESS=None
    MATERIAL_PARAM_SMOOTHNESS=None
    MATERIAL_PARAM_TRANSPARENCY=None
    MATERIAL_VOLUME=None
    MEASURE_FROM_STRUCTURE=None
    MEP_PROFILE_TYPE_PARAM=None
    MODEL_CATEGORY_ID_PARAM=None
    MODEL_GRAPHICS_STYLE=None
    MODEL_GRAPHICS_STYLE_ANON_DRAFT=None
    MODEL_OR_SYMBOLIC=None
    MODEL_TEXT_SIZE=None
    MULLION_ANGLE=None
    MULLION_CORNER_TYPE=None
    MULLION_DEPTH=None
    MULLION_DEPTH1=None
    MULLION_DEPTH2=None
    MULLION_FAM_TYPE=None
    MULLION_OFFSET=None
    MULLION_POSITION=None
    MULLION_PROFILE=None
    MULTISTORY_STAIRS_ACTUAL_TREAD_DEPTH=None
    MULTISTORY_STAIRS_REF_LEVEL=None
    MULTISTORY_STAIRS_RUN_BEGIN_WITH_RISER=None
    MULTISTORY_STAIRS_RUN_END_WITH_RISER=None
    MULTI_REFERENCE_ANNOTATION_DIMENSION_STYLE=None
    MULTI_REFERENCE_ANNOTATION_GROUP_TAG_HEADS=None
    MULTI_REFERENCE_ANNOTATION_REFERENCE_CATEGORY=None
    MULTI_REFERENCE_ANNOTATION_SHOW_DIMENSION_TEXT=None
    MULTI_REFERENCE_ANNOTATION_TAG_TYPE=None
    NODE_CONNECTION_STATUS=None
    NUMBER_PARTITION_PARAM=None
    NUMBER_SYSTEM_DISPLAY_RULE=None
    NUMBER_SYSTEM_JUSTIFY=None
    NUMBER_SYSTEM_JUSTIFY_OFFSET=None
    NUMBER_SYSTEM_ORIENTATION=None
    NUMBER_SYSTEM_REFERENCE=None
    NUMBER_SYSTEM_REFERENCE_OFFSET=None
    NUMBER_SYSTEM_TAG_TYPE=None
    NUMBER_SYSTEM_TEXT_SIZE=None
    OBJECT_STYLE_MATERIAL_ID_PARAM=None
    OFFSETFACES_SHOW_SHAPE_HANDLES=None
    OMNICLASS_CODE=None
    OMNICLASS_DESCRIPTION=None
    OPTION_NAME=None
    OPTION_SET_ID=None
    OPTION_SET_NAME=None
    ORDINATE_DIM_SETTING=None
    ORIENT_BY_VIEW=None
    PADDING_LENGTH=None
    PANEL_SCHEDULE_NAME=None
    PARTMAKER_PARAM_DIVISION_GAP=None
    PART_MAKER_DIVISION_PROFILE_OFFSET=None
    PART_MAKER_SPLITTER_PROFILE=None
    PART_MAKER_SPLITTER_PROFILE_EDGE_MATCH=None
    PART_MAKER_SPLITTER_PROFILE_FLIP_ACROSS=None
    PART_MAKER_SPLITTER_PROFILE_FLIP_ALONG=None
    PATH_REIN_ADDL_OFFSET=None
    PATH_REIN_ALTERNATING=None
    PATH_REIN_ALT_OFFSET=None
    PATH_REIN_END_HOOK_ORIENT_1_SLAB=None
    PATH_REIN_END_HOOK_ORIENT_1_WALL=None
    PATH_REIN_END_HOOK_ORIENT_2_SLAB=None
    PATH_REIN_END_HOOK_ORIENT_2_WALL=None
    PATH_REIN_END_HOOK_TYPE_1=None
    PATH_REIN_END_HOOK_TYPE_2=None
    PATH_REIN_END_SPANHOOK_ALT=None
    PATH_REIN_END_SPANHOOK_PRIM=None
    PATH_REIN_FACE_SLAB=None
    PATH_REIN_FACE_WALL=None
    PATH_REIN_HOOK_ORIENT_1_SLAB=None
    PATH_REIN_HOOK_ORIENT_1_WALL=None
    PATH_REIN_HOOK_ORIENT_2_SLAB=None
    PATH_REIN_HOOK_ORIENT_2_WALL=None
    PATH_REIN_HOOK_TYPE_1=None
    PATH_REIN_HOOK_TYPE_2=None
    PATH_REIN_LENGTH_1=None
    PATH_REIN_LENGTH_2=None
    PATH_REIN_NUMBER_OF_BARS=None
    PATH_REIN_SHAPE_1=None
    PATH_REIN_SHAPE_2=None
    PATH_REIN_SPACING=None
    PATH_REIN_SPANHOOK_ALT=None
    PATH_REIN_SPANHOOK_PRIM=None
    PATH_REIN_SPANLENGTH_ALT_OFFSET=None
    PATH_REIN_SPANLENGTH_BARLENGTH_ALT=None
    PATH_REIN_SPANLENGTH_BARLENGTH_PRIM=None
    PATH_REIN_SPANLENGTH_BOTTOM_ALT=None
    PATH_REIN_SPANLENGTH_BOTTOM_PRIM=None
    PATH_REIN_SPANLENGTH_TOP_ALT=None
    PATH_REIN_SUMMARY=None
    PATH_REIN_TYPE_1=None
    PATH_REIN_TYPE_2=None
    PATTERN_INDENT_1_FOR_DIVISION_RULE=None
    PATTERN_INDENT_2_FOR_DIVISION_RULE=None
    PATTERN_MIRROR_FOR_DIVISION_RULE=None
    PHASE_CREATED=None
    PHASE_DEMOLISHED=None
    PHASE_NAME=None
    PHASE_SEQUENCE_NUMBER=None
    PHY_MATERIAL_PARAM_AVERAGE_MODULUS=None
    PHY_MATERIAL_PARAM_BEHAVIOR=None
    PHY_MATERIAL_PARAM_BENDING=None
    PHY_MATERIAL_PARAM_BENDING_REINFORCEMENT=None
    PHY_MATERIAL_PARAM_CLASS=None
    PHY_MATERIAL_PARAM_COMPRESSION_PARALLEL=None
    PHY_MATERIAL_PARAM_COMPRESSION_PERPENDICULAR=None
    PHY_MATERIAL_PARAM_CONCRETE_COMPRESSION=None
    PHY_MATERIAL_PARAM_DAMPING_RATIO=None
    PHY_MATERIAL_PARAM_EXP_COEFF=None
    PHY_MATERIAL_PARAM_EXP_COEFF1=None
    PHY_MATERIAL_PARAM_EXP_COEFF2=None
    PHY_MATERIAL_PARAM_EXP_COEFF3=None
    PHY_MATERIAL_PARAM_EXP_COEFF_1=None
    PHY_MATERIAL_PARAM_EXP_COEFF_2=None
    PHY_MATERIAL_PARAM_FIVEPERCENT_MODULUS_OF_ELACTICITY=None
    PHY_MATERIAL_PARAM_GRADE=None
    PHY_MATERIAL_PARAM_LIGHT_WEIGHT=None
    PHY_MATERIAL_PARAM_MINIMUM_TENSILE_STRENGTH=None
    PHY_MATERIAL_PARAM_MINIMUM_YIELD_STRESS=None
    PHY_MATERIAL_PARAM_POISSON_MOD=None
    PHY_MATERIAL_PARAM_POISSON_MOD1=None
    PHY_MATERIAL_PARAM_POISSON_MOD2=None
    PHY_MATERIAL_PARAM_POISSON_MOD3=None
    PHY_MATERIAL_PARAM_POISSON_MOD_12=None
    PHY_MATERIAL_PARAM_POISSON_MOD_23=None
    PHY_MATERIAL_PARAM_REDUCTION_FACTOR=None
    PHY_MATERIAL_PARAM_RESISTANCE_CALC_STRENGTH=None
    PHY_MATERIAL_PARAM_SHEAR_MOD=None
    PHY_MATERIAL_PARAM_SHEAR_MOD1=None
    PHY_MATERIAL_PARAM_SHEAR_MOD2=None
    PHY_MATERIAL_PARAM_SHEAR_MOD3=None
    PHY_MATERIAL_PARAM_SHEAR_MOD_12=None
    PHY_MATERIAL_PARAM_SHEAR_PARALLEL=None
    PHY_MATERIAL_PARAM_SHEAR_PERPENDICULAR=None
    PHY_MATERIAL_PARAM_SHEAR_REINFORCEMENT=None
    PHY_MATERIAL_PARAM_SHEAR_STRENGTH_REDUCTION=None
    PHY_MATERIAL_PARAM_SPECIES=None
    PHY_MATERIAL_PARAM_STRUCTURAL_DENSITY=None
    PHY_MATERIAL_PARAM_STRUCTURAL_SPECIFIC_HEAT=None
    PHY_MATERIAL_PARAM_STRUCTURAL_THERMAL_TREATED=None
    PHY_MATERIAL_PARAM_SUBCLASS=None
    PHY_MATERIAL_PARAM_TENSION_PARALLEL=None
    PHY_MATERIAL_PARAM_TENSION_PERPENDICULAR=None
    PHY_MATERIAL_PARAM_THERMAL_CONDUCTIVITY=None
    PHY_MATERIAL_PARAM_THERMAL_CONDUCTIVITY_X=None
    PHY_MATERIAL_PARAM_THERMAL_CONDUCTIVITY_Y=None
    PHY_MATERIAL_PARAM_THERMAL_CONDUCTIVITY_Z=None
    PHY_MATERIAL_PARAM_TYPE=None
    PHY_MATERIAL_PARAM_UNIT_WEIGHT=None
    PHY_MATERIAL_PARAM_WOOD_CONSTRUCTION=None
    PHY_MATERIAL_PARAM_YOUNG_MOD=None
    PHY_MATERIAL_PARAM_YOUNG_MOD1=None
    PHY_MATERIAL_PARAM_YOUNG_MOD2=None
    PHY_MATERIAL_PARAM_YOUNG_MOD3=None
    PHY_MATERIAL_PARAM_YOUNG_MOD_1=None
    PHY_MATERIAL_PARAM_YOUNG_MOD_2=None
    PHY_MATERIAL_PROPERTIES=None
    PIPING_CONNECTION_TYPE=None
    PIPING_GENDER_TYPE=None
    PLAN_REGION_VIEW_RANGE=None
    PLAN_VIEW_CUT_PLANE_HEIGHT=None
    PLAN_VIEW_LEVEL=None
    PLAN_VIEW_NORTH=None
    PLAN_VIEW_RANGE=None
    PLAN_VIEW_TOP_CLIP_HEIGHT=None
    PLAN_VIEW_VIEW_DIR=None
    PLUMBING_FIXTURES_CW_CONNECTION=None
    PLUMBING_FIXTURES_DRAIN=None
    PLUMBING_FIXTURES_HW_CONNECTION=None
    PLUMBING_FIXTURES_SUPPLY_FITTING=None
    PLUMBING_FIXTURES_SUPPLY_PIPE=None
    PLUMBING_FIXTURES_TRAP=None
    PLUMBING_FIXTURES_VENT_CONNECTION=None
    PLUMBING_FIXTURES_WASTE_CONNECTION=None
    POCHE_MAT_ID=None
    POINTCLOUDINSTANCE_NAME=None
    POINTCLOUDTYPE_SCALE=None
    POINT_ADAPTIVE_CONSTRAINED=None
    POINT_ADAPTIVE_NUM_PARAM=None
    POINT_ADAPTIVE_ORIENTATION_TYPE=None
    POINT_ADAPTIVE_SHOW_NUMBER=None
    POINT_ADAPTIVE_TYPE_PARAM=None
    POINT_ELEMENT_ANGLE=None
    POINT_ELEMENT_CHORD_LENGTH=None
    POINT_ELEMENT_DRIVEN=None
    POINT_ELEMENT_DRIVING=None
    POINT_ELEMENT_HOSTED_ON_FACE_U_PARAM=None
    POINT_ELEMENT_HOSTED_ON_FACE_V_PARAM=None
    POINT_ELEMENT_HOSTED_PARAM=None
    POINT_ELEMENT_MEASUREMENT_TYPE=None
    POINT_ELEMENT_MEASURE_FROM=None
    POINT_ELEMENT_MIRRORED=None
    POINT_ELEMENT_NON_NORMALIZED_CURVE_PARAMATER=None
    POINT_ELEMENT_NORMALIZED_CURVE_PARAMATER=None
    POINT_ELEMENT_NORMALIZED_SEGMENT_LENGTH=None
    POINT_ELEMENT_OFFSET=None
    POINT_ELEMENT_ROTATION_ANGLE=None
    POINT_ELEMENT_SEGMENT_LENGTH=None
    POINT_ELEMENT_SHOW_NORMAL_PLANE_ONLY=None
    POINT_ELEMENT_SHOW_PLANES=None
    POINT_ELEMENT_ZFLIPPED=None
    POINT_ELEVATION=None
    POINT_FLEXIBLE_CONSTRAINED=None
    POINT_FLEXIBLE_NUM_PARAM=None
    POINT_FLEXIBLE_ORIENTATION_TYPE=None
    POINT_FLEXIBLE_SHOW_NUMBER=None
    POINT_NAME_PARAM=None
    POINT_VISIBILITY_PARAM=None
    PRIMARY_OPTION_ID=None
    PROFILE1_ANGLE=None
    PROFILE1_FAM_TYPE=None
    PROFILE1_FLIPPED_HOR=None
    PROFILE1_OFFSET_X=None
    PROFILE1_OFFSET_Y=None
    PROFILE2_ANGLE=None
    PROFILE2_FAM_TYPE=None
    PROFILE2_FLIPPED_HOR=None
    PROFILE2_OFFSET_X=None
    PROFILE2_OFFSET_Y=None
    PROFILE_ANGLE=None
    PROFILE_FAM_TYPE=None
    PROFILE_FAM_TYPE_PLUS_NONE=None
    PROFILE_FLIPPED_HOR=None
    PROFILE_OFFSET_X=None
    PROFILE_OFFSET_Y=None
    PROFILE_PARAM_ALONG_PATH=None
    PROJECTED_SURFACE_AREA=None
    PROJECT_ADDRESS=None
    PROJECT_AUTHOR=None
    PROJECT_BUILDING_NAME=None
    PROJECT_BUILDING_TYPE=None
    PROJECT_ISSUE_DATE=None
    PROJECT_NAME=None
    PROJECT_NUMBER=None
    PROJECT_ORGANIZATION_DESCRIPTION=None
    PROJECT_ORGANIZATION_NAME=None
    PROJECT_POSTAL_CODE=None
    PROJECT_REVISION_ENUMERATION=None
    PROJECT_REVISION_REVISION_DATE=None
    PROJECT_REVISION_REVISION_DESCRIPTION=None
    PROJECT_REVISION_REVISION_ISSUED=None
    PROJECT_REVISION_REVISION_ISSUED_BY=None
    PROJECT_REVISION_REVISION_ISSUED_TO=None
    PROJECT_REVISION_REVISION_NUM=None
    PROJECT_REVISION_SEQUENCE_NUM=None
    PROJECT_STATUS=None
    PROPERTY_AREA=None
    PROPERTY_AREA_OPEN=None
    PROPERTY_AREA_UNITS=None
    PROPERTY_LENGTH_UNITS=None
    PROPERTY_SEGMENT_BEARING=None
    PROPERTY_SEGMENT_DISTANCE=None
    PROPERTY_SEGMENT_E_W=None
    PROPERTY_SEGMENT_L_R=None
    PROPERTY_SEGMENT_N_S=None
    PROPERTY_SEGMENT_RADIUS=None
    PROPERTY_SEGMENT_SUBCATEGORY_ID=None
    PROPERTY_SET_DESCRIPTION=None
    PROPERTY_SET_KEYWORDS=None
    PROPERTY_SET_MATERIAL_ASPECT=None
    PROPERTY_SET_NAME=None
    PROPERTY_SUBCATEGORY_ID=None
    RADIAL_ARRAY_ARC_RADIUS=None
    RADIUS_SYMBOL_LOCATION=None
    RADIUS_SYMBOL_TEXT=None
    RAILING_SYSTEM_HANDRAILS_HEIGHT_PARAM=None
    RAILING_SYSTEM_HANDRAILS_LATTERAL_OFFSET=None
    RAILING_SYSTEM_HANDRAILS_POSITION_PARAM=None
    RAILING_SYSTEM_HANDRAILS_TYPES_PARAM=None
    RAILING_SYSTEM_HAS_TOP_RAIL=None
    RAILING_SYSTEM_SECONDARY_HANDRAILS_HEIGHT_PARAM=None
    RAILING_SYSTEM_SECONDARY_HANDRAILS_LATTERAL_OFFSET=None
    RAILING_SYSTEM_SECONDARY_HANDRAILS_POSITION_PARAM=None
    RAILING_SYSTEM_SECONDARY_HANDRAILS_TYPES_PARAM=None
    RAILING_SYSTEM_TOP_RAIL_HEIGHT_PARAM=None
    RAILING_SYSTEM_TOP_RAIL_TYPES_PARAM=None
    RAMP_ATTR_LEFT_BALUSTER_ATTACH_PT=None
    RAMP_ATTR_MATERIAL=None
    RAMP_ATTR_MIN_INV_SLOPE=None
    RAMP_ATTR_RIGHT_BALUSTER_ATTACH_PT=None
    RAMP_ATTR_SHAPE=None
    RAMP_ATTR_TEXT_FONT=None
    RAMP_ATTR_TEXT_SIZE=None
    RAMP_ATTR_THICKNESS=None
    RAMP_MAX_RUN_LENGTH=None
    RASTER_HORIZONTAL_SCALE=None
    RASTER_MAINTAIN_ASPECT_RATIO=None
    RASTER_SHEETHEIGHT=None
    RASTER_SHEETWIDTH=None
    RASTER_SYMBOL_FILENAME=None
    RASTER_SYMBOL_HEIGHT=None
    RASTER_SYMBOL_PIXELHEIGHT=None
    RASTER_SYMBOL_PIXELWIDTH=None
    RASTER_SYMBOL_RESOLUTION=None
    RASTER_SYMBOL_VIEWNAME=None
    RASTER_SYMBOL_WIDTH=None
    RASTER_VERTICAL_SCALE=None
    RBS_ADDITIONAL_FLOW=None
    RBS_ADJUSTABLE_CONNECTOR=None
    RBS_BUILDING_CONSTRUCTIONCLASS=None
    RBS_BUILDING_USELOADCREDITS=None
    RBS_CABLETRAYCONDUITRUN_LENGTH_PARAM=None
    RBS_CABLETRAYCONDUIT_BENDORFITTING=None
    RBS_CABLETRAYCONDUIT_CONNECTORELEM_TYPE=None
    RBS_CABLETRAYCONDUIT_SYSTEM_TYPE=None
    RBS_CABLETRAYRUN_HEIGHT_PARAM=None
    RBS_CABLETRAYRUN_WIDTH_PARAM=None
    RBS_CABLETRAY_BENDRADIUS=None
    RBS_CABLETRAY_HEIGHT_PARAM=None
    RBS_CABLETRAY_RUNGHEIGHT=None
    RBS_CABLETRAY_RUNGSPACE=None
    RBS_CABLETRAY_RUNGWIDTH=None
    RBS_CABLETRAY_SHAPETYPE=None
    RBS_CABLETRAY_THICKNESS=None
    RBS_CABLETRAY_WIDTH_PARAM=None
    RBS_CALCULATED_SIZE=None
    RBS_COMPONENT_CLASSIFICATION_PARAM=None
    RBS_CONDUITRUN_DIAMETER_PARAM=None
    RBS_CONDUITRUN_INNER_DIAM_PARAM=None
    RBS_CONDUITRUN_OUTER_DIAM_PARAM=None
    RBS_CONDUIT_BENDRADIUS=None
    RBS_CONDUIT_DIAMETER_PARAM=None
    RBS_CONDUIT_INNER_DIAM_PARAM=None
    RBS_CONDUIT_OUTER_DIAM_PARAM=None
    RBS_CONDUIT_TRADESIZE=None
    RBS_CONNECTOR_DESCRIPTION=None
    RBS_CONNECTOR_ISPRIMARY=None
    RBS_CONNECTOR_OFFSET_OBSOLETE=None
    RBS_CONSTRUCTION_SET_PARAM=None
    RBS_CONSTRUCTION_TYPE_SHADINGFACTOR_PARAM=None
    RBS_CTC_BOTTOM_ELEVATION=None
    RBS_CTC_SERVICE_TYPE=None
    RBS_CTC_TOP_ELEVATION=None
    RBS_CURVETYPE_DEFAULT_BEND_PARAM=None
    RBS_CURVETYPE_DEFAULT_CAP_PARAM=None
    RBS_CURVETYPE_DEFAULT_CROSS_PARAM=None
    RBS_CURVETYPE_DEFAULT_ELBOWDOWN_PARAM=None
    RBS_CURVETYPE_DEFAULT_ELBOWUP_PARAM=None
    RBS_CURVETYPE_DEFAULT_ELBOW_PARAM=None
    RBS_CURVETYPE_DEFAULT_HORIZONTAL_BEND_PARAM=None
    RBS_CURVETYPE_DEFAULT_MECHJOINT_PARAM=None
    RBS_CURVETYPE_DEFAULT_TAKEOFF_PARAM=None
    RBS_CURVETYPE_DEFAULT_TEEDOWN_PARAM=None
    RBS_CURVETYPE_DEFAULT_TEEUP_PARAM=None
    RBS_CURVETYPE_DEFAULT_TEE_PARAM=None
    RBS_CURVETYPE_DEFAULT_TRANSITION_PARAM=None
    RBS_CURVETYPE_DEFAULT_UNION_PARAM=None
    RBS_CURVETYPE_MAX_HEIGHT_PARAM=None
    RBS_CURVETYPE_MAX_WIDTH_PARAM=None
    RBS_CURVETYPE_MULTISHAPE_TRANSITION_OVALROUND_PARAM=None
    RBS_CURVETYPE_MULTISHAPE_TRANSITION_PARAM=None
    RBS_CURVETYPE_MULTISHAPE_TRANSITION_RECTOVAL_PARAM=None
    RBS_CURVETYPE_PREFERRED_BRANCH_PARAM=None
    RBS_CURVETYPE_ROUGHNESS_PARAM=None
    RBS_CURVE_DIAMETER_PARAM=None
    RBS_CURVE_HEIGHT_PARAM=None
    RBS_CURVE_HOR_OFFSET_PARAM=None
    RBS_CURVE_SLOPE=None
    RBS_CURVE_SURFACE_AREA=None
    RBS_CURVE_UTSLOPE=None
    RBS_CURVE_VERT_OFFSET_PARAM=None
    RBS_CURVE_WIDTH_PARAM=None
    RBS_DISTRIBUTIONSYS_CONFIG_PARAM=None
    RBS_DISTRIBUTIONSYS_NUMWIRES_PARAM=None
    RBS_DISTRIBUTIONSYS_PHASE_PARAM=None
    RBS_DISTRIBUTIONSYS_VLG_PARAM=None
    RBS_DISTRIBUTIONSYS_VLL_PARAM=None
    RBS_DUCT_BOTTOM_ELEVATION=None
    RBS_DUCT_CALCULATED_SIZE=None
    RBS_DUCT_CONNECTOR_SYSTEM_CLASSIFICATION_PARAM=None
    RBS_DUCT_FITTING_LOSS_METHOD_PARAM=None
    RBS_DUCT_FITTING_LOSS_METHOD_SERVER_PARAM=None
    RBS_DUCT_FITTING_LOSS_METHOD_SETTINGS=None
    RBS_DUCT_FITTING_LOSS_TABLE_PARAM=None
    RBS_DUCT_FLOW_CONFIGURATION_PARAM=None
    RBS_DUCT_FLOW_DIRECTION_PARAM=None
    RBS_DUCT_FLOW_PARAM=None
    RBS_DUCT_PIPE_SYSTEM_ABBREVIATION_PARAM=None
    RBS_DUCT_PRESSURE_DROP=None
    RBS_DUCT_ROUTING_PREFERENCE_PARAM=None
    RBS_DUCT_SIZE_FORMATTED_PARAM=None
    RBS_DUCT_SLOPE=None
    RBS_DUCT_STATIC_PRESSURE=None
    RBS_DUCT_SYSTEM_CALCULATION_PARAM=None
    RBS_DUCT_SYSTEM_TYPE_PARAM=None
    RBS_DUCT_TOP_ELEVATION=None
    RBS_DUCT_TYPE_PARAM=None
    RBS_ELECTRICAL_DATA=None
    RBS_ELEC_AMBIENT_TEMPERATURE=None
    RBS_ELEC_APPARENT_CURRENT_PARAM=None
    RBS_ELEC_APPARENT_CURRENT_PHASEA_PARAM=None
    RBS_ELEC_APPARENT_CURRENT_PHASEB_PARAM=None
    RBS_ELEC_APPARENT_CURRENT_PHASEC_PARAM=None
    RBS_ELEC_APPARENT_LOAD=None
    RBS_ELEC_APPARENT_LOAD_PHASE1=None
    RBS_ELEC_APPARENT_LOAD_PHASE2=None
    RBS_ELEC_APPARENT_LOAD_PHASE3=None
    RBS_ELEC_APPARENT_LOAD_PHASEA=None
    RBS_ELEC_APPARENT_LOAD_PHASEB=None
    RBS_ELEC_APPARENT_LOAD_PHASEC=None
    RBS_ELEC_BALANCED_LOAD=None
    RBS_ELEC_CALC_COEFFICIENT_UTILIZATION=None
    RBS_ELEC_CIRCUIT_FRAME_PARAM=None
    RBS_ELEC_CIRCUIT_LENGTH_PARAM=None
    RBS_ELEC_CIRCUIT_NAME=None
    RBS_ELEC_CIRCUIT_NAMING=None
    RBS_ELEC_CIRCUIT_NOTES_PARAM=None
    RBS_ELEC_CIRCUIT_NUMBER=None
    RBS_ELEC_CIRCUIT_NUMBER_OF_ELEMENTS_PARAM=None
    RBS_ELEC_CIRCUIT_PANEL_PARAM=None
    RBS_ELEC_CIRCUIT_PREFIX=None
    RBS_ELEC_CIRCUIT_PREFIX_SEPARATOR=None
    RBS_ELEC_CIRCUIT_RATING_PARAM=None
    RBS_ELEC_CIRCUIT_START_SLOT=None
    RBS_ELEC_CIRCUIT_TYPE=None
    RBS_ELEC_CIRCUIT_WIRE_NUM_GROUNDS_PARAM=None
    RBS_ELEC_CIRCUIT_WIRE_NUM_HOTS_PARAM=None
    RBS_ELEC_CIRCUIT_WIRE_NUM_NEUTRALS_PARAM=None
    RBS_ELEC_CIRCUIT_WIRE_NUM_RUNS_PARAM=None
    RBS_ELEC_CIRCUIT_WIRE_SIZE_PARAM=None
    RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM=None
    RBS_ELEC_DEMANDFACTOR_DEMANDLOAD_PARAM=None
    RBS_ELEC_DEMANDFACTOR_LOADCLASSIFICATION_PARAM=None
    RBS_ELEC_DEMANDFACTOR_LOAD_PARAM=None
    RBS_ELEC_ENCLOSURE=None
    RBS_ELEC_LOADSUMMARY_CONNECTED_CURRENT_PARAM=None
    RBS_ELEC_LOADSUMMARY_CONNECTED_LOAD_PARAM=None
    RBS_ELEC_LOADSUMMARY_DEMAND_CURRENT_PARAM=None
    RBS_ELEC_LOADSUMMARY_DEMAND_FACTOR_PARAM=None
    RBS_ELEC_LOADSUMMARY_DEMAND_FACTOR_RULE_PARAM=None
    RBS_ELEC_LOADSUMMARY_DEMAND_LOAD_PARAM=None
    RBS_ELEC_LOADSUMMARY_LOADCLASSIFICATION_PARAM=None
    RBS_ELEC_LOAD_CLASSIFICATION=None
    RBS_ELEC_MAINS=None
    RBS_ELEC_MAX_POLE_BREAKERS=None
    RBS_ELEC_MODIFICATIONS=None
    RBS_ELEC_MOUNTING=None
    RBS_ELEC_NUMBER_OF_POLES=None
    RBS_ELEC_PANEL_BUSSING_PARAM=None
    RBS_ELEC_PANEL_CONFIGURATION_PARAM=None
    RBS_ELEC_PANEL_CURRENT_PHASEA_PARAM=None
    RBS_ELEC_PANEL_CURRENT_PHASEB_PARAM=None
    RBS_ELEC_PANEL_CURRENT_PHASEC_PARAM=None
    RBS_ELEC_PANEL_FEED_PARAM=None
    RBS_ELEC_PANEL_GROUND_BUS_PARAM=None
    RBS_ELEC_PANEL_LOCATION_PARAM=None
    RBS_ELEC_PANEL_MAINSTYPE_PARAM=None
    RBS_ELEC_PANEL_MCB_RATING_PARAM=None
    RBS_ELEC_PANEL_NAME=None
    RBS_ELEC_PANEL_NEUTRAL_BUS_PARAM=None
    RBS_ELEC_PANEL_NEUTRAL_RATING_PARAM=None
    RBS_ELEC_PANEL_NUMPHASES_PARAM=None
    RBS_ELEC_PANEL_NUMWIRES_PARAM=None
    RBS_ELEC_PANEL_SCHEDULE_FOOTER_NOTES_PARAM=None
    RBS_ELEC_PANEL_SCHEDULE_HEADER_NOTES_PARAM=None
    RBS_ELEC_PANEL_SUBFEED_LUGS_PARAM=None
    RBS_ELEC_PANEL_SUPPLY_FROM_PARAM=None
    RBS_ELEC_PANEL_TOTALESTLOAD_HVAC_PARAM=None
    RBS_ELEC_PANEL_TOTALESTLOAD_LIGHT_PARAM=None
    RBS_ELEC_PANEL_TOTALESTLOAD_OTHER_PARAM=None
    RBS_ELEC_PANEL_TOTALESTLOAD_PARAM=None
    RBS_ELEC_PANEL_TOTALESTLOAD_POWER_PARAM=None
    RBS_ELEC_PANEL_TOTALLOAD_HVAC_PARAM=None
    RBS_ELEC_PANEL_TOTALLOAD_LIGHT_PARAM=None
    RBS_ELEC_PANEL_TOTALLOAD_OTHER_PARAM=None
    RBS_ELEC_PANEL_TOTALLOAD_PARAM=None
    RBS_ELEC_PANEL_TOTALLOAD_POWER_PARAM=None
    RBS_ELEC_PANEL_TOTAL_CONNECTED_CURRENT_PARAM=None
    RBS_ELEC_PANEL_TOTAL_DEMAND_CURRENT_PARAM=None
    RBS_ELEC_PANEL_TOTAL_DEMAND_FACTOR_PARAM=None
    RBS_ELEC_POWER_FACTOR=None
    RBS_ELEC_POWER_FACTOR_STATE=None
    RBS_ELEC_ROOM_AVERAGE_ILLUMINATION=None
    RBS_ELEC_ROOM_CAVITY_RATIO=None
    RBS_ELEC_ROOM_LIGHTING_CALC_LUMINAIREPLANE=None
    RBS_ELEC_ROOM_LIGHTING_CALC_WORKPLANE=None
    RBS_ELEC_ROOM_REFLECTIVITY_CEILING=None
    RBS_ELEC_ROOM_REFLECTIVITY_FLOOR=None
    RBS_ELEC_ROOM_REFLECTIVITY_WALLS=None
    RBS_ELEC_SHORT_CIRCUIT_RATING=None
    RBS_ELEC_SWITCH_ID_PARAM=None
    RBS_ELEC_TRUE_CURRENT_PARAM=None
    RBS_ELEC_TRUE_CURRENT_PHASEA_PARAM=None
    RBS_ELEC_TRUE_CURRENT_PHASEB_PARAM=None
    RBS_ELEC_TRUE_CURRENT_PHASEC_PARAM=None
    RBS_ELEC_TRUE_LOAD=None
    RBS_ELEC_TRUE_LOAD_PHASE1=None
    RBS_ELEC_TRUE_LOAD_PHASE2=None
    RBS_ELEC_TRUE_LOAD_PHASE3=None
    RBS_ELEC_TRUE_LOAD_PHASEA=None
    RBS_ELEC_TRUE_LOAD_PHASEB=None
    RBS_ELEC_TRUE_LOAD_PHASEC=None
    RBS_ELEC_VOLTAGE=None
    RBS_ELEC_VOLTAGE_DROP_PARAM=None
    RBS_ELEC_WIRE_CIRCUITS=None
    RBS_ELEC_WIRE_ELEVATION=None
    RBS_ELEC_WIRE_GROUND_ADJUSTMENT=None
    RBS_ELEC_WIRE_HOT_ADJUSTMENT=None
    RBS_ELEC_WIRE_NEUTRAL_ADJUSTMENT=None
    RBS_ELEC_WIRE_SHARE_GROUND=None
    RBS_ELEC_WIRE_SHARE_NEUTRAL=None
    RBS_ELEC_WIRE_TICKMARK_STATE=None
    RBS_ELEC_WIRE_TYPE=None
    RBS_END_LEVEL_PARAM=None
    RBS_END_OFFSET_PARAM=None
    RBS_ENERGY_ANALYSIS_BUILDING_ENVELOPE_ANALYTICAL_GRID_CELL_SIZE=None
    RBS_ENERGY_ANALYSIS_BUILDING_ENVELOPE_ANALYTICAL_SPACE_INDENTIFICATION_RESOLUTION=None
    RBS_ENERGY_ANALYSIS_BUILDING_ENVELOPE_ANALYTICAL_SURFACE_INDENTIFICATION_RESOLUTION=None
    RBS_ENERGY_ANALYSIS_BUILDING_ENVELOPE_DETERMINATION_PARAM=None
    RBS_ENERGY_ANALYSIS_EXPORT_CATEGORY_PARAM=None
    RBS_ENERGY_ANALYSIS_EXPORT_COMPLEXITY_PARAM=None
    RBS_ENERGY_ANALYSIS_EXPORT_GBXML_DEFAULTS_PARAM=None
    RBS_ENERGY_ANALYSIS_GROUND_PLANE_PARAM=None
    RBS_ENERGY_ANALYSIS_INCLUDE_THERMAL_PROPERTIES=None
    RBS_ENERGY_ANALYSIS_MODE=None
    RBS_ENERGY_ANALYSIS_PROJECT_PHASE_PARAM=None
    RBS_ENERGY_ANALYSIS_SLIVER_SPACE_TOLERANCE=None
    RBS_ENERGY_ANALYSIS_SURFACE_ADJACENT_SPACE_ID1=None
    RBS_ENERGY_ANALYSIS_SURFACE_ADJACENT_SPACE_ID2=None
    RBS_ENERGY_ANALYSIS_SURFACE_AZIMUTH=None
    RBS_ENERGY_ANALYSIS_SURFACE_CADOBJECTID=None
    RBS_ENERGY_ANALYSIS_SURFACE_ORIGIN_X=None
    RBS_ENERGY_ANALYSIS_SURFACE_ORIGIN_Y=None
    RBS_ENERGY_ANALYSIS_SURFACE_ORIGIN_Z=None
    RBS_ENERGY_ANALYSIS_SURFACE_TILT=None
    RBS_ENERGY_ANALYSIS_VIEW_BUILDING_SHELL_MODE=None
    RBS_ENERGY_ANALYSIS_VIEW_COORD_AXIS_MODE=None
    RBS_ENERGY_ANALYSIS_VIEW_INNER_SHELL_MODE=None
    RBS_ENERGY_ANALYSIS_VIEW_OUTER_SHELL_MODE=None
    RBS_ENERGY_ANALYSIS_VIEW_RBE_MODE=None
    RBS_ENERGY_ANALYSIS_VIEW_SHADING_SURFACES_MODE=None
    RBS_ENERGY_ANALYSIS_VIEW_SURFACES_MODE=None
    RBS_ENERGY_ANALYSIS_VIEW_TRANSPARENT_MODE=None
    RBS_ENERGY_ANALYSIS_VIEW_UPDATE_SURFACES=None
    RBS_EQ_DIAMETER_PARAM=None
    RBS_FAMILY_CONTENT_ANNOTATION_DISPLAY=None
    RBS_FAMILY_CONTENT_DISTRIBUTION_SYSTEM=None
    RBS_FAMILY_CONTENT_OFFSET_HEIGHT=None
    RBS_FAMILY_CONTENT_OFFSET_WIDTH=None
    RBS_FAMILY_CONTENT_SECONDARY_DISTRIBSYS=None
    RBS_FAMILY_CONTENT_TAKEOFF_FIXED_LENGTH=None
    RBS_FAMILY_CONTENT_TAKEOFF_LENGTH=None
    RBS_FAMILY_CONTENT_TAKEOFF_PROJLENGTH=None
    RBS_FLEXDUCT_ROUNDTYPE_PARAM=None
    RBS_FLEX_DUCT_TYPE_PARAM=None
    RBS_FLEX_PATTERN_PARAM=None
    RBS_FLEX_PIPE_TYPE_PARAM=None
    RBS_FLOW_FACTOR_PARAM=None
    RBS_FLOW_OBSOLETE=None
    RBS_FP_SPRINKLER_COVERAGE_PARAM=None
    RBS_FP_SPRINKLER_K_FACTOR_PARAM=None
    RBS_FP_SPRINKLER_ORIFICE_PARAM=None
    RBS_FP_SPRINKLER_ORIFICE_SIZE_PARAM=None
    RBS_FP_SPRINKLER_PRESSURE_CLASS_PARAM=None
    RBS_FP_SPRINKLER_RESPONSE_PARAM=None
    RBS_FP_SPRINKLER_TEMPERATURE_RATING_PARAM=None
    RBS_FRICTION=None
    RBS_GBXML_OPENING_TYPE=None
    RBS_GBXML_SURFACE_AREA=None
    RBS_GBXML_SURFACE_NAME=None
    RBS_GBXML_SURFACE_TYPE=None
    RBS_HVACLOAD_DOOR_AREA_PARAM=None
    RBS_HVACLOAD_DOOR_COOLING_LOAD_PARAM=None
    RBS_HVACLOAD_FLOOR_AREA_PARAM=None
    RBS_HVACLOAD_PARTITION_AREA_PARAM=None
    RBS_HVACLOAD_PARTITION_COOLING_LOAD_PARAM=None
    RBS_HVACLOAD_PLENUM_COOLING_LOAD_PARAM=None
    RBS_HVACLOAD_ROOF_AREA_PARAM=None
    RBS_HVACLOAD_ROOF_COOLING_LOAD_PARAM=None
    RBS_HVACLOAD_SKYLIGHT_AREA_PARAM=None
    RBS_HVACLOAD_SKYLIGHT_COOLING_LOAD_PARAM=None
    RBS_HVACLOAD_WALL_AREA_PARAM=None
    RBS_HVACLOAD_WALL_COOLING_LOAD_PARAM=None
    RBS_HVACLOAD_WINDOW_AREA_PARAM=None
    RBS_HVACLOAD_WINDOW_COOLING_LOAD_PARAM=None
    RBS_HYDRAULIC_DIAMETER_PARAM=None
    RBS_INSULATION_LINING_VOLUME=None
    RBS_INSULATION_THICKNESS=None
    RBS_INSULATION_THICKNESS_FOR_DUCT=None
    RBS_INSULATION_THICKNESS_FOR_PIPE=None
    RBS_IS_CUSTOM_FITTING=None
    RBS_LINING_THICKNESS=None
    RBS_LINING_THICKNESS_FOR_DUCT=None
    RBS_LOAD_SUB_CLASSIFICATION_MOTOR=None
    RBS_LOOKUP_TABLE_NAME=None
    RBS_LOSS_COEFFICIENT=None
    RBS_MAX_FLOW=None
    RBS_MIN_FLOW=None
    RBS_OFFSET_PARAM=None
    RBS_PANEL_SCHEDULE_SHEET_APPEARANCE_INST_PARAM=None
    RBS_PANEL_SCHEDULE_SHEET_APPEARANCE_PARAM=None
    RBS_PARALLELCONDUITS_HORIZONTAL_NUMBER=None
    RBS_PARALLELCONDUITS_HORIZONTAL_OFFSET_VALUE=None
    RBS_PARALLELCONDUITS_VERTICAL_NUMBER=None
    RBS_PARALLELCONDUITS_VERTICAL_OFFSET_VALUE=None
    RBS_PARALLELPIPES_HORIZONTAL_NUMBER=None
    RBS_PARALLELPIPES_HORIZONTAL_OFFSET_VALUE=None
    RBS_PARALLELPIPES_VERTICAL_NUMBER=None
    RBS_PARALLELPIPES_VERTICAL_OFFSET_VALUE=None
    RBS_PART_TYPE=None
    RBS_PIPE_ADDITIONAL_FLOW_PARAM=None
    RBS_PIPE_CALCULATED_SIZE=None
    RBS_PIPE_CLASS_PARAM=None
    RBS_PIPE_CONNECTIONTYPE_PARAM=None
    RBS_PIPE_CONNECTOR_SYSTEM_CLASSIFICATION_PARAM=None
    RBS_PIPE_CWFU_PARAM=None
    RBS_PIPE_DIAMETER_PARAM=None
    RBS_PIPE_FITTING_LOSS_KFACTOR_PARAM=None
    RBS_PIPE_FITTING_LOSS_METHOD_PARAM=None
    RBS_PIPE_FITTING_LOSS_METHOD_SERVER_PARAM=None
    RBS_PIPE_FITTING_LOSS_METHOD_SETTINGS=None
    RBS_PIPE_FITTING_LOSS_TABLE_PARAM=None
    RBS_PIPE_FIXTURE_UNITS_PARAM=None
    RBS_PIPE_FLOW_CONFIGURATION_PARAM=None
    RBS_PIPE_FLOW_DIRECTION_PARAM=None
    RBS_PIPE_FLOW_PARAM=None
    RBS_PIPE_FLOW_STATE_PARAM=None
    RBS_PIPE_FLUID_DENSITY_PARAM=None
    RBS_PIPE_FLUID_TEMPERATURE_PARAM=None
    RBS_PIPE_FLUID_TYPE_PARAM=None
    RBS_PIPE_FLUID_VISCOSITY_PARAM=None
    RBS_PIPE_FRICTION_FACTOR_PARAM=None
    RBS_PIPE_FRICTION_PARAM=None
    RBS_PIPE_HWFU_PARAM=None
    RBS_PIPE_INNER_DIAM_PARAM=None
    RBS_PIPE_INSULATION_THICKNESS=None
    RBS_PIPE_INVERT_ELEVATION=None
    RBS_PIPE_JOINTTYPE_PARAM=None
    RBS_PIPE_MATERIAL_PARAM=None
    RBS_PIPE_OUTER_DIAMETER=None
    RBS_PIPE_PRESSUREDROP_PARAM=None
    RBS_PIPE_RELATIVE_ROUGHNESS_PARAM=None
    RBS_PIPE_REYNOLDS_NUMBER_PARAM=None
    RBS_PIPE_ROUGHNESS_PARAM=None
    RBS_PIPE_SEGMENT_PARAM=None
    RBS_PIPE_SIZE_FORMATTED_PARAM=None
    RBS_PIPE_SIZE_MAXIMUM=None
    RBS_PIPE_SIZE_MINIMUM=None
    RBS_PIPE_SLOPE=None
    RBS_PIPE_SLOPE_DEF_PARAM=None
    RBS_PIPE_STATIC_PRESSURE=None
    RBS_PIPE_SYSTEM_CALCULATION_PARAM=None
    RBS_PIPE_SYSTEM_FIXTURE_UNIT_PARAM=None
    RBS_PIPE_TYPE_FITTING_LOSS_KFACTOR_PARAM=None
    RBS_PIPE_TYPE_FITTING_LOSS_METHOD_PARAM=None
    RBS_PIPE_TYPE_FITTING_LOSS_TABLE_PARAM=None
    RBS_PIPE_TYPE_PARAM=None
    RBS_PIPE_TYPE_VALVE_LOSS_CVFACTOR_PARAM=None
    RBS_PIPE_VALVE_LOSS_CVFACTOR_PARAM=None
    RBS_PIPE_VELOCITY_PARAM=None
    RBS_PIPE_VOLUME_PARAM=None
    RBS_PIPE_WFU_PARAM=None
    RBS_PIPING_SYSTEM_TYPE_PARAM=None
    RBS_PRESSURE_DROP=None
    RBS_PROJECT_CONSTRUCTION_TYPE_SHADINGFACTOR_PARAM=None
    RBS_PROJECT_LOCATION_PARAM=None
    RBS_PROJECT_REPORTTYPE_PARAM=None
    RBS_REFERENCE_FREESIZE=None
    RBS_REFERENCE_INSULATION_THICKNESS=None
    RBS_REFERENCE_INSULATION_TYPE=None
    RBS_REFERENCE_LINING_THICKNESS=None
    RBS_REFERENCE_LINING_TYPE=None
    RBS_REFERENCE_OVERALLSIZE=None
    RBS_REYNOLDSNUMBER_PARAM=None
    RBS_ROOM_COEFFICIENT_UTILIZATION=None
    RBS_ROUTING_PREFERENCE_PARAM=None
    RBS_SECTION=None
    RBS_SEGMENT_DESCRIPTION_PARAM=None
    RBS_SERVICE_TYPE_PARAM=None
    RBS_SHOW_PROFILE_TYPE=None
    RBS_SIZE_LOCK=None
    RBS_START_LEVEL_PARAM=None
    RBS_START_OFFSET_PARAM=None
    RBS_SYSTEM_ABBREVIATION_PARAM=None
    RBS_SYSTEM_BASE_ELEMENT_PARAM=None
    RBS_SYSTEM_CLASSIFICATION_PARAM=None
    RBS_SYSTEM_FLOW_CONVERSION_METHOD_PARAM=None
    RBS_SYSTEM_NAME_PARAM=None
    RBS_SYSTEM_NUM_ELEMENTS_PARAM=None
    RBS_SYSTEM_OVERRIDE_GRAPHICS_PARAM=None
    RBS_SYSTEM_RISEDROP_1LINEDROPSYMBOL_PARAM=None
    RBS_SYSTEM_RISEDROP_1LINERISESYMBOL_PARAM=None
    RBS_SYSTEM_RISEDROP_1LINETEEDOWNSYMBOL_PARAM=None
    RBS_SYSTEM_RISEDROP_1LINETEEUPSYMBOL_PARAM=None
    RBS_SYSTEM_RISEDROP_2LINEDROPSYMBOL_PARAM=None
    RBS_SYSTEM_RISEDROP_2LINERISESYMBOL_PARAM=None
    RBS_SYSTEM_RISEDROP_PARAM=None
    RBS_VELOCITY=None
    RBS_VELOCITY_PRESSURE=None
    RBS_VOLTAGETYPE_MAXVOLTAGE_PARAM=None
    RBS_VOLTAGETYPE_MINVOLTAGE_PARAM=None
    RBS_VOLTAGETYPE_VOLTAGE_PARAM=None
    RBS_WIRE_CIRCUIT_DESCRIPTION=None
    RBS_WIRE_CIRCUIT_LOAD_NAME=None
    RBS_WIRE_CONDUIT_TYPE_PARAM=None
    RBS_WIRE_INSULATION_PARAM=None
    RBS_WIRE_MATERIAL_PARAM=None
    RBS_WIRE_MAX_CONDUCTOR_SIZE_PARAM=None
    RBS_WIRE_NEUTRAL_INCLUDED_IN_BALANCED_LOAD_PARAM=None
    RBS_WIRE_NEUTRAL_MODE_PARAM=None
    RBS_WIRE_NEUTRAL_MULTIPLIER_PARAM=None
    RBS_WIRE_NUM_CONDUCTORS_PARAM=None
    RBS_WIRE_TEMPERATURE_RATING_PARAM=None
    REBAR_BAR_ALLOWED_BAR_TYPES=None
    REBAR_BAR_DEFORMATION_TYPE=None
    REBAR_BAR_DIAMETER=None
    REBAR_BAR_HOOK_LENGTHS=None
    REBAR_BAR_MAXIMUM_BEND_RADIUS=None
    REBAR_BAR_STIRRUP_BEND_DIAMETER=None
    REBAR_BAR_STYLE=None
    REBAR_CONTAINER_BAR_TYPE=None
    REBAR_DISTRIBUTION_TYPE=None
    REBAR_ELEMENT_ROUNDING=None
    REBAR_ELEMENT_VISIBILITY=None
    REBAR_ELEM_BAR_SPACING=None
    REBAR_ELEM_ENDTREATMENT_END=None
    REBAR_ELEM_ENDTREATMENT_START=None
    REBAR_ELEM_HOOK_END_ORIENT=None
    REBAR_ELEM_HOOK_END_TYPE=None
    REBAR_ELEM_HOOK_START_ORIENT=None
    REBAR_ELEM_HOOK_START_TYPE=None
    REBAR_ELEM_HOOK_STYLE=None
    REBAR_ELEM_HOST_MARK=None
    REBAR_ELEM_LAYOUT_RULE=None
    REBAR_ELEM_LENGTH=None
    REBAR_ELEM_QUANTITY_OF_BARS=None
    REBAR_ELEM_SCHEDULE_MARK=None
    REBAR_ELEM_TOTAL_LENGTH=None
    REBAR_HOOK_ANGLE=None
    REBAR_HOOK_LINE_LEN_FACTOR=None
    REBAR_HOOK_STYLE=None
    REBAR_HOST_CATEGORY=None
    REBAR_INCLUDE_FIRST_BAR=None
    REBAR_INCLUDE_LAST_BAR=None
    REBAR_INSTANCE_BAR_DIAMETER=None
    REBAR_INSTANCE_BEND_DIAMETER=None
    REBAR_INSTANCE_STIRRUP_TIE_ATTACHMENT=None
    REBAR_INTERNAL_MULTIPLANAR=None
    REBAR_INTERNAL_MULTIPLANAR_DUPLICATE=None
    REBAR_INTERNAL_MULTIPLANAR_END_CONNECTOR=None
    REBAR_INTERNAL_MULTIPLANAR_START_CONNECTOR=None
    REBAR_MAXIM_SUFFIX=None
    REBAR_MAX_LENGTH=None
    REBAR_MINIM_SUFFIX=None
    REBAR_MIN_LENGTH=None
    REBAR_NUMBER=None
    REBAR_NUMBER_SUFFIX=None
    REBAR_QUANITY_BY_DISTRIB=None
    REBAR_SHAPE=None
    REBAR_SHAPE_ALLOWED_BAR_TYPES=None
    REBAR_SHAPE_ENDTREATMENT_END_TYPE=None
    REBAR_SHAPE_ENDTREATMENT_START_TYPE=None
    REBAR_SHAPE_END_HOOK_LENGTH=None
    REBAR_SHAPE_END_HOOK_OFFSET=None
    REBAR_SHAPE_HOOK_END_TYPE=None
    REBAR_SHAPE_HOOK_START_TYPE=None
    REBAR_SHAPE_HOOK_STYLE=None
    REBAR_SHAPE_IMAGE=None
    REBAR_SHAPE_OUT_OF_PLANE_BEND_DIAMETER=None
    REBAR_SHAPE_PARAM_END_HOOK_TAN_LEN=None
    REBAR_SHAPE_PARAM_START_HOOK_TAN_LEN=None
    REBAR_SHAPE_SPIRAL_BASE_FINISHING_TURNS=None
    REBAR_SHAPE_SPIRAL_HEIGHT=None
    REBAR_SHAPE_SPIRAL_PITCH=None
    REBAR_SHAPE_SPIRAL_TOP_FINISHING_TURNS=None
    REBAR_SHAPE_START_HOOK_LENGTH=None
    REBAR_SHAPE_START_HOOK_OFFSET=None
    REBAR_SHAPE_STIRRUP_TIE_ATTACHMENT=None
    REBAR_STANDARD_BEND_DIAMETER=None
    REBAR_STANDARD_HOOK_BEND_DIAMETER=None
    REBAR_SYSTEM_ACTIVE_BACK_DIR_1=None
    REBAR_SYSTEM_ACTIVE_BACK_DIR_2=None
    REBAR_SYSTEM_ACTIVE_BOTTOM_DIR_1=None
    REBAR_SYSTEM_ACTIVE_BOTTOM_DIR_1_GENERIC=None
    REBAR_SYSTEM_ACTIVE_BOTTOM_DIR_2=None
    REBAR_SYSTEM_ACTIVE_BOTTOM_DIR_2_GENERIC=None
    REBAR_SYSTEM_ACTIVE_FRONT_DIR_1=None
    REBAR_SYSTEM_ACTIVE_FRONT_DIR_2=None
    REBAR_SYSTEM_ACTIVE_TOP_DIR_1=None
    REBAR_SYSTEM_ACTIVE_TOP_DIR_1_GENERIC=None
    REBAR_SYSTEM_ACTIVE_TOP_DIR_2=None
    REBAR_SYSTEM_ACTIVE_TOP_DIR_2_GENERIC=None
    REBAR_SYSTEM_ADDL_BOTTOM_OFFSET=None
    REBAR_SYSTEM_ADDL_EXTERIOR_OFFSET=None
    REBAR_SYSTEM_ADDL_INTERIOR_OFFSET=None
    REBAR_SYSTEM_ADDL_TOP_OFFSET=None
    REBAR_SYSTEM_BAR_TYPE_BACK_DIR_1=None
    REBAR_SYSTEM_BAR_TYPE_BACK_DIR_2=None
    REBAR_SYSTEM_BAR_TYPE_BOTTOM_DIR_1=None
    REBAR_SYSTEM_BAR_TYPE_BOTTOM_DIR_1_GENERIC=None
    REBAR_SYSTEM_BAR_TYPE_BOTTOM_DIR_2=None
    REBAR_SYSTEM_BAR_TYPE_BOTTOM_DIR_2_GENERIC=None
    REBAR_SYSTEM_BAR_TYPE_FRONT_DIR_1=None
    REBAR_SYSTEM_BAR_TYPE_FRONT_DIR_2=None
    REBAR_SYSTEM_BAR_TYPE_TOP_DIR_1=None
    REBAR_SYSTEM_BAR_TYPE_TOP_DIR_1_GENERIC=None
    REBAR_SYSTEM_BAR_TYPE_TOP_DIR_2=None
    REBAR_SYSTEM_BAR_TYPE_TOP_DIR_2_GENERIC=None
    REBAR_SYSTEM_BOTTOM_MAJOR_MATCHES_BOTTOM_MINOR=None
    REBAR_SYSTEM_COVER_BOTTOM=None
    REBAR_SYSTEM_COVER_SIDE=None
    REBAR_SYSTEM_COVER_TOP=None
    REBAR_SYSTEM_HOOK_ORIENT_BACK_DIR_1=None
    REBAR_SYSTEM_HOOK_ORIENT_BACK_DIR_2=None
    REBAR_SYSTEM_HOOK_ORIENT_BOTTOM_DIR_1=None
    REBAR_SYSTEM_HOOK_ORIENT_BOTTOM_DIR_2=None
    REBAR_SYSTEM_HOOK_ORIENT_FRONT_DIR_1=None
    REBAR_SYSTEM_HOOK_ORIENT_FRONT_DIR_2=None
    REBAR_SYSTEM_HOOK_ORIENT_TOP_DIR_1=None
    REBAR_SYSTEM_HOOK_ORIENT_TOP_DIR_2=None
    REBAR_SYSTEM_HOOK_TYPE_BACK_DIR_1=None
    REBAR_SYSTEM_HOOK_TYPE_BACK_DIR_2=None
    REBAR_SYSTEM_HOOK_TYPE_BOTTOM_DIR_1=None
    REBAR_SYSTEM_HOOK_TYPE_BOTTOM_DIR_2=None
    REBAR_SYSTEM_HOOK_TYPE_FRONT_DIR_1=None
    REBAR_SYSTEM_HOOK_TYPE_FRONT_DIR_2=None
    REBAR_SYSTEM_HOOK_TYPE_TOP_DIR_1=None
    REBAR_SYSTEM_HOOK_TYPE_TOP_DIR_2=None
    REBAR_SYSTEM_LAYER_SUMMARY_BOTTOM_DIR_1_NO_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_BOTTOM_DIR_1_WITH_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_BOTTOM_DIR_2_NO_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_BOTTOM_DIR_2_WITH_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_DIR_1_NO_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_DIR_1_WITH_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_DIR_2_NO_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_DIR_2_WITH_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_NO_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_TOP_DIR_1_NO_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_TOP_DIR_1_WITH_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_TOP_DIR_2_NO_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_TOP_DIR_2_WITH_SPACING=None
    REBAR_SYSTEM_LAYER_SUMMARY_WITH_SPACING=None
    REBAR_SYSTEM_LAYOUT_RULE=None
    REBAR_SYSTEM_NUMBER_OF_LINES_BACK_DIR_1=None
    REBAR_SYSTEM_NUMBER_OF_LINES_BACK_DIR_2=None
    REBAR_SYSTEM_NUMBER_OF_LINES_BOTTOM_DIR_1=None
    REBAR_SYSTEM_NUMBER_OF_LINES_BOTTOM_DIR_1_GENERIC=None
    REBAR_SYSTEM_NUMBER_OF_LINES_BOTTOM_DIR_2=None
    REBAR_SYSTEM_NUMBER_OF_LINES_BOTTOM_DIR_2_GENERIC=None
    REBAR_SYSTEM_NUMBER_OF_LINES_FRONT_DIR_1=None
    REBAR_SYSTEM_NUMBER_OF_LINES_FRONT_DIR_2=None
    REBAR_SYSTEM_NUMBER_OF_LINES_TOP_DIR_1=None
    REBAR_SYSTEM_NUMBER_OF_LINES_TOP_DIR_1_GENERIC=None
    REBAR_SYSTEM_NUMBER_OF_LINES_TOP_DIR_2=None
    REBAR_SYSTEM_NUMBER_OF_LINES_TOP_DIR_2_GENERIC=None
    REBAR_SYSTEM_OVERRIDE=None
    REBAR_SYSTEM_SPACING_BACK_DIR_1=None
    REBAR_SYSTEM_SPACING_BACK_DIR_2=None
    REBAR_SYSTEM_SPACING_BOTTOM_DIR_1=None
    REBAR_SYSTEM_SPACING_BOTTOM_DIR_1_GENERIC=None
    REBAR_SYSTEM_SPACING_BOTTOM_DIR_2=None
    REBAR_SYSTEM_SPACING_BOTTOM_DIR_2_GENERIC=None
    REBAR_SYSTEM_SPACING_FRONT_DIR_1=None
    REBAR_SYSTEM_SPACING_FRONT_DIR_2=None
    REBAR_SYSTEM_SPACING_TOP_DIR_1=None
    REBAR_SYSTEM_SPACING_TOP_DIR_1_GENERIC=None
    REBAR_SYSTEM_SPACING_TOP_DIR_2=None
    REBAR_SYSTEM_SPACING_TOP_DIR_2_GENERIC=None
    REBAR_SYSTEM_SPANACTIVE_DIR_1=None
    REBAR_SYSTEM_SPANACTIVE_DIR_2=None
    REBAR_SYSTEM_SPANHOOK_BOTTOM_DIR_2=None
    REBAR_SYSTEM_SPANHOOK_LEFT_DIR_1=None
    REBAR_SYSTEM_SPANHOOK_RIGHT_DIR_1=None
    REBAR_SYSTEM_SPANHOOK_TOP_DIR_2=None
    REBAR_SYSTEM_TOP_MAJOR_MATCHES_BOTTOM_MAJOR=None
    REBAR_SYSTEM_TOP_MAJOR_MATCHES_TOP_MINOR=None
    REBAR_SYSTEM_TOP_MINOR_MATCHES_BOTTOM_MINOR=None
    RECT_MULLION_THICK=None
    RECT_MULLION_WIDTH1=None
    RECT_MULLION_WIDTH2=None
    REFERENCED_VIEW=None
    REFERENCE_OTHER_VIEW_UI_REF_VIEW=None
    REFERENCE_OTHER_VIEW_UI_TOGGLE=None
    REFERENCE_VIEWER_ATTR_TAG=None
    REFERENCE_VIEWER_TARGET_VIEW=None
    REFERENCE_VIEWER_UI_TARGET_FILTER=None
    REFERENCE_VIEWER_UI_TARGET_VIEW=None
    REF_TABLE_ELEM_NAME=None
    REF_TABLE_PARAM_NAME=None
    REINFORCEMENT_VOLUME=None
    REIN_EST_BAR_LENGTH=None
    REIN_EST_BAR_VOLUME=None
    REIN_EST_NUMBER_OF_BARS=None
    RELATED_TO_MASS=None
    RENDER_PLANT_HEIGHT=None
    RENDER_PLANT_NAME=None
    RENDER_PLANT_TRIM_HEIGHT=None
    RENDER_RPC_FILENAME=None
    RENDER_RPC_PROPERTIES=None
    REPEATING_DETAIL_ELEMENT=None
    REPEATING_DETAIL_INSIDE=None
    REPEATING_DETAIL_LAYOUT=None
    REPEATING_DETAIL_NUMBER=None
    REPEATING_DETAIL_ROTATION=None
    REPEATING_DETAIL_SPACING=None
    REVEAL_PROFILE_PARAM=None
    REVISION_CLOUD_REVISION=None
    REVISION_CLOUD_REVISION_DATE=None
    REVISION_CLOUD_REVISION_DESCRIPTION=None
    REVISION_CLOUD_REVISION_ISSUED_BY=None
    REVISION_CLOUD_REVISION_ISSUED_TO=None
    REVISION_CLOUD_REVISION_NUM=None
    REVOLUTION_END_ANGLE=None
    REVOLUTION_START_ANGLE=None
    RGB_B_PARAM=None
    RGB_G_PARAM=None
    RGB_R_PARAM=None
    ROOF_ATTR_DEFAULT_THICKNESS_PARAM=None
    ROOF_ATTR_THICKNESS_PARAM=None
    ROOF_BASE_LEVEL_PARAM=None
    ROOF_CONSTRAINT_LEVEL_PARAM=None
    ROOF_CONSTRAINT_OFFSET_PARAM=None
    ROOF_CURVE_HEIGHT_AT_WALL=None
    ROOF_CURVE_HEIGHT_OFFSET=None
    ROOF_CURVE_IS_SLOPE_DEFINING=None
    ROOF_EAVE_CUT_PARAM=None
    ROOF_FACES_LOCATION=None
    ROOF_LEVEL_OFFSET_PARAM=None
    ROOF_RAFTER_OR_TRUSS_PARAM=None
    ROOF_SLOPE=None
    ROOF_STRUCTURE_ID_PARAM=None
    ROOF_UPTO_LEVEL_OFFSET_PARAM=None
    ROOF_UPTO_LEVEL_PARAM=None
    ROOM_ACTUAL_EXHAUST_AIRFLOW_PARAM=None
    ROOM_ACTUAL_LIGHTING_LOAD_PARAM=None
    ROOM_ACTUAL_LIGHTING_LOAD_PER_AREA_PARAM=None
    ROOM_ACTUAL_POWER_LOAD_PARAM=None
    ROOM_ACTUAL_POWER_LOAD_PER_AREA_PARAM=None
    ROOM_ACTUAL_RETURN_AIRFLOW_PARAM=None
    ROOM_ACTUAL_SUPPLY_AIRFLOW_PARAM=None
    ROOM_AREA=None
    ROOM_AREA_PER_PERSON_PARAM=None
    ROOM_BASE_HEAT_LOAD_ON_PARAM=None
    ROOM_BASE_LIGHTING_LOAD_ON_PARAM=None
    ROOM_BASE_POWER_LOAD_ON_PARAM=None
    ROOM_BASE_RETURN_AIRFLOW_ON_PARAM=None
    ROOM_CALCULATED_COOLING_LOAD_PARAM=None
    ROOM_CALCULATED_COOLING_LOAD_PER_AREA_PARAM=None
    ROOM_CALCULATED_HEATING_LOAD_PARAM=None
    ROOM_CALCULATED_HEATING_LOAD_PER_AREA_PARAM=None
    ROOM_CALCULATED_SUPPLY_AIRFLOW_PARAM=None
    ROOM_CALCULATED_SUPPLY_AIRFLOW_PER_AREA_PARAM=None
    ROOM_CALCULATION_POINT=None
    ROOM_COMPUTATION_HEIGHT=None
    ROOM_COMPUTATION_METHOD=None
    ROOM_CONDITION_TYPE_PARAM=None
    ROOM_CONSTRUCTION_SET_PARAM=None
    ROOM_DEPARTMENT=None
    ROOM_DESIGN_COOLING_LOAD_PARAM=None
    ROOM_DESIGN_EXHAUST_AIRFLOW_PARAM=None
    ROOM_DESIGN_HEATING_LOAD_PARAM=None
    ROOM_DESIGN_LIGHTING_LOAD_PARAM=None
    ROOM_DESIGN_LIGHTING_LOAD_PER_AREA_PARAM=None
    ROOM_DESIGN_MECHANICAL_LOAD_PER_AREA_PARAM=None
    ROOM_DESIGN_OTHER_LOAD_PER_AREA_PARAM=None
    ROOM_DESIGN_POWER_LOAD_PARAM=None
    ROOM_DESIGN_POWER_LOAD_PER_AREA_PARAM=None
    ROOM_DESIGN_RETURN_AIRFLOW_PARAM=None
    ROOM_DESIGN_SUPPLY_AIRFLOW_PARAM=None
    ROOM_EDIT_ELECTRICAL_LOADS_PARAM=None
    ROOM_EDIT_PEOPLE_LOADS_PARAM=None
    ROOM_FINISH_BASE=None
    ROOM_FINISH_CEILING=None
    ROOM_FINISH_FLOOR=None
    ROOM_FINISH_WALL=None
    ROOM_HEIGHT=None
    ROOM_LEVEL_ID=None
    ROOM_LIGHTING_LOAD_UNITS_PARAM=None
    ROOM_LOWER_OFFSET=None
    ROOM_NAME=None
    ROOM_NUMBER=None
    ROOM_NUMBER_OF_PEOPLE_PARAM=None
    ROOM_OCCUPANCY=None
    ROOM_OCCUPANCY_UNIT_PARAM=None
    ROOM_PEOPLE_LATENT_HEAT_GAIN_PER_PERSON_PARAM=None
    ROOM_PEOPLE_SENSIBLE_HEAT_GAIN_PER_PERSON_PARAM=None
    ROOM_PEOPLE_TOTAL_HEAT_GAIN_PER_PERSON_PARAM=None
    ROOM_PERIMETER=None
    ROOM_PHASE=None
    ROOM_PHASE_ID=None
    ROOM_PLENUM_LIGHTING_PARAM=None
    ROOM_POWER_LOAD_UNITS_PARAM=None
    ROOM_SPACE_TYPE_PARAM=None
    ROOM_TAG_ORIENTATION_PARAM=None
    ROOM_UPPER_LEVEL=None
    ROOM_UPPER_OFFSET=None
    ROOM_VOLUME=None
    ROUTING_PREFERENCE_PARAM=None
    RVT_HOST_LEVEL=None
    RVT_LEVEL_OFFSET=None
    RVT_LINK_FILE_NAME_WITHOUT_EXT=None
    RVT_LINK_INSTANCE_NAME=None
    RVT_LINK_PHASE_MAP=None
    RVT_LINK_REFERENCE_TYPE=None
    RVT_SOURCE_LEVEL=None
    SCHEDULE_BASE_LEVEL_OFFSET_PARAM=None
    SCHEDULE_BASE_LEVEL_PARAM=None
    SCHEDULE_EMBEDDED_PARAM=None
    SCHEDULE_FIELDS_PARAM=None
    SCHEDULE_FILTER_PARAM=None
    SCHEDULE_FORMAT_PARAM=None
    SCHEDULE_GROUP_PARAM=None
    SCHEDULE_LEVEL_PARAM=None
    SCHEDULE_SHEET_APPEARANCE_PARAM=None
    SCHEDULE_TOP_LEVEL_OFFSET_PARAM=None
    SCHEDULE_TOP_LEVEL_PARAM=None
    SECTION_ATTR_HEAD_TAG=None
    SECTION_ATTR_TAIL_LENGTH=None
    SECTION_ATTR_TAIL_TAG=None
    SECTION_ATTR_TAIL_WIDTH=None
    SECTION_BROKEN_DISPLAY_STYLE=None
    SECTION_COARSER_SCALE_PULLDOWN_IMPERIAL=None
    SECTION_COARSER_SCALE_PULLDOWN_METRIC=None
    SECTION_PARENT_VIEW_NAME=None
    SECTION_SHOW_IN_ONE_VIEW_ONLY=None
    SECTION_TAG=None
    SEEK_ITEM_ID=None
    SHEET_APPROVED_BY=None
    SHEET_ASSEMBLY_ASSEMBLY_CODE=None
    SHEET_ASSEMBLY_ASSEMBLY_DESCRIPTION=None
    SHEET_ASSEMBLY_COST=None
    SHEET_ASSEMBLY_DESCRIPTION=None
    SHEET_ASSEMBLY_KEYNOTE=None
    SHEET_ASSEMBLY_MANUFACTURER=None
    SHEET_ASSEMBLY_MODEL=None
    SHEET_ASSEMBLY_NAME=None
    SHEET_ASSEMBLY_TYPE_COMMENTS=None
    SHEET_ASSEMBLY_TYPE_MARK=None
    SHEET_ASSEMBLY_URL=None
    SHEET_CHECKED_BY=None
    SHEET_CURRENT_REVISION=None
    SHEET_CURRENT_REVISION_DATE=None
    SHEET_CURRENT_REVISION_DESCRIPTION=None
    SHEET_CURRENT_REVISION_ISSUED=None
    SHEET_CURRENT_REVISION_ISSUED_BY=None
    SHEET_CURRENT_REVISION_ISSUED_TO=None
    SHEET_DATE=None
    SHEET_DESIGNED_BY=None
    SHEET_DRAWN_BY=None
    SHEET_FILE_PATH=None
    SHEET_GUIDE_GRID=None
    SHEET_HEIGHT=None
    SHEET_ISSUE_DATE=None
    SHEET_KEY_NUMBER=None
    SHEET_NAME=None
    SHEET_NUMBER=None
    SHEET_REVISIONS_ON_SHEET=None
    SHEET_SCALE=None
    SHEET_SCHEDULED=None
    SHEET_WIDTH=None
    SHOW_ARROWHEAD_TO_CUT_MARK=None
    SHOW_ICON_PARAM=None
    SHOW_TITLE=None
    SKETCH_GRID_SPACING_PARAM=None
    SKETCH_PLANE_PARAM=None
    SLAB_EDGE_MATERIAL_PARAM=None
    SLAB_EDGE_PROFILE_PARAM=None
    SLANTED_COLUMN_BASE_CUT_STYLE=None
    SLANTED_COLUMN_BASE_EXTENSION=None
    SLANTED_COLUMN_GEOMETRY_TREATMENT_BASE=None
    SLANTED_COLUMN_GEOMETRY_TREATMENT_TOP=None
    SLANTED_COLUMN_TOP_CUT_STYLE=None
    SLANTED_COLUMN_TOP_EXTENSION=None
    SLANTED_COLUMN_TYPE_PARAM=None
    SLOPE_ARROW_LEVEL_END=None
    SLOPE_ARROW_LEVEL_START=None
    SLOPE_END_HEIGHT=None
    SLOPE_START_HEIGHT=None
    SPACE_ASSOC_ROOM_NAME=None
    SPACE_ASSOC_ROOM_NUMBER=None
    SPACE_CARPETING_PARAM=None
    SPACE_ELEC_EQUIPMENT_RADIANT_PERCENTAGE_PARAM=None
    SPACE_INFILTRATION_PARAM=None
    SPACE_IS_OCCUPIABLE=None
    SPACE_IS_PLENUM=None
    SPACE_LIGHTING_SCHEDULE_PARAM=None
    SPACE_OCCUPANCY_SCHEDULE_PARAM=None
    SPACE_PEOPLE_ACTIVITY_LEVEL_PARAM=None
    SPACE_POWER_SCHEDULE_PARAM=None
    SPACE_ZONE_NAME=None
    SPACING_APPEND=None
    SPACING_JUSTIFICATION=None
    SPACING_JUSTIFICATION_1=None
    SPACING_JUSTIFICATION_2=None
    SPACING_JUSTIFICATION_HORIZ=None
    SPACING_JUSTIFICATION_U=None
    SPACING_JUSTIFICATION_V=None
    SPACING_JUSTIFICATION_VERT=None
    SPACING_LAYOUT=None
    SPACING_LAYOUT_1=None
    SPACING_LAYOUT_2=None
    SPACING_LAYOUT_HORIZ=None
    SPACING_LAYOUT_U=None
    SPACING_LAYOUT_V=None
    SPACING_LAYOUT_VERT=None
    SPACING_LENGTH=None
    SPACING_LENGTH_1=None
    SPACING_LENGTH_2=None
    SPACING_LENGTH_HORIZ=None
    SPACING_LENGTH_U=None
    SPACING_LENGTH_V=None
    SPACING_LENGTH_VERT=None
    SPACING_NUM_DIVISIONS=None
    SPACING_NUM_DIVISIONS_1=None
    SPACING_NUM_DIVISIONS_2=None
    SPACING_NUM_DIVISIONS_HORIZ=None
    SPACING_NUM_DIVISIONS_U=None
    SPACING_NUM_DIVISIONS_V=None
    SPACING_NUM_DIVISIONS_VERT=None
    SPAN_DIR_INST_PARAM_ANGLE=None
    SPAN_DIR_SYM_PARAM_BOTTOM=None
    SPAN_DIR_SYM_PARAM_LEFT=None
    SPAN_DIR_SYM_PARAM_RIGHT=None
    SPAN_DIR_SYM_PARAM_TOP=None
    SPATIAL_FIELD_MGR_CURRENT_NAME=None
    SPATIAL_FIELD_MGR_DESCRIPTION=None
    SPATIAL_FIELD_MGR_LEGEND_HEIGHT=None
    SPATIAL_FIELD_MGR_LEGEND_HOR_ORIGIN_GAP=None
    SPATIAL_FIELD_MGR_LEGEND_SHOW_CONFIG_NAME=None
    SPATIAL_FIELD_MGR_LEGEND_SHOW_DESCRIPTION=None
    SPATIAL_FIELD_MGR_LEGEND_TEXT_TYPE=None
    SPATIAL_FIELD_MGR_LEGEND_VERT_ORIGIN_GAP=None
    SPATIAL_FIELD_MGR_LEGEND_WIDTH=None
    SPATIAL_FIELD_MGR_RANGE=None
    SPATIAL_FIELD_MGR_RESULTS_VISIBILITY=None
    SPECIFY_SLOPE_OR_OFFSET=None
    SPOT_COORDINATE_BASE=None
    SPOT_COORDINATE_BOTTOM_PREFIX=None
    SPOT_COORDINATE_BOTTOM_SUFFIX=None
    SPOT_COORDINATE_ELEVATION_PREFIX=None
    SPOT_COORDINATE_ELEVATION_SUFFIX=None
    SPOT_COORDINATE_INCLUDE_ELEVATION=None
    SPOT_COORDINATE_TOP_PREFIX=None
    SPOT_COORDINATE_TOP_SUFFIX=None
    SPOT_DIM_LEADER=None
    SPOT_DIM_STYLE_SLOPE_UNITS=None
    SPOT_DIM_STYLE_SLOPE_UNITS_ALT=None
    SPOT_ELEV_BASE=None
    SPOT_ELEV_BEND_LEADER=None
    SPOT_ELEV_BOT_VALUE=None
    SPOT_ELEV_DISPLAY_ELEVATIONS=None
    SPOT_ELEV_FLIP_TEXT_VERT=None
    SPOT_ELEV_IND_BOTTOM=None
    SPOT_ELEV_IND_ELEVATION=None
    SPOT_ELEV_IND_EW=None
    SPOT_ELEV_IND_NS=None
    SPOT_ELEV_IND_TOP=None
    SPOT_ELEV_IND_TYPE=None
    SPOT_ELEV_IND_TYPE_BOTTOM=None
    SPOT_ELEV_IND_TYPE_ELEVATION=None
    SPOT_ELEV_IND_TYPE_TOP=None
    SPOT_ELEV_LEADER_ARROWHEAD=None
    SPOT_ELEV_LINE_PEN=None
    SPOT_ELEV_LOWER_PREFIX=None
    SPOT_ELEV_LOWER_SUFFIX=None
    SPOT_ELEV_LOWER_VALUE=None
    SPOT_ELEV_RELATIVE_BASE=None
    SPOT_ELEV_ROTATE_WITH_COMPONENT=None
    SPOT_ELEV_SINGLE_OR_UPPER_PREFIX=None
    SPOT_ELEV_SINGLE_OR_UPPER_SUFFIX=None
    SPOT_ELEV_SINGLE_OR_UPPER_VALUE=None
    SPOT_ELEV_SYMBOL=None
    SPOT_ELEV_TEXT_HORIZ_OFFSET=None
    SPOT_ELEV_TEXT_LOCATION=None
    SPOT_ELEV_TEXT_ORIENTATION=None
    SPOT_ELEV_TICK_MARK_PEN=None
    SPOT_ELEV_TOP_VALUE=None
    SPOT_SLOPE_LEADER_LENGTH=None
    SPOT_SLOPE_OFFSET_FROM_REFERENCE=None
    SPOT_SLOPE_PREFIX=None
    SPOT_SLOPE_SLOPE_DIRECTION=None
    SPOT_SLOPE_SLOPE_REPRESENTATION=None
    SPOT_SLOPE_SUFFIX=None
    SPOT_TEXT_FROM_LEADER=None
    STAIRSTYPE_CALCULATION_RULES=None
    STAIRSTYPE_CALC_RULE_MAX_RESULT=None
    STAIRSTYPE_CALC_RULE_MIN_RESULT=None
    STAIRSTYPE_CALC_RULE_RISER_MULTIPLIER=None
    STAIRSTYPE_CALC_RULE_TARGET_RESULT=None
    STAIRSTYPE_CALC_RULE_TREAD_MULTIPLIER=None
    STAIRSTYPE_CONSTRUCTION_METHOD=None
    STAIRSTYPE_CUTMARK_TYPE=None
    STAIRSTYPE_GEOMUNJOINED_END_CUT_STYLE=None
    STAIRSTYPE_HAS_INTERMEDIATE_SUPPORT=None
    STAIRSTYPE_HAS_LEFT_SUPPORT=None
    STAIRSTYPE_HAS_RIGHT_SUPPORT=None
    STAIRSTYPE_INTERMEDIATE_SUPPORT_TYPE=None
    STAIRSTYPE_IS_ASSEMBLED_STAIRS=None
    STAIRSTYPE_LANDING_TYPE=None
    STAIRSTYPE_LEFT_SIDE_SUPPORT_TYPE=None
    STAIRSTYPE_LEFT_SUPPORT_LATERAL_OFFSET=None
    STAIRSTYPE_MAXIMUM_RISER_HEIGHT=None
    STAIRSTYPE_MINIMUM_RUN_WIDTH=None
    STAIRSTYPE_MINIMUM_TREAD_DEPTH=None
    STAIRSTYPE_MINIMUM_TREAD_WIDTH_INSIDE_BOUNDARY=None
    STAIRSTYPE_NOTCH_CUSTOM_WIDTH=None
    STAIRSTYPE_NOTCH_EXTENSION=None
    STAIRSTYPE_NOTCH_HORIZONTAL_GAP=None
    STAIRSTYPE_NOTCH_THICKNESS=None
    STAIRSTYPE_NOTCH_VERTICAL_GAP=None
    STAIRSTYPE_NOTCH_WIDTH=None
    STAIRSTYPE_NUMBER_OF_INTERMEDIATE_SUPPORTS=None
    STAIRSTYPE_RIGHT_SIDE_SUPPORT_TYPE=None
    STAIRSTYPE_RIGHT_SUPPORT_LATERAL_OFFSET=None
    STAIRSTYPE_RUN_TYPE=None
    STAIRSTYPE_SHOW_CUTLINE=None
    STAIRSTYPE_SHOW_STAIR_PATH=None
    STAIRSTYPE_SHOW_UPDOWN=None
    STAIRSTYPE_WINDER_STEP_FRONT_MEASUREMENT=None
    STAIRS_ACTUAL_NUMBER_OF_RISERS=None
    STAIRS_ACTUAL_NUM_RISERS=None
    STAIRS_ACTUAL_RISER_HEIGHT=None
    STAIRS_ACTUAL_TREAD_DEPTH=None
    STAIRS_ATTR_BODY_MATERIAL=None
    STAIRS_ATTR_BREAK_SYM_IN_CUTLINE=None
    STAIRS_ATTR_CALC_ENABLED=None
    STAIRS_ATTR_CALC_MAX=None
    STAIRS_ATTR_CALC_MIN=None
    STAIRS_ATTR_EQ_RESULT=None
    STAIRS_ATTR_FIRST_RISER=None
    STAIRS_ATTR_LANDINGS_OVERLAPPING=None
    STAIRS_ATTR_LANDING_CARRIAGE=None
    STAIRS_ATTR_LAST_RISER=None
    STAIRS_ATTR_LEFT_SIDE_STRINGER=None
    STAIRS_ATTR_MAX_RISER_HEIGHT=None
    STAIRS_ATTR_MINIMUM_TREAD_DEPTH=None
    STAIRS_ATTR_MONOLITHIC_STAIRS=None
    STAIRS_ATTR_NOSING_LENGTH=None
    STAIRS_ATTR_NOSING_PLACEMENT=None
    STAIRS_ATTR_NUM_MID_STRINGERS=None
    STAIRS_ATTR_RIGHT_SIDE_STRINGER=None
    STAIRS_ATTR_RISERS_PRESENT=None
    STAIRS_ATTR_RISER_ANGLE=None
    STAIRS_ATTR_RISER_MATERIAL=None
    STAIRS_ATTR_RISER_MULT=None
    STAIRS_ATTR_RISER_THICKNESS=None
    STAIRS_ATTR_RISER_TREAD_CONNECT=None
    STAIRS_ATTR_RISER_TYPE=None
    STAIRS_ATTR_SIDE_STRINGER_TYPE_PARAM=None
    STAIRS_ATTR_STAIRS_BOTTOM=None
    STAIRS_ATTR_STAIRS_CUT_OFFSET=None
    STAIRS_ATTR_STAIR_CALCULATOR=None
    STAIRS_ATTR_STRINGER_CARRIAGE=None
    STAIRS_ATTR_STRINGER_HEIGHT=None
    STAIRS_ATTR_STRINGER_MATERIAL=None
    STAIRS_ATTR_STRINGER_OFFSET=None
    STAIRS_ATTR_STRINGER_THICKNESS=None
    STAIRS_ATTR_TEXT_FONT=None
    STAIRS_ATTR_TEXT_SIZE=None
    STAIRS_ATTR_TREAD_FRONT_PROFILE=None
    STAIRS_ATTR_TREAD_MATERIAL=None
    STAIRS_ATTR_TREAD_MULT=None
    STAIRS_ATTR_TREAD_THICKNESS=None
    STAIRS_ATTR_TREAD_WIDTH=None
    STAIRS_ATTR_TRIM_TOP=None
    STAIRS_BASE_LEVEL=None
    STAIRS_BASE_LEVEL_PARAM=None
    STAIRS_BASE_OFFSET=None
    STAIRS_CURVE_TYPE=None
    STAIRS_DBG_SHOW_ANNOTATION_CUT_MARK=None
    STAIRS_DBG_SHOW_BOUNDARY_2D=None
    STAIRS_DBG_SHOW_BOUNDARY_3D=None
    STAIRS_DBG_SHOW_LANDING_BOUNDARY=None
    STAIRS_DBG_SHOW_LANDING_FACES=None
    STAIRS_DBG_SHOW_LANDING_PATH=None
    STAIRS_DBG_SHOW_LEFT_RUN_BOUNDARY_2D=None
    STAIRS_DBG_SHOW_LEFT_RUN_BOUNDARY_3D=None
    STAIRS_DBG_SHOW_MONOLITHIC_SUPPORT_CORSE_GEOM=None
    STAIRS_DBG_SHOW_MONOLITHIC_SUPPORT_GEOM=None
    STAIRS_DBG_SHOW_RIGHT_RUN_BOUNDARY_2D=None
    STAIRS_DBG_SHOW_RIGHT_RUN_BOUNDARY_3D=None
    STAIRS_DBG_SHOW_RUN_CORSE_GEOM=None
    STAIRS_DBG_SHOW_RUN_GEOM=None
    STAIRS_DBG_SHOW_RUN_NOSING=None
    STAIRS_DBG_SHOW_RUN_OUTLINE_FOR_PLAN=None
    STAIRS_DBG_SHOW_RUN_PATH_2D=None
    STAIRS_DBG_SHOW_RUN_PATH_3D=None
    STAIRS_DBG_SHOW_RUN_RISER=None
    STAIRS_DBG_SHOW_SUPPORT_PATH=None
    STAIRS_DBG_SHOW_TREAD_FACES=None
    STAIRS_DBG_SHOW_TRISER_CORSE_GEOM=None
    STAIRS_DBG_SHOW_TRISER_GEOM=None
    STAIRS_DESIRED_NUMBER_OF_RISERS=None
    STAIRS_DESIRED_NUM_RISERS=None
    STAIRS_DOWN_TEXT=None
    STAIRS_ENABLE_CALCULATION_RULE_CHECKING=None
    STAIRS_INST_ALWAYS_UP=None
    STAIRS_INST_DOWN_ARROW_ON=None
    STAIRS_INST_DOWN_LABEL_ON=None
    STAIRS_INST_DOWN_LABEL_TEXT=None
    STAIRS_INST_UP_ARROW_ON=None
    STAIRS_INST_UP_LABEL_ON=None
    STAIRS_INST_UP_LABEL_TEXT=None
    STAIRS_LANDINGTYPE_HAS_MONOLITHIC_SUPPORT=None
    STAIRS_LANDINGTYPE_LANDING_MATERIAL=None
    STAIRS_LANDINGTYPE_STRUCTURE=None
    STAIRS_LANDINGTYPE_THICKNESS=None
    STAIRS_LANDINGTYPE_TREADRISER_TYPE=None
    STAIRS_LANDINGTYPE_USE_SAME_TRISER_AS_RUN=None
    STAIRS_LANDING_BASE_ELEVATION=None
    STAIRS_LANDING_OVERRIDDEN=None
    STAIRS_LANDING_STRUCTURAL=None
    STAIRS_LANDING_THICKNESS=None
    STAIRS_MIN_AUTOMATIC_LANDING_DEPTH=None
    STAIRS_MULTISTORY_TOP_LEVEL_PARAM=None
    STAIRS_MULTISTORY_UP_TO_LEVEL=None
    STAIRS_PATH_FULL_STEP_ARROW=None
    STAIRS_PATH_START_EXTENSION=None
    STAIRS_PATH_START_FROM_RISER=None
    STAIRS_RAILING_ANGLED_CONNECTION=None
    STAIRS_RAILING_BALUSTERS_PER_TREAD=None
    STAIRS_RAILING_BALUSTER_BOTTOM_ANGLE=None
    STAIRS_RAILING_BALUSTER_FAMILY=None
    STAIRS_RAILING_BALUSTER_HEIGHT=None
    STAIRS_RAILING_BALUSTER_IS_POST=None
    STAIRS_RAILING_BALUSTER_LENGTH=None
    STAIRS_RAILING_BALUSTER_OFFSET=None
    STAIRS_RAILING_BALUSTER_PLACEMENT=None
    STAIRS_RAILING_BALUSTER_SHAPE=None
    STAIRS_RAILING_BALUSTER_SLOPE_ANGLE=None
    STAIRS_RAILING_BALUSTER_SPACING=None
    STAIRS_RAILING_BALUSTER_SPACING_TYPE=None
    STAIRS_RAILING_BALUSTER_TOP_ANGLE=None
    STAIRS_RAILING_BALUSTER_WIDTH=None
    STAIRS_RAILING_BASE_LEVEL_PARAM=None
    STAIRS_RAILING_CONNECTION=None
    STAIRS_RAILING_HEIGHT=None
    STAIRS_RAILING_HEIGHT_OFFSET=None
    STAIRS_RAILING_HEIGHT_SHIFT_TYPE=None
    STAIRS_RAILING_HEIGHT_SHIFT_VAL=None
    STAIRS_RAILING_PLACEMENT_OFFSET=None
    STAIRS_RAILING_RAIL_HEIGHT=None
    STAIRS_RAILING_RAIL_NAME=None
    STAIRS_RAILING_RAIL_OFFSET=None
    STAIRS_RAILING_RAIL_STRUCTURE=None
    STAIRS_RAILING_SHAPE=None
    STAIRS_RAILING_TANGENT_CONNECTION=None
    STAIRS_RAILING_THICKNESS=None
    STAIRS_RAILING_WIDTH=None
    STAIRS_RUNTYPE_HAS_MONOLITHIC_SUPPORT=None
    STAIRS_RUNTYPE_RUN_MATERIAL=None
    STAIRS_RUNTYPE_STRUCTURAL_DEPTH=None
    STAIRS_RUNTYPE_STRUCTURE=None
    STAIRS_RUNTYPE_TOTAL_DEPTH=None
    STAIRS_RUNTYPE_UNDERSIDE_SURFACE_TYPE=None
    STAIRS_RUN_ACTUAL_NUMBER_OF_RISERS=None
    STAIRS_RUN_ACTUAL_NUMBER_OF_TREADS=None
    STAIRS_RUN_ACTUAL_RISER_HEIGHT=None
    STAIRS_RUN_ACTUAL_RUN_WIDTH=None
    STAIRS_RUN_ACTUAL_TREAD_DEPTH=None
    STAIRS_RUN_BEGIN_WITH_RISER=None
    STAIRS_RUN_BOTTOM_ELEVATION=None
    STAIRS_RUN_CCW=None
    STAIRS_RUN_CENTER_MARK_VISIBLE=None
    STAIRS_RUN_CREATE_AUTO_LANDING=None
    STAIRS_RUN_END_WITH_RISER=None
    STAIRS_RUN_EXTEND_BELOW_RISER_BASE=None
    STAIRS_RUN_EXTEND_BELOW_TREAD_BASE=None
    STAIRS_RUN_HEIGHT=None
    STAIRS_RUN_LOCATIONPATH_JUSTFICATION=None
    STAIRS_RUN_OVERRIDDEN=None
    STAIRS_RUN_STRUCTURAL=None
    STAIRS_RUN_TOP_ELEVATION=None
    STAIRS_RUN_WIDTH_MEASUREMENT=None
    STAIRS_RUN_WINDER_BEGIN_WITH_STRAIGHT=None
    STAIRS_RUN_WINDER_END_WITH_STRAIGHT=None
    STAIRS_SHOW_DOWN_TEXT=None
    STAIRS_SHOW_UP_TEXT=None
    STAIRS_STAIRS_HEIGHT=None
    STAIRS_STRINGERS_PRESENT=None
    STAIRS_SUPPORTTYPE_FLIP_SECTION_PROFILE=None
    STAIRS_SUPPORTTYPE_MATERIAL=None
    STAIRS_SUPPORTTYPE_SECTION_PROFILE=None
    STAIRS_SUPPORTTYPE_STRUCTURAL_DEPTH=None
    STAIRS_SUPPORTTYPE_STRUCTURAL_DEPTH_ON_LANDING=None
    STAIRS_SUPPORTTYPE_STRUCTURAL_DEPTH_ON_RUN=None
    STAIRS_SUPPORTTYPE_TOPSIDE_SURFACE=None
    STAIRS_SUPPORTTYPE_TOTAL_DEPTH=None
    STAIRS_SUPPORTTYPE_UNDERSIDE_SURFACE=None
    STAIRS_SUPPORTTYPE_WIDTH=None
    STAIRS_SUPPORT_HORIZONTAL_OFFSET=None
    STAIRS_SUPPORT_LANDINGSUPPORT_TYPE=None
    STAIRS_SUPPORT_LOWER_END_CUT=None
    STAIRS_SUPPORT_OVERRIDDEN=None
    STAIRS_SUPPORT_TRIM_SUPPORT_UPPER=None
    STAIRS_SUPPORT_UPPER_END_CUT=None
    STAIRS_SUPPORT_VERTICAL_OFFSET=None
    STAIRS_TEXT_ORIENTATION=None
    STAIRS_TEXT_TYPE=None
    STAIRS_TOP_LEVEL=None
    STAIRS_TOP_LEVEL_PARAM=None
    STAIRS_TOP_OFFSET=None
    STAIRS_TOTAL_NUMBER_OF_RISERS=None
    STAIRS_TOTAL_NUMBER_OF_TREADS=None
    STAIRS_TRISERTYPE_BACK_NOSING=None
    STAIRS_TRISERTYPE_FRONT_NOSING=None
    STAIRS_TRISERTYPE_LEFT_NOSING=None
    STAIRS_TRISERTYPE_NOSING_LENGTH=None
    STAIRS_TRISERTYPE_NOSING_PLACEMENT=None
    STAIRS_TRISERTYPE_NOSING_PROFILE=None
    STAIRS_TRISERTYPE_RIGHT_NOSING=None
    STAIRS_TRISERTYPE_RISER=None
    STAIRS_TRISERTYPE_RISER_IS_SLANTED=None
    STAIRS_TRISERTYPE_RISER_MATERIAL=None
    STAIRS_TRISERTYPE_RISER_PROFILE=None
    STAIRS_TRISERTYPE_RISER_STYLE=None
    STAIRS_TRISERTYPE_RISER_THICKNESS=None
    STAIRS_TRISERTYPE_RISER_TREAD_CONNECTION=None
    STAIRS_TRISERTYPE_TREAD=None
    STAIRS_TRISERTYPE_TREAD_MATERIAL=None
    STAIRS_TRISERTYPE_TREAD_PROFILE=None
    STAIRS_TRISERTYPE_TREAD_THICKNESS=None
    STAIRS_TRISER_IS_TYPE_OVERRIDDEN=None
    STAIRS_TRISER_NUMBER_BASE_INDEX=None
    STAIRS_TRISER_RISER_MARK=None
    STAIRS_TRISER_RISER_NUMBER=None
    STAIRS_TRISER_TREAD_MARK=None
    STAIRS_TRISER_TREAD_NUMBER=None
    STAIRS_UP_TEXT=None
    STAIRS_WINDERPATTERN_FILLET_INSIDE_CORNER=None
    STAIRS_WINDERPATTERN_MINIMUM_WIDTH_CORNER=None
    STAIRS_WINDERPATTERN_MINIMUM_WIDTH_INSIDE_WALKLINE=None
    STAIRS_WINDERPATTERN_NUMBER_OF_STRAIGHT_STEPS_AT_BEGIN=None
    STAIRS_WINDERPATTERN_NUMBER_OF_STRAIGHT_STEPS_AT_END=None
    STAIRS_WINDERPATTERN_RADIUS_INTERIOR=None
    STAIRS_WINDERPATTERN_STAIR_PATH_OFFSET=None
    STAIRS_WINDERPATTERN_WINDER_STYLE=None
    START_EXTENSION=None
    START_JOIN_CUTBACK=None
    START_SYMBOL_TYPE=None
    START_Y_JUSTIFICATION=None
    START_Y_OFFSET_VALUE=None
    START_Z_JUSTIFICATION=None
    START_Z_OFFSET_VALUE=None
    STRUCTURAL_ANALYTICAL_BEAM_HORIZONTAL_PROJECTION_PLANE=None
    STRUCTURAL_ANALYTICAL_BEAM_RIGID_LINK=None
    STRUCTURAL_ANALYTICAL_COLUMN_HORIZONTAL_PROJECTION_PLANE=None
    STRUCTURAL_ANALYTICAL_COLUMN_RIGID_LINK=None
    STRUCTURAL_ANALYTICAL_HARD_POINTS=None
    STRUCTURAL_ANALYTICAL_MODEL=None
    STRUCTURAL_ANALYTICAL_PROJECT_FLOOR_PLANE=None
    STRUCTURAL_ANALYTICAL_PROJECT_MEMBER_PLANE=None
    STRUCTURAL_ANALYTICAL_PROJECT_MEMBER_PLANE_COLUMN_BOTTOM=None
    STRUCTURAL_ANALYTICAL_PROJECT_MEMBER_PLANE_COLUMN_TOP=None
    STRUCTURAL_ANALYTICAL_TESSELLATE=None
    STRUCTURAL_ANALYTICAL_TESS_DEVIATION=None
    STRUCTURAL_ANALYZES_AS=None
    STRUCTURAL_ASSET_PARAM=None
    STRUCTURAL_ATTACHMENT_BASE_DISTANCE=None
    STRUCTURAL_ATTACHMENT_BASE_RATIO=None
    STRUCTURAL_ATTACHMENT_BASE_REFERENCEDEND=None
    STRUCTURAL_ATTACHMENT_BASE_TYPE=None
    STRUCTURAL_ATTACHMENT_END_LEVEL_REFERENCE=None
    STRUCTURAL_ATTACHMENT_END_REFELEMENT_END=None
    STRUCTURAL_ATTACHMENT_END_TYPE=None
    STRUCTURAL_ATTACHMENT_END_VALUE_DISTANCE=None
    STRUCTURAL_ATTACHMENT_END_VALUE_ELEVATION=None
    STRUCTURAL_ATTACHMENT_END_VALUE_RATIO=None
    STRUCTURAL_ATTACHMENT_START_LEVEL_REFERENCE=None
    STRUCTURAL_ATTACHMENT_START_REFELEMENT_END=None
    STRUCTURAL_ATTACHMENT_START_TYPE=None
    STRUCTURAL_ATTACHMENT_START_VALUE_DISTANCE=None
    STRUCTURAL_ATTACHMENT_START_VALUE_ELEVATION=None
    STRUCTURAL_ATTACHMENT_START_VALUE_RATIO=None
    STRUCTURAL_ATTACHMENT_TOP_DISTANCE=None
    STRUCTURAL_ATTACHMENT_TOP_RATIO=None
    STRUCTURAL_ATTACHMENT_TOP_REFERENCEDEND=None
    STRUCTURAL_ATTACHMENT_TOP_TYPE=None
    STRUCTURAL_BEAM_CUTBACK_FOR_COLUMN=None
    STRUCTURAL_BEAM_END0_ELEVATION=None
    STRUCTURAL_BEAM_END1_ELEVATION=None
    STRUCTURAL_BEAM_END_ATTACHMENT_DISTANCE=None
    STRUCTURAL_BEAM_END_ATTACHMENT_REFCOLUMN_END=None
    STRUCTURAL_BEAM_END_ATTACHMENT_TYPE=None
    STRUCTURAL_BEAM_END_SUPPORT=None
    STRUCTURAL_BEAM_ORIENTATION=None
    STRUCTURAL_BEAM_START_ATTACHMENT_DISTANCE=None
    STRUCTURAL_BEAM_START_ATTACHMENT_REFCOLUMN_END=None
    STRUCTURAL_BEAM_START_ATTACHMENT_TYPE=None
    STRUCTURAL_BEAM_START_SUPPORT=None
    STRUCTURAL_BEND_DIR_ANGLE=None
    STRUCTURAL_BOTTOM_RELEASE_FX=None
    STRUCTURAL_BOTTOM_RELEASE_FY=None
    STRUCTURAL_BOTTOM_RELEASE_FZ=None
    STRUCTURAL_BOTTOM_RELEASE_MX=None
    STRUCTURAL_BOTTOM_RELEASE_MY=None
    STRUCTURAL_BOTTOM_RELEASE_MZ=None
    STRUCTURAL_BOTTOM_RELEASE_TYPE=None
    STRUCTURAL_BRACE_REPRESENTATION=None
    STRUCTURAL_CAMBER=None
    STRUCTURAL_CONNECTION_APPROVAL_STATUS=None
    STRUCTURAL_CONNECTION_CODE_CHECKING_STATUS=None
    STRUCTURAL_CONNECTION_MODIFY_CONNECTION_PARAMETERS=None
    STRUCTURAL_CONNECTION_NOBLE_STATUS=None
    STRUCTURAL_CONNECTION_SYMBOL=None
    STRUCTURAL_COPING_DISTANCE=None
    STRUCTURAL_DISPLAY_IN_HIDDEN_VIEWS=None
    STRUCTURAL_DISPLAY_IN_HIDDEN_VIEWS_COLUMN=None
    STRUCTURAL_DISPLAY_IN_HIDDEN_VIEWS_FRAMING=None
    STRUCTURAL_ELEVATION_AT_BOTTOM=None
    STRUCTURAL_ELEVATION_AT_BOTTOM_CORE=None
    STRUCTURAL_ELEVATION_AT_BOTTOM_SURVEY=None
    STRUCTURAL_ELEVATION_AT_TOP=None
    STRUCTURAL_ELEVATION_AT_TOP_CORE=None
    STRUCTURAL_ELEVATION_AT_TOP_SURVEY=None
    STRUCTURAL_END_RELEASE_FX=None
    STRUCTURAL_END_RELEASE_FY=None
    STRUCTURAL_END_RELEASE_FZ=None
    STRUCTURAL_END_RELEASE_MX=None
    STRUCTURAL_END_RELEASE_MY=None
    STRUCTURAL_END_RELEASE_MZ=None
    STRUCTURAL_END_RELEASE_TYPE=None
    STRUCTURAL_FAMILY_CODE_NAME=None
    STRUCTURAL_FAMILY_NAME_KEY=None
    STRUCTURAL_FLOOR_ANALYZES_AS=None
    STRUCTURAL_FLOOR_CORE_THICKNESS=None
    STRUCTURAL_FOUNDATION_LENGTH=None
    STRUCTURAL_FOUNDATION_THICKNESS=None
    STRUCTURAL_FOUNDATION_WIDTH=None
    STRUCTURAL_FRAME_CUT_LENGTH=None
    STRUCTURAL_MATERIAL_PARAM=None
    STRUCTURAL_MATERIAL_TYPE=None
    STRUCTURAL_MEMBER_FORCES=None
    STRUCTURAL_NUMBER_OF_STUDS=None
    STRUCTURAL_REFERENCE_LEVEL_ELEVATION=None
    STRUCTURAL_SECTION_AREA=None
    STRUCTURAL_SECTION_BOTTOM_CUT_HEIGHT=None
    STRUCTURAL_SECTION_BOTTOM_CUT_WIDTH=None
    STRUCTURAL_SECTION_CANTILEVER_HEIGHT=None
    STRUCTURAL_SECTION_CANTILEVER_LENGTH=None
    STRUCTURAL_SECTION_COMMON_ALPHA=None
    STRUCTURAL_SECTION_COMMON_CENTROID_HORIZ=None
    STRUCTURAL_SECTION_COMMON_CENTROID_VERTICAL=None
    STRUCTURAL_SECTION_COMMON_DIAMETER=None
    STRUCTURAL_SECTION_COMMON_ELASTIC_MODULUS_STRONG_AXIS=None
    STRUCTURAL_SECTION_COMMON_ELASTIC_MODULUS_WEAK_AXIS=None
    STRUCTURAL_SECTION_COMMON_HEIGHT=None
    STRUCTURAL_SECTION_COMMON_MOMENT_OF_INERTIA_STRONG_AXIS=None
    STRUCTURAL_SECTION_COMMON_MOMENT_OF_INERTIA_WEAK_AXIS=None
    STRUCTURAL_SECTION_COMMON_NOMINAL_WEIGHT=None
    STRUCTURAL_SECTION_COMMON_PERIMETER=None
    STRUCTURAL_SECTION_COMMON_PLASTIC_MODULUS_STRONG_AXIS=None
    STRUCTURAL_SECTION_COMMON_PLASTIC_MODULUS_WEAK_AXIS=None
    STRUCTURAL_SECTION_COMMON_SHEAR_AREA_STRONG_AXIS=None
    STRUCTURAL_SECTION_COMMON_SHEAR_AREA_WEAK_AXIS=None
    STRUCTURAL_SECTION_COMMON_TORSIONAL_MODULUS=None
    STRUCTURAL_SECTION_COMMON_TORSIONAL_MOMENT_OF_INERTIA=None
    STRUCTURAL_SECTION_COMMON_WARPING_CONSTANT=None
    STRUCTURAL_SECTION_COMMON_WIDTH=None
    STRUCTURAL_SECTION_CPROFILE_FOLD_LENGTH=None
    STRUCTURAL_SECTION_HSS_INNERFILLET=None
    STRUCTURAL_SECTION_HSS_OUTERFILLET=None
    STRUCTURAL_SECTION_ISHAPE_BOLT_DIAMETER=None
    STRUCTURAL_SECTION_ISHAPE_BOLT_SPACING=None
    STRUCTURAL_SECTION_ISHAPE_BOLT_SPACING_BETWEEN_ROWS=None
    STRUCTURAL_SECTION_ISHAPE_BOLT_SPACING_TWO_ROWS=None
    STRUCTURAL_SECTION_ISHAPE_BOLT_SPACING_WEB=None
    STRUCTURAL_SECTION_ISHAPE_CLEAR_WEB_HEIGHT=None
    STRUCTURAL_SECTION_ISHAPE_FLANGEFILLET=None
    STRUCTURAL_SECTION_ISHAPE_FLANGETHICKNESS=None
    STRUCTURAL_SECTION_ISHAPE_FLANGE_TOE_OF_FILLET=None
    STRUCTURAL_SECTION_ISHAPE_WEBFILLET=None
    STRUCTURAL_SECTION_ISHAPE_WEBHEIGHT=None
    STRUCTURAL_SECTION_ISHAPE_WEBTHICKNESS=None
    STRUCTURAL_SECTION_ISHAPE_WEB_TOE_OF_FILLET=None
    STRUCTURAL_SECTION_IWELDED_BOTTOMFLANGETHICKNESS=None
    STRUCTURAL_SECTION_IWELDED_BOTTOMFLANGEWIDTH=None
    STRUCTURAL_SECTION_IWELDED_TOPFLANGETHICKNESS=None
    STRUCTURAL_SECTION_IWELDED_TOPFLANGEWIDTH=None
    STRUCTURAL_SECTION_LANGLE_BOLT_DIAMETER_LONGER_FLANGE=None
    STRUCTURAL_SECTION_LANGLE_BOLT_DIAMETER_SHORTER_FLANGE=None
    STRUCTURAL_SECTION_LANGLE_BOLT_SPACING_1_LONGER_FLANGE=None
    STRUCTURAL_SECTION_LANGLE_BOLT_SPACING_2_LONGER_FLANGE=None
    STRUCTURAL_SECTION_LANGLE_BOLT_SPACING_SHORTER_FLANGE=None
    STRUCTURAL_SECTION_LPROFILE_LIP_LENGTH=None
    STRUCTURAL_SECTION_NAME_KEY=None
    STRUCTURAL_SECTION_PIPESTANDARD_WALLDESIGNTHICKNESS=None
    STRUCTURAL_SECTION_PIPESTANDARD_WALLNOMINALTHICKNESS=None
    STRUCTURAL_SECTION_SHAPE=None
    STRUCTURAL_SECTION_SIGMA_PROFILE_BEND_WIDTH=None
    STRUCTURAL_SECTION_SIGMA_PROFILE_MIDDLE_BEND_WIDTH=None
    STRUCTURAL_SECTION_SIGMA_PROFILE_TOP_BEND_WIDTH=None
    STRUCTURAL_SECTION_TOP_CUT_HEIGHT=None
    STRUCTURAL_SECTION_TOP_CUT_WIDTH=None
    STRUCTURAL_SECTION_ZPROFILE_BOTTOM_FLANGE_LENGTH=None
    STRUCTURAL_START_RELEASE_FX=None
    STRUCTURAL_START_RELEASE_FY=None
    STRUCTURAL_START_RELEASE_FZ=None
    STRUCTURAL_START_RELEASE_MX=None
    STRUCTURAL_START_RELEASE_MY=None
    STRUCTURAL_START_RELEASE_MZ=None
    STRUCTURAL_START_RELEASE_TYPE=None
    STRUCTURAL_STICK_SYMBOL_LOCATION=None
    STRUCTURAL_TOP_RELEASE_FX=None
    STRUCTURAL_TOP_RELEASE_FY=None
    STRUCTURAL_TOP_RELEASE_FZ=None
    STRUCTURAL_TOP_RELEASE_MX=None
    STRUCTURAL_TOP_RELEASE_MY=None
    STRUCTURAL_TOP_RELEASE_MZ=None
    STRUCTURAL_TOP_RELEASE_TYPE=None
    STRUCTURAL_WALL_BOTTOM_PROJECTION_PLANE=None
    STRUCTURAL_WALL_PROJECTION_SURFACE=None
    STRUCTURAL_WALL_TOP_PROJECTION_PLANE=None
    STRUCT_CONNECTION_APPLY_TO=None
    STRUCT_CONNECTION_BEAM_END=None
    STRUCT_CONNECTION_BEAM_START=None
    STRUCT_CONNECTION_COLUMN_BASE=None
    STRUCT_CONNECTION_COLUMN_TOP=None
    STRUCT_CONNECTION_CUTBACK=None
    STRUCT_CONNECTION_TYPE_NAME=None
    STRUCT_FRAM_JOIN_STATUS=None
    SUPPORT_HAND_CLEARANCE=None
    SUPPORT_HEIGHT=None
    SURFACE_AREA=None
    SURFACE_PATTERN_ID_PARAM=None
    SURFACE_PERIMETER=None
    SWEEP_BASE_FLOOR_SUBCATEGORY_ID=None
    SWEEP_BASE_OFFSET=None
    SWEEP_BASE_ROOF_SUBCATEGORY_ID=None
    SWEEP_BASE_VERT_OFFSET=None
    SWEEP_MAX_SEG_ANGLE=None
    SWEEP_TRAJ_SEGMENTED=None
    SYMBOL_FAMILY_AND_TYPE_NAMES_PARAM=None
    SYMBOL_FAMILY_NAME_PARAM=None
    SYMBOL_ID_PARAM=None
    SYMBOL_NAME_PARAM=None
    TAG_LEADER_TYPE=None
    TAG_NO_BREAK_PARAM_STRINGS=None
    TAG_ORIENTATION_PARAM=None
    TAG_SAMPLE_TEXT=None
    TAG_TAG=None
    TEMPLATE_NAME=None
    TERMINATION_EXTENSION_LENGTH=None
    TEXT_ALIGNMENT=None
    TEXT_ALIGN_HORZ=None
    TEXT_ALIGN_VERT=None
    TEXT_BACKGROUND=None
    TEXT_BOX_VISIBILITY=None
    TEXT_COLOR=None
    TEXT_DIST_TO_LINE=None
    TEXT_FONT=None
    TEXT_POSITION=None
    TEXT_SIZE=None
    TEXT_STYLE_BOLD=None
    TEXT_STYLE_FONT=None
    TEXT_STYLE_ITALIC=None
    TEXT_STYLE_SIZE=None
    TEXT_STYLE_UNDERLINE=None
    TEXT_TAB_SIZE=None
    TEXT_TEXT=None
    TEXT_WIDTH_SCALE=None
    THERMAL_MATERIAL_PARAM_COMPRESSIBILITY=None
    THERMAL_MATERIAL_PARAM_ELECTRICAL_RESISTIVITY=None
    THERMAL_MATERIAL_PARAM_EMISSIVITY=None
    THERMAL_MATERIAL_PARAM_GAS_VISCOSITY=None
    THERMAL_MATERIAL_PARAM_LIQUID_VISCOSITY=None
    THERMAL_MATERIAL_PARAM_PERMEABILITY=None
    THERMAL_MATERIAL_PARAM_POROSITY=None
    THERMAL_MATERIAL_PARAM_REFLECTIVITY=None
    THERMAL_MATERIAL_PARAM_SPECIFIC_HEAT_OF_VAPORIZATION=None
    THERMAL_MATERIAL_PARAM_TRANSMITS_LIGHT=None
    THERMAL_MATERIAL_PARAM_VAPOR_PRESSURE=None
    TICK_MARK_PEN=None
    TILE_PATTERN_FAMREF_COMPONENT_EXTENTS=None
    TILE_PATTERN_GRID_CELLS_X=None
    TILE_PATTERN_GRID_CELLS_Y=None
    TILE_PATTERN_GRID_UNIT_X=None
    TILE_PATTERN_GRID_UNIT_Y=None
    TITLE_FONT=None
    TITLE_SIZE=None
    TITLE_STYLE_BOLD=None
    TITLE_STYLE_ITALIC=None
    TITLE_STYLE_UNDERLINE=None
    TRAP_MULL_WIDTH=None
    TRUSS_BEARING_CHORD_TOP_BOTTOM_PARAM=None
    TRUSS_ELEMENT_ANGLE_PARAM=None
    TRUSS_ELEMENT_BEARING_JUST_PARAM=None
    TRUSS_ELEMENT_CLASS_PARAM=None
    TRUSS_ELEMENT_CREATE_BOTTOM_PARAM=None
    TRUSS_ELEMENT_CREATE_TOP_PARAM=None
    TRUSS_ELEMENT_END0_ELEVATION=None
    TRUSS_ELEMENT_END1_ELEVATION=None
    TRUSS_ELEMENT_REFERENCE_LEVEL_PARAM=None
    TRUSS_ELEMENT_ROTATE_CHORDS_WITH_TRUSS=None
    TRUSS_ELEMENT_SPAN_PARAM=None
    TRUSS_ELEMENT_STICK_JUST_PARAM=None
    TRUSS_ELEMENT_TAG_NEW_MEMBERS_VIEW=None
    TRUSS_FAMILY_BOTTOM_CHORD_ANGLE_PARAM=None
    TRUSS_FAMILY_BOTTOM_CHORD_END_RELEASE_TYPE=None
    TRUSS_FAMILY_BOTTOM_CHORD_START_RELEASE_TYPE=None
    TRUSS_FAMILY_BOTTOM_CHORD_STRUCTURAL_TYPES_PARAM=None
    TRUSS_FAMILY_BOTTOM_CHORD_VERTICAL_PROJECTION_PARAM=None
    TRUSS_FAMILY_DIAG_WEB_ANGLE_PARAM=None
    TRUSS_FAMILY_DIAG_WEB_END_RELEASE_TYPE=None
    TRUSS_FAMILY_DIAG_WEB_START_RELEASE_TYPE=None
    TRUSS_FAMILY_DIAG_WEB_STRUCTURAL_TYPES_PARAM=None
    TRUSS_FAMILY_TOP_CHORD_ANGLE_PARAM=None
    TRUSS_FAMILY_TOP_CHORD_END_RELEASE_TYPE=None
    TRUSS_FAMILY_TOP_CHORD_START_RELEASE_TYPE=None
    TRUSS_FAMILY_TOP_CHORD_STRUCTURAL_TYPES_PARAM=None
    TRUSS_FAMILY_TOP_CHORD_VERTICAL_PROJECTION_PARAM=None
    TRUSS_FAMILY_TRANSFORMATION_PARAM=None
    TRUSS_FAMILY_VERT_WEB_ANGLE_PARAM=None
    TRUSS_FAMILY_VERT_WEB_END_RELEASE_TYPE=None
    TRUSS_FAMILY_VERT_WEB_START_RELEASE_TYPE=None
    TRUSS_FAMILY_VERT_WEB_STRUCTURAL_TYPES_PARAM=None
    TRUSS_FAMILY_WEBS_HAVE_SYMBOLIC_CUTBACK_PARAM=None
    TRUSS_HEIGHT=None
    TRUSS_LENGTH=None
    TRUSS_NON_BEARING_OFFSET_PARAM=None
    TYPE_WALL_CLOSURE=None
    UNIFORMAT_CODE=None
    UNIFORMAT_DESCRIPTION=None
    value__=None
    VIEWER3D_RENDER_SETTINGS=None
    VIEWER_ANNOTATION_CROP_ACTIVE=None
    VIEWER_BOUND_ACTIVE_BOTTOM=None
    VIEWER_BOUND_ACTIVE_FAR=None
    VIEWER_BOUND_ACTIVE_LEFT=None
    VIEWER_BOUND_ACTIVE_NEAR=None
    VIEWER_BOUND_ACTIVE_RIGHT=None
    VIEWER_BOUND_ACTIVE_TOP=None
    VIEWER_BOUND_FAR_CLIPPING=None
    VIEWER_BOUND_OFFSET_BOTTOM=None
    VIEWER_BOUND_OFFSET_FAR=None
    VIEWER_BOUND_OFFSET_LEFT=None
    VIEWER_BOUND_OFFSET_NEAR=None
    VIEWER_BOUND_OFFSET_RIGHT=None
    VIEWER_BOUND_OFFSET_TOP=None
    VIEWER_CROP_REGION=None
    VIEWER_CROP_REGION_DISABLED=None
    VIEWER_CROP_REGION_VISIBLE=None
    VIEWER_DETAIL_NUMBER=None
    VIEWER_EYE_ELEVATION=None
    VIEWER_IS_REFERENCE=None
    VIEWER_MODEL_CLIP_BOX_ACTIVE=None
    VIEWER_OPTION_VISIBILITY=None
    VIEWER_PERSPECTIVE=None
    VIEWER_PERSPECTIVE_DISABLED=None
    VIEWER_REFERENCE_LABEL=None
    VIEWER_REFERENCE_LABEL_TEXT=None
    VIEWER_SHEET_NUMBER=None
    VIEWER_SHOW_UNCROPPED=None
    VIEWER_TARGET_ELEVATION=None
    VIEWER_VOLUME_OF_INTEREST_CROP=None
    VIEWPORT_ATTR_LABEL_TAG=None
    VIEWPORT_ATTR_ORIENTATION_ON_SHEET=None
    VIEWPORT_ATTR_SHOW_BOX=None
    VIEWPORT_ATTR_SHOW_EXTENSION_LINE=None
    VIEWPORT_ATTR_SHOW_LABEL=None
    VIEWPORT_DETAIL_NUMBER=None
    VIEWPORT_SCALE=None
    VIEWPORT_SHEET_NAME=None
    VIEWPORT_SHEET_NUMBER=None
    VIEWPORT_VIEW_NAME=None
    VIEW_ANALYSIS_DISPLAY_STYLE=None
    VIEW_ANALYSIS_RESULTS_VISIBILITY=None
    VIEW_ASSOCIATED_ASSEMBLY_INSTANCE_ID=None
    VIEW_BACK_CLIPPING=None
    VIEW_CAMERA_ORIENTATION=None
    VIEW_CAMERA_POSITION=None
    VIEW_CLEAN_JOINS=None
    VIEW_DEPENDENCY=None
    VIEW_DEPTH=None
    VIEW_DESCRIPTION=None
    VIEW_DESIGN_OPTIONS_CONFIG=None
    VIEW_DETAIL_LEVEL=None
    VIEW_DISCIPLINE=None
    VIEW_FAMILY=None
    VIEW_FAMILY_AND_TYPE_SCHEDULES=None
    VIEW_FAMILY_SCHEDULES=None
    VIEW_FIXED_SKETCH_PLANE=None
    VIEW_GRAPH_SCHED_BOTTOM_LEVEL=None
    VIEW_GRAPH_SCHED_GRID_APPEARANCE=None
    VIEW_GRAPH_SCHED_GROUP_SIMILAR=None
    VIEW_GRAPH_SCHED_HIDDEN_LEVELS=None
    VIEW_GRAPH_SCHED_LEVEL_RELATIVE_BASE_TYPE=None
    VIEW_GRAPH_SCHED_LOCATIONS_HIGH=None
    VIEW_GRAPH_SCHED_LOCATIONS_LOW=None
    VIEW_GRAPH_SCHED_MATERIAL_TYPES=None
    VIEW_GRAPH_SCHED_NUMBER_COLUMNS=None
    VIEW_GRAPH_SCHED_OFF_GRID=None
    VIEW_GRAPH_SCHED_ROWS_COUNT=None
    VIEW_GRAPH_SCHED_ROWS_FROM=None
    VIEW_GRAPH_SCHED_TEXT_APPEARANCE=None
    VIEW_GRAPH_SCHED_TITLE=None
    VIEW_GRAPH_SCHED_TOP_LEVEL=None
    VIEW_GRAPH_SCHED_TOTAL_COLUMNS=None
    VIEW_GRAPH_SCHED_TOTAL_ROWS=None
    VIEW_GRAPH_SCHED_UNITS_FORMAT=None
    VIEW_GRAPH_SUN_PATH=None
    VIEW_GRAPH_SUN_PATH_SIZE=None
    VIEW_MODEL_DISPLAY_MODE=None
    VIEW_NAME=None
    VIEW_PARTS_VISIBILITY=None
    VIEW_PHASE=None
    VIEW_PHASE_FILTER=None
    VIEW_REFERENCING_DETAIL=None
    VIEW_REFERENCING_SHEET=None
    VIEW_SCALE=None
    VIEW_SCALE_CUSTOMNAME=None
    VIEW_SCALE_HAVENAME=None
    VIEW_SCALE_PULLDOWN_IMPERIAL=None
    VIEW_SCALE_PULLDOWN_METRIC=None
    VIEW_SCHEMA_SETTING_FOR_BUILDING=None
    VIEW_SCHEMA_SETTING_FOR_SYSTEM=None
    VIEW_SCHEMA_SETTING_FOR_SYSTEM_TEMPLATE=None
    VIEW_SHEET_VIEWPORT_INFO=None
    VIEW_SHOW_HIDDEN_LINES=None
    VIEW_SHOW_MASSING=None
    VIEW_SLANTED_COLUMN_SYMBOL_OFFSET=None
    VIEW_TEMPLATE=None
    VIEW_TEMPLATE_FOR_SCHEDULE=None
    VIEW_TYPE=None
    VIEW_TYPE_SCHEDULES=None
    VIEW_UNDERLAY_BOTTOM_ID=None
    VIEW_UNDERLAY_ORIENTATION=None
    VIEW_UNDERLAY_TOP_ID=None
    VIEW_VISIBLE_CATEGORIES=None
    VIS_GRAPHICS_ANALYTICAL_MODEL=None
    VIS_GRAPHICS_ANNOTATION=None
    VIS_GRAPHICS_DESIGNOPTIONS=None
    VIS_GRAPHICS_FILTERS=None
    VIS_GRAPHICS_IMPORT=None
    VIS_GRAPHICS_MODEL=None
    VIS_GRAPHICS_POINT_CLOUDS=None
    VIS_GRAPHICS_RVT_LINKS=None
    VIS_GRAPHICS_WORKSETS=None
    VOLUME_CUT=None
    VOLUME_FILL=None
    VOLUME_NET=None
    VOLUME_OF_INTEREST_NAME=None
    VOLUME_OF_INTEREST_VIEWS_VISIBLE=None
    WALKTHROUGH_FRAMES_COUNT=None
    WALL_ALIGN_KEY_REF_PARAM=None
    WALL_ATTR_DEFHEIGHT_PARAM=None
    WALL_ATTR_HEIGHT_PARAM=None
    WALL_ATTR_ROOM_BOUNDING=None
    WALL_ATTR_WIDTH_PARAM=None
    WALL_BASE_CONSTRAINT=None
    WALL_BASE_HEIGHT_PARAM=None
    WALL_BASE_OFFSET=None
    WALL_BOTTOM_EXTENSION_DIST_PARAM=None
    WALL_BOTTOM_IS_ATTACHED=None
    WALL_HEIGHT_TYPE=None
    WALL_KEY_REF_PARAM=None
    WALL_LOCATION_LINE_OFFSET_PARAM=None
    WALL_STRUCTURAL_SIGNIFICANT=None
    WALL_STRUCTURAL_USAGE_PARAM=None
    WALL_STRUCTURE_ID_PARAM=None
    WALL_SWEEP_CUTS_WALL_PARAM=None
    WALL_SWEEP_CUT_BY_INSERTS_PARAM=None
    WALL_SWEEP_DEFAULT_SETBACK_PARAM=None
    WALL_SWEEP_LEVEL_PARAM=None
    WALL_SWEEP_OFFSET_PARAM=None
    WALL_SWEEP_PROFILE_PARAM=None
    WALL_SWEEP_WALL_OFFSET_PARAM=None
    WALL_SWEEP_WALL_SUBCATEGORY_ID=None
    WALL_TOP_EXTENSION_DIST_PARAM=None
    WALL_TOP_IS_ATTACHED=None
    WALL_TOP_OFFSET=None
    WALL_USER_HEIGHT_PARAM=None
    WINDOW_CONSTRUCTION_TYPE=None
    WINDOW_HEIGHT=None
    WINDOW_INSET=None
    WINDOW_OPERATION_TYPE=None
    WINDOW_THICKNESS=None
    WINDOW_TYPE_ID=None
    WINDOW_WIDTH=None
    WITNS_LINE_EXTENSION=None
    WITNS_LINE_GAP_TO_ELT=None
    WITNS_LINE_TICK_MARK=None
    WRAPPING_AT_ENDS_PARAM=None
    WRAPPING_AT_INSERTS_PARAM=None
    YZ_JUSTIFICATION=None
    Y_JUSTIFICATION=None
    Y_OFFSET_VALUE=None
    ZONE_AIR_VOLUME_CALCULATION_TYPE_PARAM=None
    ZONE_AREA=None
    ZONE_AREA_GROSS=None
    ZONE_CALCULATED_AREA_PER_COOLING_LOAD_PARAM=None
    ZONE_CALCULATED_AREA_PER_HEATING_LOAD_PARAM=None
    ZONE_CALCULATED_COOLING_LOAD_PARAM=None
    ZONE_CALCULATED_COOLING_LOAD_PER_AREA_PARAM=None
    ZONE_CALCULATED_HEATING_LOAD_PARAM=None
    ZONE_CALCULATED_HEATING_LOAD_PER_AREA_PARAM=None
    ZONE_CALCULATED_SUPPLY_AIRFLOW_PARAM=None
    ZONE_CALCULATED_SUPPLY_AIRFLOW_PER_AREA_PARAM=None
    ZONE_COIL_BYPASS_PERCENTAGE_PARAM=None
    ZONE_COOLING_AIR_TEMPERATURE_PARAM=None
    ZONE_COOLING_INFORMATION_PARAM=None
    ZONE_COOLING_SET_POINT_PARAM=None
    ZONE_DEHUMIDIFICATION_SET_POINT_PARAM=None
    ZONE_HEATING_AIR_TEMPERATURE_PARAM=None
    ZONE_HEATING_INFORMATION_PARAM=None
    ZONE_HEATING_SET_POINT_PARAM=None
    ZONE_HUMIDIFICATION_SET_POINT_PARAM=None
    ZONE_LEVEL_ID=None
    ZONE_NAME=None
    ZONE_OA_RATE_PER_ACH_PARAM=None
    ZONE_OUTDOOR_AIR_INFORMATION_PARAM=None
    ZONE_OUTSIDE_AIR_PER_AREA_PARAM=None
    ZONE_OUTSIDE_AIR_PER_PERSON_PARAM=None
    ZONE_PERIMETER=None
    ZONE_PHASE=None
    ZONE_PHASE_ID=None
    ZONE_SERVICE_TYPE_PARAM=None
    ZONE_USE_AIR_CHANGES_PER_HOUR_PARAM=None
    ZONE_USE_DEHUMIDIFICATION_SETPOINT_PARAM=None
    ZONE_USE_HUMIDIFICATION_SETPOINT_PARAM=None
    ZONE_USE_OUTSIDE_AIR_PER_AREA_PARAM=None
    ZONE_USE_OUTSIDE_AIR_PER_PERSON_PARAM=None
    ZONE_VOLUME=None
    ZONE_VOLUME_GROSS=None
    Z_JUSTIFICATION=None
    Z_OFFSET_VALUE=None
class BuiltInParameterGroup(Enum):
    INVALID=None
    PG_ADSK_MODEL_PROPERTIES=None
    PG_AELECTRICAL=None
    PG_ANALYSIS_RESULTS=None
    PG_ANALYTICAL_ALIGNMENT=None
    PG_ANALYTICAL_MODEL=None
    PG_ANALYTICAL_PROPERTIES=None
    PG_AREA=None
    PG_CONCEPTUAL_ENERGY_DATA=None
    PG_CONCEPTUAL_ENERGY_DATA_BUILDING_SERVICES=None
    PG_CONSTRAINTS=None
    PG_CONSTRUCTION=None
    PG_CONTINUOUSRAIL_BEGIN_BOTTOM_EXTENSION=None
    PG_CONTINUOUSRAIL_END_TOP_EXTENSION=None
    PG_COUPLER_ARRAY=None
    PG_CURTAIN_GRID=None
    PG_CURTAIN_GRID_1=None
    PG_CURTAIN_GRID_2=None
    PG_CURTAIN_GRID_HORIZ=None
    PG_CURTAIN_GRID_U=None
    PG_CURTAIN_GRID_V=None
    PG_CURTAIN_GRID_VERT=None
    PG_CURTAIN_MULLION_1=None
    PG_CURTAIN_MULLION_2=None
    PG_CURTAIN_MULLION_HORIZ=None
    PG_CURTAIN_MULLION_VERT=None
    PG_DATA=None
    PG_DISPLAY=None
    PG_DIVISION_GEOMETRY=None
    PG_ELECTRICAL=None
    PG_ELECTRICAL_CIRCUITING=None
    PG_ELECTRICAL_LIGHTING=None
    PG_ELECTRICAL_LOADS=None
    PG_ENERGY_ANALYSIS=None
    PG_ENERGY_ANALYSIS_ADVANCED=None
    PG_ENERGY_ANALYSIS_BLDG_CONS_MTL_THERMAL_PROPS=None
    PG_ENERGY_ANALYSIS_BUILDING_DATA=None
    PG_ENERGY_ANALYSIS_CONCEPTUAL_MODEL=None
    PG_ENERGY_ANALYSIS_DETAILED_AND_CONCEPTUAL_MODELS=None
    PG_ENERGY_ANALYSIS_DETAILED_MODEL=None
    PG_ENERGY_ANALYSIS_ROOM_SPACE_DATA=None
    PG_FABRICATION_PRODUCT_DATA=None
    PG_FIRE_PROTECTION=None
    PG_FITTING=None
    PG_FLEXIBLE=None
    PG_FORCES=None
    PG_GENERAL=None
    PG_GEOMETRY=None
    PG_GEOMETRY_POSITIONING=None
    PG_GRAPHICS=None
    PG_GREEN_BUILDING=None
    PG_IDENTITY_DATA=None
    PG_IFC=None
    PG_INSULATION=None
    PG_LENGTH=None
    PG_LIGHT_PHOTOMETRICS=None
    PG_LINING=None
    PG_MATERIALS=None
    PG_MECHANICAL=None
    PG_MECHANICAL_AIRFLOW=None
    PG_MECHANICAL_LOADS=None
    PG_MOMENTS=None
    PG_NODES=None
    PG_OVERALL_LEGEND=None
    PG_PATTERN=None
    PG_PATTERN_APPLICATION=None
    PG_PHASING=None
    PG_PLUMBING=None
    PG_PRIMARY_END=None
    PG_PROFILE=None
    PG_PROFILE_1=None
    PG_PROFILE_2=None
    PG_RAILING_SYSTEM_FAMILY_HANDRAILS=None
    PG_RAILING_SYSTEM_FAMILY_SEGMENT_PATTERN=None
    PG_RAILING_SYSTEM_FAMILY_TOP_RAIL=None
    PG_RAILING_SYSTEM_SECONDARY_FAMILY_HANDRAILS=None
    PG_RAILING_SYSTEM_SEGMENT_PATTERN_REMAINDER=None
    PG_RAILING_SYSTEM_SEGMENT_PATTERN_REPEAT=None
    PG_RAILING_SYSTEM_SEGMENT_POSTS=None
    PG_RAILING_SYSTEM_SEGMENT_U_GRID=None
    PG_RAILING_SYSTEM_SEGMENT_V_GRID=None
    PG_REBAR_ARRAY=None
    PG_REBAR_SYSTEM_LAYERS=None
    PG_REFERENCE=None
    PG_RELEASES_MEMBER_FORCES=None
    PG_ROTATION_ABOUT=None
    PG_SECONDARY_END=None
    PG_SEGMENTS_FITTINGS=None
    PG_SLAB_SHAPE_EDIT=None
    PG_SPLIT_PROFILE_DIMENSIONS=None
    PG_STAIRS_CALCULATOR_RULES=None
    PG_STAIRS_OPEN_END_CONNECTION=None
    PG_STAIRS_SUPPORTS=None
    PG_STAIRS_TREADS_RISERS=None
    PG_STAIRS_WINDERS=None
    PG_STAIR_RISERS=None
    PG_STAIR_STRINGERS=None
    PG_STAIR_TREADS=None
    PG_STRUCTURAL=None
    PG_STRUCTURAL_ANALYSIS=None
    PG_SUPPORT=None
    PG_SYSTEMTYPE_RISEDROP=None
    PG_TERMINTATION=None
    PG_TEXT=None
    PG_TITLE=None
    PG_TRANSLATION_IN=None
    PG_TRUSS_FAMILY_BOTTOM_CHORD=None
    PG_TRUSS_FAMILY_DIAG_WEB=None
    PG_TRUSS_FAMILY_TOP_CHORD=None
    PG_TRUSS_FAMILY_VERT_WEB=None
    PG_UNDERLAY=None
    PG_VIEW_CAMERA=None
    PG_VIEW_EXTENTS=None
    PG_VISIBILITY=None
    value__=None
class CADExportOptions(object):
class CADLinkType(ElementType):
    def Dispose(self):
        pass
class CameraInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    FarDistance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalExtent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsPerspective=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsPespective=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NearDistance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RightOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TargetDistance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UpOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VerticalExtent=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CancellationListener(object):
    def Dispose(self):
        pass
    def IsCancelled(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CategoryNameMap(APIObject):
    def Clear(self):
        pass
    def Contains(self,key):
        pass
    def Dispose(self):
        pass
    def Erase(self,key):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,key,item):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Categories(CategoryNameMap):
    def Contains(self,name):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,key,item):
        pass
    def NewSubcategory(self,parentCategory,name):
        pass
    def ReverseIterator(self):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Category(APIObject):
    def Dispose(self):
        pass
    @staticmethod
    def GetCategory(document,categoryId):
        pass
    def GetGraphicsStyle(self,graphicsStyleType):
        pass
    def GetHashCode(self):
        pass
    def GetLinePatternId(self,graphicsStyleType):
        pass
    def GetLineWeight(self,graphicsStyleType):
        pass
    def SetLinePatternId(self,linePatternId,graphicsStyleType):
        pass
    def SetLineWeight(self,lineWeight,graphicsStyleType):
        pass
    AllowsBoundParameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanAddSubcategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CategoryType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasMaterialQuantities=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCuttable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTagCategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Material=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Parent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SubCategories=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CategoryNameMapIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Key=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CategorySet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CategorySetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CategoryType(Enum):
    AnalyticalModel=None
    Annotation=None
    Internal=None
    Invalid=None
    Model=None
    value__=None
class HostObject(Element):
    def Dispose(self):
        pass
    def FindInserts(self,addRectOpenings,includeShadows,includeEmbeddedWalls,includeSharedEmbeddedInserts):
        pass
class CeilingAndFloor(HostObject):
    def Dispose(self):
        pass
class Ceiling(CeilingAndFloor):
    def Dispose(self):
        pass
class CeilingType(HostObjAttributes):
    def Dispose(self):
        pass
    ThermalProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CellType(Enum):
    CalculatedValue=None
    CombinedParameter=None
    Graphic=None
    Inherited=None
    Parameter=None
    ParameterText=None
    Text=None
    value__=None
class ChangePriority(Enum):
    Annotations=None
    Connections=None
    DetailComponents=None
    DoorsOpeningsWindows=None
    FloorsRoofsStructuralWalls=None
    FreeStandingComponents=None
    GridsLevelsReferencePlanes=None
    InteriorWalls=None
    Masses=None
    MEPAccessoriesFittingsSegmentsWires=None
    MEPCalculations=None
    MEPFixtures=None
    MEPSystems=None
    Rebar=None
    RoomsSpacesZones=None
    Structure=None
    value__=None
    Views=None
class ChangeType(object):
    @staticmethod
    def ConcatenateChangeTypes(changeType1,changeType2):
        pass
    def Contains(self,changeType):
        pass
    def Dispose(self):
        pass
    def IsIdentical(self,changeType):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CheckoutStatus(Enum):
    NotOwned=None
    OwnedByCurrentUser=None
    OwnedByOtherUser=None
    value__=None
class City(APIObject):
    def Dispose(self):
        pass
    Latitude=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Longitude=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TimeZone=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WeatherStation=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CitySet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CitySetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class KeyBasedTreeEntries(object):
    def Dispose(self):
        pass
    def FindEntry(self,key):
        pass
    def GetEnumerator(self):
        pass
    def GetKeyBasedTreeEntriesIterator(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ClassificationEntries(KeyBasedTreeEntries):
    def Dispose(self):
        pass
    @staticmethod
    def LoadClassificationEntriesFromFile(filePath,loadContent):
        pass
class KeyBasedTreeEntry(object):
    def Dispose(self):
        pass
    def GetChildrenKeys(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Key=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParentKey=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ClassificationEntry(KeyBasedTreeEntry):
    def Dispose(self):
        pass
    def HasBadCategoryId(self):
        pass
    def HasBadLevel(self):
        pass
    def HasInvalidKey(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,key,parentKey,description,level,categoryId):
        pass
    CategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Level=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Color(APIObject):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,red,green,blue):
        pass
    Blue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Green=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValid=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Red=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InvalidColorValue=None
class ColorBackgroundSettings(BackgroundSettings):
    def Dispose(self):
        pass
    Color=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ColorDepthType(Enum):
    BlackLine=None
    Color=None
    GrayScale=None
    value__=None
class ColorWithTransparency(object):
    def Dispose(self):
        pass
    def GetBlue(self):
        pass
    def GetColor(self):
        pass
    def GetGreen(self):
        pass
    def GetRed(self):
        pass
    def GetTransparency(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetBlue(self,blue):
        pass
    def SetColor(self,color):
        pass
    def SetGreen(self,green):
        pass
    def SetRed(self,red):
        pass
    def SetTransparency(self,transparency):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,red=None,green=None,blue=None,transparency=None):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ColumnAttachment(object):
    @staticmethod
    def AddColumnAttachment(doc,column,target,baseOrTop,cutColumnStyle,justification,attachOffset):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetColumnAttachment(column,*__args):
        pass
    @staticmethod
    def IsValidColumn(familyInstance):
        pass
    @staticmethod
    def IsValidTarget(*__args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    @staticmethod
    def RemoveColumnAttachment(column,*__args):
        pass
    def SetJustification(self,justification):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AttachOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BaseOrTop=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Justification=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TargetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ColumnAttachmentCutStyle(Enum):
    CutColumn=None
    CutTarget=None
    None_JEDIFIX=None
    value__=None
class ColumnAttachmentJustification(Enum):
    Maximum=None
    Midpoint=None
    Minimum=None
    Tangent=None
    value__=None
class CombinableElementArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CombinableElementArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ComponentRepeater(Element):
    @staticmethod
    def CanElementBeRepeated(ADoc,elementId):
        pass
    def Dispose(self):
        pass
    def GetEnumerator(self):
        pass
    def IsTypeValidForRepeater(self,typeId):
        pass
    @staticmethod
    def RemoveRepeaters(document,elementIds):
        pass
    @staticmethod
    def RepeatElements(document,elementIds):
        pass
    def __contains__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    DefaultFamilyType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DimensionCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ComponentRepeaterIterator(object):
    def Dispose(self):
        pass
    def GetCurrent(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ComponentRepeaterSlot(Element):
    def Dispose(self):
        pass
    def IsTypeValidForSlot(self,typeId):
        pass
    def MakeDefault(self):
        pass
    def MakeEmpty(self):
        pass
    FamilyType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsDefault=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ComponentRotation(Enum):
    Angle0=None
    Angle180=None
    Angle270=None
    Angle90=None
    value__=None
class CompoundStructure(object):
    def AddWallSweep(self,wallSweepInfo):
        pass
    def AssociateRegionWithLayer(self,regionId,layerIdx):
        pass
    def CanLayerBeStructuralMaterial(self,layerIndex):
        pass
    def CanLayerBeVariable(self,variableLayerIndex):
        pass
    def CanLayerWidthBeNonZero(self,layerIdx):
        pass
    def ChangeRegionWidth(self,regionId,newWidth):
        pass
    def ClearWallSweeps(self,wallSweepType):
        pass
    @staticmethod
    def CreateSimpleCompoundStructure(layers):
        pass
    @staticmethod
    def CreateSingleLayerCompoundStructure(*__args):
        pass
    def DeleteLayer(self,layerIdx):
        pass
    def Dispose(self):
        pass
    def FindEnclosingRegionAndSegments(self,gridUV,splitDirection,segmentId1,segmentId2):
        pass
    def GetAdjacentRegions(self,segmentId):
        pass
    def GetCoreBoundaryLayerIndex(self,shellLayerType):
        pass
    def GetDeckEmbeddingType(self,layerIdx):
        pass
    def GetDeckProfileId(self,layerIdx):
        pass
    def GetExtendableRegionIds(self,top):
        pass
    def GetFirstCoreLayerIndex(self):
        pass
    def GetLastCoreLayerIndex(self):
        pass
    def GetLayerAssociatedToRegion(self,regionId):
        pass
    def GetLayerFunction(self,layerIdx):
        pass
    def GetLayers(self):
        pass
    def GetLayerWidth(self,layerIdx):
        pass
    def GetMaterialId(self,layerIdx):
        pass
    @staticmethod
    def GetMinimumLayerThickness():
        pass
    def GetNumberOfShellLayers(self,shellLayerType):
        pass
    def GetOffsetForLocationLine(self,wallLocationLine):
        pass
    def GetPreviousNonZeroLayerIndex(self,thisIdx):
        pass
    def GetRegionEnvelope(self,regionId):
        pass
    def GetRegionIds(self):
        pass
    def GetRegionsAlongLevel(self,height):
        pass
    def GetRegionsAssociatedToLayer(self,layerIdx):
        pass
    def GetSegmentCoordinate(self,segmentId):
        pass
    def GetSegmentEndPoints(self,segmentId,regionId,end1,end2):
        pass
    def GetSegmentIds(self):
        pass
    def GetSegmentOrientation(self,segmentId):
        pass
    def GetSimpleCompoundStructure(self,wallHeight,distAboveBase):
        pass
    def GetWallSweepsInfo(self,wallSweepType):
        pass
    def GetWidth(self,regionId=None):
        pass
    def IsCoreLayer(self,layerIdx):
        pass
    def IsEqual(self,otherStructure):
        pass
    def IsLayerValid(self,layerIdx,layer):
        pass
    def IsRectangularRegion(self,regionId):
        pass
    def IsSimpleRegion(self,regionId):
        pass
    def IsStructuralDeck(self,layerIdx):
        pass
    def IsValid(self,doc,errMap,twoLayerErrorsMap):
        pass
    def IsValidRegionId(self,regionId):
        pass
    def IsValidSampleHeight(self,height):
        pass
    def IsValidSegmentId(self,segmentId):
        pass
    def IsVerticallyHomogeneous(self):
        pass
    def MergeRegionsAdjacentToSegment(self,segmentId,layerIdxForMergedRegion):
        pass
    def ParticipatesInWrapping(self,layerIdx):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveWallSweep(self,wallSweepType,id):
        pass
    def SetDeckEmbeddingType(self,layerIdx,embedType):
        pass
    def SetDeckProfileId(self,layerIdx,profileId):
        pass
    def SetExtendableRegionIds(self,top,regionIds):
        pass
    def SetLayer(self,layerIdx,layer):
        pass
    def SetLayerFunction(self,layerIdx,function):
        pass
    def SetLayers(self,layers):
        pass
    def SetLayerWidth(self,layerIdx,width):
        pass
    def SetMaterialId(self,layerIdx,materialId):
        pass
    def SetNumberOfShellLayers(self,shellLayerType,numLayers):
        pass
    def SetParticipatesInWrapping(self,layerIdx,participatesInWrapping):
        pass
    def SplitRegion(self,gridUV,splitDirection,newSegmentId=None):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    CutoffHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EndCap=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasStructuralDeck=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsVerticallyCompound=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LayerCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinimumSampleHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OpeningWrapping=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SampleHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralMaterialIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VariableLayerIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CompoundStructureError(Enum):
    BadShellOrder=None
    BadShellsStructure=None
    CoreTooThin=None
    DeckCantBoundAbove=None
    DeckCantBoundBelow=None
    ExtensibleRegionsNotContiguousAlongBottom=None
    ExtensibleRegionsNotContiguousAlongTop=None
    InvalidMaterialId=None
    InvalidProfileId=None
    MembraneTooThick=None
    NonmembraneTooThin=None
    ThinOuterLayer=None
    value__=None
    VarThickLayerCantBeZero=None
    VerticalUnusedLayer=None
    VerticalWrongOrderCoreExterior=None
    VerticalWrongOrderCoreInterior=None
    VerticalWrongOrderLayer=None
    VerticalWrongOrderMembrane=None
class CompoundStructureLayer(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    DeckEmbeddingType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DeckProfileId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Function=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LayerCapFlag=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LayerId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConfigurationReloadInfo(object):
    def Dispose(self):
        pass
    def GetConnectivityValidation(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Disconnects=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileNotAvailable=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Face(GeometryObject):
    def ComputeDerivatives(self,point):
        pass
    def ComputeNormal(self,point):
        pass
    def ComputeSecondDerivatives(self,point):
        pass
    def Dispose(self):
        pass
    def Evaluate(self,params):
        pass
    def GetBoundingBox(self):
        pass
    def GetEdgesAsCurveLoops(self):
        pass
    def GetRegions(self):
        pass
    def Intersect(self,*__args):
        pass
    def IsInside(self,point,result=None):
        pass
    def Project(self,point):
        pass
    def Triangulate(self,levelOfDetail=None):
        pass
    Area=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EdgeLoops=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasRegions=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTwoSided=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Reference=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConicalFace(Face):
    def Dispose(self):
        pass
    Axis=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HalfAngle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Surface(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConicalSurface(Surface):
    @staticmethod
    def Create(frameOfReference,halfAngle):
        pass
    def Dispose(self):
        pass
    def GetFrameOfReference(self):
        pass
    @staticmethod
    def IsValidConeAngle(halfAngle):
        pass
    Axis=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HalfAngle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XDir=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YDir=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConnectionResolution(Enum):
    Disconnected=None
    value__=None
class ConnectionValidationInfo(object):
    def Dispose(self):
        pass
    def GetWarning(self,index):
        pass
    def IsValidWarningIndex(self,index):
        pass
    def ManyWarnings(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConnectionValidationWarning(object):
    def Dispose(self):
        pass
    def GetParts(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,resolution,reason,part1,part2):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Reason=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Resolution=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConnectionWarning(Enum):
    Alignment=None
    Connectivity=None
    Shape=None
    Size=None
    Unknown=None
    value__=None
class Connector(object):
    def ConnectTo(self,connector):
        pass
    def DisconnectFrom(self,connector):
        pass
    def Dispose(self):
        pass
    def GetFabricationConnectorInfo(self):
        pass
    def GetMEPConnectorInfo(self):
        pass
    def IsConnectedTo(self,connector):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AllowsSlopeAdjustments=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AllRefs=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Angle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedDuctFlowConfiguration=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedDuctLossMethod=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedFixtureUnits=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedFlow=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedFlowDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedFlowFactor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedKCoefficient=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedLossCoefficient=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedPipeFlowConfiguration=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedPipeLossMethod=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssignedPressureDrop=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Coefficient=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConnectorManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConnectorType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CoordinateSystem=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Demand=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Direction=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Domain=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DuctSystemType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ElectricalSystemType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EngagementLength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Flow=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Height=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsConnected=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsMovable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MEPSystem=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Owner=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PipeSystemType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PressureDrop=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Radius=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Shape=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Utility=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VelocityPressure=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConnectorDomainType(Enum):
    CableTrayConduit=None
    Electrical=None
    Hvac=None
    Piping=None
    StructuralAnalytical=None
    Undefined=None
    value__=None
class ConnectorElement(Element):
    def AssignAsPrimary(self):
        pass
    @staticmethod
    def CreateCableTrayConnector(document,planarFace,edge=None):
        pass
    @staticmethod
    def CreateConduitConnector(document,planarFace,edge=None):
        pass
    @staticmethod
    def CreateDuctConnector(document,ductSystemType,profileShape,planarFace,edge=None):
        pass
    @staticmethod
    def CreateElectricalConnector(document,electricalSystemType,planarFace,edge=None):
        pass
    @staticmethod
    def CreatePipeConnector(document,pipeSystemType,planarFace,edge=None):
        pass
    def Dispose(self):
        pass
    def FlipDirection(self):
        pass
    def GetLinkedConnectorElement(self):
        pass
    def IsSystemClassificationValid(self,systemClassification):
        pass
    def SetLinkedConnectorElement(self,otherConnector):
        pass
    CoordinateSystem=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Direction=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Domain=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Height=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsPrimary=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Radius=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Shape=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SystemClassification=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConnectorGenderType(Enum):
    Female=None
    Male=None
    Undefined=None
    value__=None
class ConnectorJointType(Enum):
    Flanged=None
    Glued=None
    Grooved=None
    Soldered=None
    Threaded=None
    Undefined=None
    value__=None
    Welded=None
class ConnectorManager(object):
    def Dispose(self):
        pass
    def Lookup(self,index):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Connectors=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Owner=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UnusedConnectors=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConnectorProfileType(Enum):
    Invalid=None
    Oval=None
    Rectangular=None
    Round=None
    value__=None
class ConnectorSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConnectorSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ConnectorType(Enum):
    AllModes=None
    AnyEnd=None
    BlankEnd=None
    Curve=None
    End=None
    EndSurface=None
    Family=None
    Invalid=None
    Logical=None
    MasterSurface=None
    NodeReference=None
    NonEnd=None
    Physical=None
    Reference=None
    Surface=None
    value__=None
class Construction(object):
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RenderNode(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NodeName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ContentNode(RenderNode):
    def Dispose(self):
        pass
    def GetAsset(self):
        pass
    def GetTransform(self):
        pass
class Control(Element):
    def Dispose(self):
        pass
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Shape=property(lambda self:object(),lambda self,v:None,lambda self:None)
    View=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ControlShape(Enum):
    DoubleHorizontalArrow=None
    DoubleVerticalArrow=None
    HorizontalArrow=None
    value__=None
    VerticalArrow=None
class CoordinatePlaneVisibility(Enum):
    Always=None
    Never=None
    value__=None
    WhenSelected=None
class CopyPasteOptions(object):
    def Dispose(self):
        pass
    def GetDuplicateTypeNamesHandler(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetDuplicateTypeNamesHandler(self,handler):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurtainCell(APIObject):
    def Dispose(self):
        pass
    CurveLoops=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PlanarizedCurveLoops=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurtainGrid(APIObject):
    def AddGridLine(self,isUGridLine,position,oneSegmentOnly):
        pass
    def ChangePanelType(self,panel,newSymbol):
        pass
    def Dispose(self):
        pass
    def GetCell(self,uGridLineId,vGridLineId):
        pass
    def GetCurtainCells(self):
        pass
    def GetMullionIds(self):
        pass
    def GetPanel(self,uGridLineId,vGridLineId):
        pass
    def GetPanelIds(self):
        pass
    def GetUGridLineIds(self):
        pass
    def GetUnlockedMullionIds(self):
        pass
    def GetUnlockedPanelIds(self):
        pass
    def GetVGridLineIds(self):
        pass
    Grid1Angle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Grid1Justification=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Grid1Offset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Grid2Angle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Grid2Justification=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Grid2Offset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumPanels=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumULines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumVLines=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurtainGridAlignType(Enum):
    Beginning=None
    Center=None
    End=None
    NoJustify=None
    value__=None
class CurtainGridLine(HostObject):
    def AddAllSegments(self):
        pass
    def AddMullions(self,segment,mullionType,oneSegmentOnly):
        pass
    def AddSegment(self,curve):
        pass
    def Dispose(self):
        pass
    def RemoveSegment(self,curve):
        pass
    AllSegmentCurves=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExistingSegmentCurves=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FullCurve=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsUGridLine=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Lock=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SkippedSegmentCurves=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurtainGridSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurtainGridSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurtainSystemBase(HostObject):
    def Dispose(self):
        pass
class CurtainSystem(CurtainSystemBase):
    def AddCurtainGrid(self,face):
        pass
    def Dispose(self):
        pass
    def RemoveCurtainGrid(self,face):
        pass
    CurtainGrids=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CurtainSystemType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurtainSystemType(HostObjAttributes):
    def Dispose(self):
        pass
class CurveArrArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveArrArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveElement(Element):
    def Dispose(self):
        pass
    def GetAdjoinedCurveElements(self,end):
        pass
    def GetLineStyleIds(self):
        pass
    def GetTangentLock(self,end,other):
        pass
    def HasTangentJoin(self,end,other):
        pass
    def HasTangentLocks(self,end):
        pass
    def IsAdjoinedCurveElement(self,end,other):
        pass
    def SetGeometryCurve(self,curve,overrideJoins):
        pass
    def SetSketchPlaneAndCurve(self,sketchPlane,curve):
        pass
    def SetTangentLock(self,end,other,state):
        pass
    CenterPointReference=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CurveElementType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GeometryCurve=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SketchPlane=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SupportsTangentLocks=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveByPoints(CurveElement):
    def Dispose(self):
        pass
    def GetPoints(self):
        pass
    def GetVisibility(self):
        pass
    def SetPoints(self,points):
        pass
    def SetVisibility(self,visibility):
        pass
    @staticmethod
    def SortPoints(arr):
        pass
    IsReferenceLine=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReferenceType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SketchPlane=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Subcategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visible=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveByPointsArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveByPointsArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveByPointsUtils(object):
    @staticmethod
    def AddCurvesToFaceRegion(document,curveElemIds):
        pass
    @staticmethod
    def CreateArcThroughPoints(document,startPoint,endPoint,interiorPoint):
        pass
    @staticmethod
    def CreateRectangle(document,startPoint,endPoint,projectionType,boundaryReferenceLines,boundaryCurvesFollowSurface,createdCurvesIds,createdCornersIds):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetFaceRegions(cda,referenceOfFace):
        pass
    @staticmethod
    def GetHostFace(curveElem):
        pass
    @staticmethod
    def GetProjectionType(curveElem):
        pass
    @staticmethod
    def GetSketchOnSurface(curveElem):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    @staticmethod
    def SetProjectionType(curveElem,value):
        pass
    @staticmethod
    def SetSketchOnSurface(curveElem,sketchOnSurface):
        pass
    @staticmethod
    def ValidateCurveElementIdArrayForFaceRegions(document,curveElemIds):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveElementFilter(ElementSlowFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,curveElementType,inverted=None):
        pass
    CurveElementType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveElementType(Enum):
    AreaSeparation=None
    Cloud=None
    CurveByPoints=None
    DetailCurve=None
    Insulation=None
    Invalid=None
    ModelCurve=None
    ReferenceLine=None
    RepeatingDetail=None
    RoomSeparation=None
    SpaceSeparation=None
    SymbolicCurve=None
    value__=None
class CurveExtents(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EndParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveLoop(object):
    def Append(self,curve):
        pass
    @staticmethod
    def Create(curves):
        pass
    @staticmethod
    def CreateViaCopy(original):
        pass
    @staticmethod
    def CreateViaOffset(original,offsetDist,normal):
        pass
    @staticmethod
    def CreateViaThicken(*__args):
        pass
    @staticmethod
    def CreateViaTransform(curveLoop,transform):
        pass
    def Dispose(self):
        pass
    def Flip(self):
        pass
    def GetCurveLoopIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def GetExactLength(self):
        pass
    def GetPlane(self):
        pass
    def GetRectangularHeight(self,plane):
        pass
    def GetRectangularWidth(self,plane):
        pass
    def HasPlane(self):
        pass
    def IsCounterclockwise(self,normal):
        pass
    def IsOpen(self):
        pass
    def IsRectangular(self,plane):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Transform(self,transform):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveLoopIterator(object):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SweepProfile(APIObject):
    def Dispose(self):
        pass
class CurveLoopsProfile(SweepProfile):
    def Dispose(self):
        pass
    Profile=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ModelCurveNode(RenderNode):
    def Dispose(self):
        pass
    LineProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CurveNode(ModelCurveNode):
    def Dispose(self):
        pass
    def GetCurve(self):
        pass
class CurveProjectionType(Enum):
    FollowSurfaceUV=None
    FromTopDown=None
    ParallelToLevel=None
    value__=None
class CustomExporter(object):
    def Dispose(self):
        pass
    def Export(self,*__args):
        pass
    @staticmethod
    def IsRenderingSupported():
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document,context):
        pass
    IncludeGeometricObjects=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShouldStopOnError=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CutFailureReason(Enum):
    CutAllowed=None
    CutAlreadyExists=None
    CutNotAppropriateForElements=None
    OppositeCutExists=None
    value__=None
class CylindricalFace(Face):
    def Dispose(self):
        pass
    Axis=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CylindricalHelix(Curve):
    @staticmethod
    def Create(basePoint,radius,xVector,zVector,pitch,startAngle,endAngle):
        pass
    def Dispose(self):
        pass
    BasePoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Height=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsRightHanded=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Pitch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Radius=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XVector=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YVector=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ZVector=property(lambda self:object(),lambda self,v:None,lambda self:None)
class CylindricalSurface(Surface):
    @staticmethod
    def Create(frameOfReference,radius):
        pass
    def Dispose(self):
        pass
    def GetFrameOfReference(self):
        pass
    Axis=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Radius=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XDir=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YDir=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DataConversionMonitorScope(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,IDCM):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DataExchangeMessageId(Enum):
    EmptyObject=None
    GenericError=None
    InvalidDataSet=None
    InvalidRenderingStyle=None
    InvalidSourceObject=None
    None_JEDIFIX=None
    ObjectCreated=None
    ObjectNotConverted=None
    ObjectNotSupported=None
    UnexpectedResult=None
    UnitOfProgressCompleted=None
    value__=None
class DataExchangeMessageSeverity(Enum):
    Error=None
    FatalError=None
    Info=None
    value__=None
    Warning=None
class DataExchangeMessageVerbosity(Enum):
    Default=None
    Minimal=None
    value__=None
    Verbose=None
class DatumEnds(Enum):
    End0=None
    End1=None
    value__=None
class DatumExtentType(Enum):
    Model=None
    value__=None
    ViewSpecific=None
class DatumPlane(Element):
    def AddLeader(self,datumEnd,view):
        pass
    def CanBeVisibleInView(self,view):
        pass
    def Dispose(self):
        pass
    def GetCurvesInView(self,extentMode,view):
        pass
    def GetDatumExtentTypeInView(self,datumEnd,view):
        pass
    def GetLeader(self,datumEnd,view):
        pass
    def GetPropagationViews(self,view):
        pass
    def HasBubbleInView(self,datumEnd,view):
        pass
    def HideBubbleInView(self,datumEnd,view):
        pass
    def IsBubbleVisibleInView(self,datumEnd,view):
        pass
    def IsCurveValidInView(self,extentMode,view,curve):
        pass
    def IsLeaderValid(self,datumEnd,view,leader):
        pass
    def Maximize3DExtents(self):
        pass
    def PropagateToViews(self,view,parallelViews):
        pass
    def SetCurveInView(self,extentMode,view,curve):
        pass
    def SetDatumExtentType(self,datumEnd,view,extentMode):
        pass
    def SetLeader(self,datumEnd,view,pLeader):
        pass
    def ShowBubbleInView(self,datumEnd,view):
        pass
class DecimalSymbol(Enum):
    Comma=None
    Dot=None
    value__=None
class DefaultDivideSettings(Element):
    def Dispose(self):
        pass
    @staticmethod
    def GetDefaultDivideSettings(cda):
        pass
    def GetSurfaceDistance(self,gridlines):
        pass
    def GetSurfaceLayout(self,gridlines):
        pass
    def GetSurfaceNumber(self,gridlines):
        pass
    def SetSurfaceDistance(self,gridlines,distance):
        pass
    def SetSurfaceLayout(self,gridlines,layout):
        pass
    def SetSurfaceNumber(self,gridlines,number):
        pass
    PathDistance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathLayout=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathMeasurementType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Definition(object):
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterGroup=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UnitType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DefinitionBindingMapIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Key=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DefinitionFile(APIObject):
    def Dispose(self):
        pass
    Filename=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Groups=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DefinitionGroup(APIObject):
    def Dispose(self):
        pass
    Definitions=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DefinitionGroups(object):
    def Contains(self,definitionGroup):
        pass
    def Create(self,name):
        pass
    def Dispose(self):
        pass
    def GetEnumerator(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Definitions(object):
    def Contains(self,definition):
        pass
    def Create(self,option):
        pass
    def Dispose(self):
        pass
    def GetEnumerator(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureResolution(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DeleteElements(FailureResolution):
    @staticmethod
    def Create(document,*__args):
        pass
    def Dispose(self):
        pass
class DesignOption(Element):
    def Dispose(self):
        pass
    @staticmethod
    def GetActiveDesignOptionId(document):
        pass
    IsPrimary=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DetachFromCentralOption(Enum):
    ClearTransmittedSaveAsNewCentral=None
    DetachAndDiscardWorksets=None
    DetachAndPreserveWorksets=None
    DoNotDetach=None
    value__=None
class DetailCurve(CurveElement):
    def Dispose(self):
        pass
class DetailArc(DetailCurve):
    def Dispose(self):
        pass
class DetailCurveArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DetailCurveArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DetailElementOrderUtils(object):
    @staticmethod
    def AreDetailElements(pDocument,pDBView,detailElementIds):
        pass
    @staticmethod
    def BringForward(pDocument,pDBView,*__args):
        pass
    @staticmethod
    def BringToFront(pDocument,pDBView,*__args):
        pass
    @staticmethod
    def IsDetailElement(pDocument,pDBView,detailElementId):
        pass
    @staticmethod
    def SendBackward(pDocument,pDBView,*__args):
        pass
    @staticmethod
    def SendToBack(pDocument,pDBView,*__args):
        pass
    __all__=[
        'AreDetailElements',
        'BringForward',
        'BringToFront',
        'IsDetailElement',
        'SendBackward',
        'SendToBack',
    ]
class DetailEllipse(DetailCurve):
    def Dispose(self):
        pass
class DetailLine(DetailCurve):
    def Dispose(self):
        pass
class DetailNurbSpline(DetailCurve):
    def Dispose(self):
        pass
class DGNExportOptions(BaseExportOptions):
    def Dispose(self):
        pass
    def GetExportLineweightTable(self):
        pass
    @staticmethod
    def GetPredefinedOptions(document,setup):
        pass
    @staticmethod
    def GetPredefinedSetupNames(document):
        pass
    def SetExportLineweightTable(self,lineweightTable):
        pass
    @staticmethod # known case of __new__
    def __new__(self,option=None):
        pass
    FileVersion=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MasterUnits=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MergedViews=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SeedName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DGNFileFormat(Enum):
    Default=None
    DGNVersion7=None
    DGNVersion8=None
    value__=None
class DGNImportOptions(BaseImportOptions):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,option=None):
        pass
    DGNModelViewName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IgnoreUnsupportedElementWarning=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DigitGroupingAmount(Enum):
    Three=None
    Two=None
    value__=None
class DigitGroupingSymbol(Enum):
    Apostrophe=None
    Comma=None
    Dot=None
    Space=None
    Tick=None
    value__=None
class DimensionEqualityLabelFormatting(object):
    def Dispose(self):
        pass
    def GetFormatOptions(self):
        pass
    def IsValidFormatOptions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetFormatOptions(self,formatOptions):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,leadingSpaces,prefix,labelType,suffix,formatOptions):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LabelType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeadingSpaces=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Prefix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Suffix=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DimensionSegment(APIObject):
    def Dispose(self):
        pass
    def IsTextPositionAdjustable(self):
        pass
    def ResetTextPosition(self):
        pass
    Above=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Below=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsLocked=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderEndPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Prefix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Suffix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Value=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ValueOverride=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ValueString=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DimensionSegmentArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DimensionSegmentArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DimensionShape(Enum):
    Angular=None
    ArcLength=None
    Diameter=None
    Linear=None
    Radial=None
    Spot=None
    Unknown=None
    value__=None
class DimensionStyleType(Enum):
    Angular=None
    ArcLength=None
    Diameter=None
    Linear=None
    LinearFixed=None
    Radial=None
    SpotCoordinate=None
    SpotElevation=None
    SpotSlope=None
    value__=None
class DimensionType(ElementType):
    def CanHaveEqualityFormula(self):
        pass
    def CanHaveOrdinateDimensionSetting(self):
        pass
    def Dispose(self):
        pass
    def GetAlternateUnitsFormatOptions(self):
        pass
    def GetEqualityFormula(self):
        pass
    def GetOrdinateDimensionSetting(self):
        pass
    def GetUnitsFormatOptions(self):
        pass
    def SetAlternateUnitsFormatOptions(self,formatOptions):
        pass
    def SetEqualityFormula(self,formattingArr):
        pass
    def SetOrdinateDimensionSetting(self,ordinateDimSetting):
        pass
    def SetUnitsFormatOptions(self,formatOptions):
        pass
    AlternateUnits=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AlternateUnitsPrefix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AlternateUnitsSuffix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StyleType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UnitType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DirectShape(Element):
    def AppendShape(self,*__args):
        pass
    def AreOptionsValid(self,options):
        pass
    def AreOptionsValidForTransientDirectShape(self,options):
        pass
    @staticmethod
    def CreateElement(document,categoryId,applicationId=None,applicationDataId=None):
        pass
    @staticmethod
    def CreateElementInstance(document,typeId,categoryId,definitionId,trf,applicationId=None,applicationDataId=None):
        pass
    @staticmethod
    def CreateGeometryInstance(document,definition_id,trf):
        pass
    def Dispose(self):
        pass
    def GetOptions(self):
        pass
    @staticmethod
    def IsSupportedDocument(document):
        pass
    @staticmethod
    def IsValidCategoryId(categoryId,doc):
        pass
    def IsValidGeometry(self,Geom):
        pass
    def IsValidShape(self,shape,viewType=None):
        pass
    def IsValidTypeId(self,typeId):
        pass
    def SetGUIDs(self,appGUID,appDataGUID):
        pass
    def SetName(self,name):
        pass
    def SetOptions(self,options):
        pass
    def SetShape(self,*__args):
        pass
    def SetTypeId(self,typeId):
        pass
    ApplicationDataId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ApplicationId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TypeId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DirectShapeLibrary(object):
    def AddDefinition(self,id,*__args):
        pass
    def AddDefinitionType(self,id,typeId):
        pass
    def Contains(self,id):
        pass
    def ContainsType(self,name):
        pass
    def Dispose(self):
        pass
    def FindDefinition(self,id):
        pass
    def FindDefinitionType(self,id):
        pass
    @staticmethod
    def GetDirectShapeLibrary(ADoc):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DirectShapeOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReferencingOption=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RoomBoundingOption=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DirectShapeReferencingOption(Enum):
    NotReferenceable=None
    Referenceable=None
    value__=None
class DirectShapeRoomBoundingOption(Enum):
    NotApplicable=None
    SetByParameter=None
    value__=None
class DirectShapeTargetViewType(Enum):
    Default=None
    Plan=None
    Undefined=None
    value__=None
class DirectShapeType(ElementType):
    def AppendShape(self,*__args):
        pass
    @staticmethod
    def Create(document,name,categoryId):
        pass
    def Dispose(self):
        pass
    def IsValidShape(self,shape,viewType=None):
        pass
    def SetShape(self,*__args):
        pass
class DisplacementElement(Element):
    @staticmethod
    def CanCategoryBeDisplaced(categoryId):
        pass
    def CanElementsBeAddedToDisplacementSet(self,toDisplace):
        pass
    @staticmethod
    def CanElementsBeDisplaced(view,elementIds,commonDisplacedElementId=None):
        pass
    @staticmethod
    def Create(document,elementsToDisplace,displacement,ownerDBView,parentDisplacementElement):
        pass
    def Dispose(self):
        pass
    def GetAbsoluteDisplacement(self):
        pass
    @staticmethod
    def GetAdditionalElementsToDisplace(document,view,idToDisplace):
        pass
    def GetChildren(self):
        pass
    def GetDisplacedElementIds(self,view=None):
        pass
    def GetDisplacedElementIdsFromAllChildren(self):
        pass
    @staticmethod
    def GetDisplacementElementId(view,id):
        pass
    @staticmethod
    def GetDisplacementElementIds(view):
        pass
    def GetRelativeDisplacement(self):
        pass
    @staticmethod
    def IsAllowedAsDisplacedElement(element):
        pass
    @staticmethod
    def IsElementDisplacedInView(view,id):
        pass
    @staticmethod
    def IsNotEmpty(elementIds):
        pass
    @staticmethod
    def IsValidAsParentInView(view,parent):
        pass
    def RemoveDisplacedElement(self,ElemToRemove):
        pass
    def ResetDisplacedElements(self):
        pass
    def SetDisplacedElementIds(self,displacedElemIds):
        pass
    def SetRelativeDisplacement(self,displacement):
        pass
    ParentId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DisplacementPath(Element):
    @staticmethod
    def Create(aDoc,displacementElement,reference,param):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def IsValidParam(param):
        pass
    @staticmethod
    def IsValidReference(displacementElement,reference):
        pass
    def SetAnchorPoint(self,displacementElement,reference,param):
        pass
    AncestorIdx=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DisplacementPathStyle(Enum):
    Jogged=None
    Straight=None
    value__=None
class DisplayStyle(Enum):
    FlatColors=None
    HLR=None
    Raytrace=None
    Realistic=None
    RealisticWithEdges=None
    Rendering=None
    Shading=None
    ShadingWithEdges=None
    Undefined=None
    value__=None
    Wireframe=None
class DisplayUnit(Enum):
    IMPERIAL=None
    METRIC=None
    value__=None
class DisplayUnitType(Enum):
    DUT_1_RATIO=None
    DUT_ACRES=None
    DUT_AMPERES=None
    DUT_ATMOSPHERES=None
    DUT_BARS=None
    DUT_BRITISH_THERMAL_UNITS=None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR=None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR_CUBIC_FOOT=None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR_FOOT_FAHRENHEIT=None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR_SQUARE_FOOT=None
    DUT_BRITISH_THERMAL_UNITS_PER_HOUR_SQUARE_FOOT_FAHRENHEIT=None
    DUT_BRITISH_THERMAL_UNITS_PER_POUND=None
    DUT_BRITISH_THERMAL_UNITS_PER_POUND_FAHRENHEIT=None
    DUT_BRITISH_THERMAL_UNITS_PER_SECOND=None
    DUT_BRITISH_THERMAL_UNIT_PER_FAHRENHEIT=None
    DUT_CALORIES=None
    DUT_CALORIES_PER_SECOND=None
    DUT_CANDELAS=None
    DUT_CANDELAS_PER_SQUARE_METER=None
    DUT_CANDLEPOWER=None
    DUT_CELSIUS=None
    DUT_CELSIUS_DIFFERENCE=None
    DUT_CENTIMETERS=None
    DUT_CENTIMETERS_PER_MINUTE=None
    DUT_CENTIMETERS_TO_THE_FOURTH_POWER=None
    DUT_CENTIMETERS_TO_THE_SIXTH_POWER=None
    DUT_CENTIPOISES=None
    DUT_CUBIC_CENTIMETERS=None
    DUT_CUBIC_FEET=None
    DUT_CUBIC_FEET_PER_KIP=None
    DUT_CUBIC_FEET_PER_MINUTE=None
    DUT_CUBIC_FEET_PER_MINUTE_CUBIC_FOOT=None
    DUT_CUBIC_FEET_PER_MINUTE_SQUARE_FOOT=None
    DUT_CUBIC_FEET_PER_MINUTE_TON_OF_REFRIGERATION=None
    DUT_CUBIC_INCHES=None
    DUT_CUBIC_METERS=None
    DUT_CUBIC_METERS_PER_HOUR=None
    DUT_CUBIC_METERS_PER_KILONEWTON=None
    DUT_CUBIC_METERS_PER_SECOND=None
    DUT_CUBIC_MILLIMETERS=None
    DUT_CUBIC_YARDS=None
    DUT_CURRENCY=None
    DUT_CUSTOM=None
    DUT_CYCLES_PER_SECOND=None
    DUT_DECANEWTONS=None
    DUT_DECANEWTONS_PER_METER=None
    DUT_DECANEWTONS_PER_SQUARE_METER=None
    DUT_DECANEWTON_METERS=None
    DUT_DECANEWTON_METERS_PER_METER=None
    DUT_DECIMAL_DEGREES=None
    DUT_DECIMAL_FEET=None
    DUT_DECIMAL_INCHES=None
    DUT_DECIMETERS=None
    DUT_DEGREES_AND_MINUTES=None
    DUT_FAHRENHEIT=None
    DUT_FAHRENHEIT_DIFFERENCE=None
    DUT_FEET_FRACTIONAL_INCHES=None
    DUT_FEET_OF_WATER=None
    DUT_FEET_OF_WATER_PER_100FT=None
    DUT_FEET_PER_KIP=None
    DUT_FEET_PER_MINUTE=None
    DUT_FEET_PER_SECOND=None
    DUT_FEET_PER_SECOND_SQUARED=None
    DUT_FEET_TO_THE_FOURTH_POWER=None
    DUT_FEET_TO_THE_SIXTH_POWER=None
    DUT_FIXED=None
    DUT_FOOTCANDLES=None
    DUT_FOOTLAMBERTS=None
    DUT_FRACTIONAL_INCHES=None
    DUT_GALLONS_US=None
    DUT_GALLONS_US_PER_HOUR=None
    DUT_GALLONS_US_PER_MINUTE=None
    DUT_GENERAL=None
    DUT_GRADS=None
    DUT_GRAINS_PER_HOUR_SQUARE_FOOT_INCH_MERCURY=None
    DUT_HECTARES=None
    DUT_HERTZ=None
    DUT_HORSEPOWER=None
    DUT_HOURS=None
    DUT_HOUR_SQUARE_FOOT_FAHRENHEIT_PER_BRITISH_THERMAL_UNIT=None
    DUT_INCHES_OF_MERCURY=None
    DUT_INCHES_OF_WATER=None
    DUT_INCHES_OF_WATER_PER_100FT=None
    DUT_INCHES_PER_SECOND_SQUARED=None
    DUT_INCHES_TO_THE_FOURTH_POWER=None
    DUT_INCHES_TO_THE_SIXTH_POWER=None
    DUT_INV_CELSIUS=None
    DUT_INV_FAHRENHEIT=None
    DUT_INV_KILONEWTONS=None
    DUT_INV_KIPS=None
    DUT_JOULES=None
    DUT_JOULES_PER_GRAM=None
    DUT_JOULES_PER_GRAM_CELSIUS=None
    DUT_JOULES_PER_KELVIN=None
    DUT_JOULES_PER_KILOGRAM_CELSIUS=None
    DUT_KELVIN=None
    DUT_KELVIN_DIFFERENCE=None
    DUT_KILOAMPERES=None
    DUT_KILOCALORIES=None
    DUT_KILOCALORIES_PER_SECOND=None
    DUT_KILOGRAMS_FORCE=None
    DUT_KILOGRAMS_FORCE_PER_METER=None
    DUT_KILOGRAMS_FORCE_PER_SQUARE_METER=None
    DUT_KILOGRAMS_MASS=None
    DUT_KILOGRAMS_MASS_PER_METER=None
    DUT_KILOGRAMS_MASS_PER_SQUARE_METER=None
    DUT_KILOGRAMS_PER_CUBIC_METER=None
    DUT_KILOGRAM_FORCE_METERS=None
    DUT_KILOGRAM_FORCE_METERS_PER_METER=None
    DUT_KILOJOULES=None
    DUT_KILOJOULES_PER_KELVIN=None
    DUT_KILOMETERS_PER_HOUR=None
    DUT_KILOMETERS_PER_SECOND_SQUARED=None
    DUT_KILONEWTONS=None
    DUT_KILONEWTONS_PER_CUBIC_METER=None
    DUT_KILONEWTONS_PER_METER=None
    DUT_KILONEWTONS_PER_SQUARE_CENTIMETER=None
    DUT_KILONEWTONS_PER_SQUARE_METER=None
    DUT_KILONEWTONS_PER_SQUARE_MILLIMETER=None
    DUT_KILONEWTON_METERS=None
    DUT_KILONEWTON_METERS_PER_DEGREE=None
    DUT_KILONEWTON_METERS_PER_DEGREE_PER_METER=None
    DUT_KILONEWTON_METERS_PER_METER=None
    DUT_KILOPASCALS=None
    DUT_KILOVOLTS=None
    DUT_KILOVOLT_AMPERES=None
    DUT_KILOWATTS=None
    DUT_KILOWATT_HOURS=None
    DUT_KIPS=None
    DUT_KIPS_PER_CUBIC_FOOT=None
    DUT_KIPS_PER_CUBIC_INCH=None
    DUT_KIPS_PER_FOOT=None
    DUT_KIPS_PER_INCH=None
    DUT_KIPS_PER_SQUARE_FOOT=None
    DUT_KIPS_PER_SQUARE_INCH=None
    DUT_KIP_FEET=None
    DUT_KIP_FEET_PER_DEGREE=None
    DUT_KIP_FEET_PER_DEGREE_PER_FOOT=None
    DUT_KIP_FEET_PER_FOOT=None
    DUT_LITERS=None
    DUT_LITERS_PER_MINUTE=None
    DUT_LITERS_PER_SECOND=None
    DUT_LITERS_PER_SECOND_CUBIC_METER=None
    DUT_LITERS_PER_SECOND_KILOWATTS=None
    DUT_LITERS_PER_SECOND_SQUARE_METER=None
    DUT_LUMENS=None
    DUT_LUMENS_PER_WATT=None
    DUT_LUX=None
    DUT_MEGANEWTONS=None
    DUT_MEGANEWTONS_PER_METER=None
    DUT_MEGANEWTONS_PER_SQUARE_METER=None
    DUT_MEGANEWTON_METERS=None
    DUT_MEGANEWTON_METERS_PER_METER=None
    DUT_MEGAPASCALS=None
    DUT_METERS=None
    DUT_METERS_CENTIMETERS=None
    DUT_METERS_PER_KILONEWTON=None
    DUT_METERS_PER_SECOND=None
    DUT_METERS_PER_SECOND_SQUARED=None
    DUT_METERS_TO_THE_FOURTH_POWER=None
    DUT_METERS_TO_THE_SIXTH_POWER=None
    DUT_MICROINCHES_PER_INCH_FAHRENHEIT=None
    DUT_MICROMETERS_PER_METER_CELSIUS=None
    DUT_MILES_PER_HOUR=None
    DUT_MILES_PER_SECOND_SQUARED=None
    DUT_MILISECONDS=None
    DUT_MILLIAMPERES=None
    DUT_MILLIMETERS=None
    DUT_MILLIMETERS_OF_MERCURY=None
    DUT_MILLIMETERS_TO_THE_FOURTH_POWER=None
    DUT_MILLIMETERS_TO_THE_SIXTH_POWER=None
    DUT_MILLIVOLTS=None
    DUT_MINUTES=None
    DUT_NANOGRAMS_PER_PASCAL_SECOND_SQUARE_METER=None
    DUT_NEWTONS=None
    DUT_NEWTONS_PER_METER=None
    DUT_NEWTONS_PER_SQUARE_METER=None
    DUT_NEWTONS_PER_SQUARE_MILLIMETER=None
    DUT_NEWTON_METERS=None
    DUT_NEWTON_METERS_PER_METER=None
    DUT_OHM_METERS=None
    DUT_PASCALS=None
    DUT_PASCALS_PER_METER=None
    DUT_PASCAL_SECONDS=None
    DUT_PERCENTAGE=None
    DUT_PER_MILLE=None
    DUT_POUNDS_FORCE=None
    DUT_POUNDS_FORCE_PER_CUBIC_FOOT=None
    DUT_POUNDS_FORCE_PER_FOOT=None
    DUT_POUNDS_FORCE_PER_SQUARE_FOOT=None
    DUT_POUNDS_FORCE_PER_SQUARE_INCH=None
    DUT_POUNDS_MASS=None
    DUT_POUNDS_MASS_PER_CUBIC_FOOT=None
    DUT_POUNDS_MASS_PER_CUBIC_INCH=None
    DUT_POUNDS_MASS_PER_FOOT=None
    DUT_POUNDS_MASS_PER_FOOT_HOUR=None
    DUT_POUNDS_MASS_PER_FOOT_SECOND=None
    DUT_POUNDS_MASS_PER_SQUARE_FOOT=None
    DUT_POUND_FORCE_FEET=None
    DUT_POUND_FORCE_FEET_PER_FOOT=None
    DUT_RADIANS=None
    DUT_RADIANS_PER_SECOND=None
    DUT_RANKINE=None
    DUT_RANKINE_DIFFERENCE=None
    DUT_RATIO_10=None
    DUT_RATIO_12=None
    DUT_RISE_OVER_10_FEET=None
    DUT_RISE_OVER_120_INCHES=None
    DUT_RISE_OVER_FOOT=None
    DUT_RISE_OVER_INCHES=None
    DUT_RISE_OVER_MMS=None
    DUT_SECONDS=None
    DUT_SLOPE_DEGREES=None
    DUT_SQUARE_CENTIMETERS=None
    DUT_SQUARE_CENTIMETERS_PER_METER=None
    DUT_SQUARE_FEET=None
    DUT_SQUARE_FEET_PER_FOOT=None
    DUT_SQUARE_FEET_PER_KIP=None
    DUT_SQUARE_FEET_PER_THOUSAND_BRITISH_THERMAL_UNITS_PER_HOUR=None
    DUT_SQUARE_FEET_PER_TON_OF_REFRIGERATION=None
    DUT_SQUARE_INCHES=None
    DUT_SQUARE_INCHES_PER_FOOT=None
    DUT_SQUARE_METERS=None
    DUT_SQUARE_METERS_PER_KILONEWTON=None
    DUT_SQUARE_METERS_PER_KILOWATTS=None
    DUT_SQUARE_METERS_PER_METER=None
    DUT_SQUARE_METER_KELVIN_PER_WATT=None
    DUT_SQUARE_MILLIMETERS=None
    DUT_SQUARE_MILLIMETERS_PER_METER=None
    DUT_THERMS=None
    DUT_TONNES_FORCE=None
    DUT_TONNES_FORCE_PER_METER=None
    DUT_TONNES_FORCE_PER_SQUARE_METER=None
    DUT_TONNES_MASS=None
    DUT_TONNE_FORCE_METERS=None
    DUT_TONNE_FORCE_METERS_PER_METER=None
    DUT_TON_OF_REFRIGERATION=None
    DUT_UNDEFINED=None
    DUT_USTONNES_FORCE=None
    DUT_USTONNES_MASS=None
    DUT_VOLTS=None
    DUT_VOLT_AMPERES=None
    DUT_WATTS=None
    DUT_WATTS_PER_CUBIC_FOOT=None
    DUT_WATTS_PER_CUBIC_METER=None
    DUT_WATTS_PER_METER_KELVIN=None
    DUT_WATTS_PER_SQUARE_FOOT=None
    DUT_WATTS_PER_SQUARE_METER=None
    DUT_WATTS_PER_SQUARE_METER_KELVIN=None
    value__=None
class DistanceMeasuredFrom(Enum):
    Base=None
    Top=None
    value__=None
class DistributionOfNormals(Enum):
    AtEachPoint=None
    OnEachFacet=None
    OnePerFace=None
    value__=None
class DividedPath(Element):
    @staticmethod
    def AreCurveReferencesConnected(document,curveReferences):
        pass
    @staticmethod
    def Create(document,curveReferences,intersectors=None):
        pass
    def Dispose(self):
        pass
    def Flip(self):
        pass
    def GetIntersectingElements(self):
        pass
    @staticmethod
    def IsCurveReferenceValid(document,curveReference):
        pass
    @staticmethod
    def IsIntersectorValidForCreation(document,intersector):
        pass
    def IsIntersectorValidForDividedPath(self,intersector):
        pass
    def IsValidBeginningIndent(self,beginningIndent):
        pass
    def IsValidEndIndent(self,endIndent):
        pass
    @staticmethod
    def IsValidFixedNumberOfPoints(fixedNumberOfPoints):
        pass
    def IsValidMeasurementType(self,measurementType):
        pass
    def IsValidSpacingRuleJustification(self,justification):
        pass
    def IsValidSpacingRuleLayout(self,layout):
        pass
    @staticmethod
    def SeparateReferencesIntoConnectedReferences(document,curveReferences):
        pass
    def SetIntersectingElements(self,intersectors):
        pass
    BeginningIndent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayNodeNumbers=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayNodes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayReferenceCurves=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Distance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EndIndent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FixedNumberOfPoints=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Flipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsClosedLoop=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCyclical=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaximumDistance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MeasurementType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinimumDistance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfPoints=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpacingRuleJustification=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpacingRuleLayout=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TotalPathLength=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DividedPathMeasurementType(Enum):
    ChordLength=None
    SegmentLength=None
    value__=None
class DividedSurface(Element):
    def AddIntersectionElement(self,newIntersectionElemId):
        pass
    @staticmethod
    def CanBeDivided(document,reference):
        pass
    def CanBeIntersectionElement(self,id):
        pass
    @staticmethod
    def Create(document,faceReference):
        pass
    def Dispose(self):
        pass
    def GetAllIntersectionElements(self):
        pass
    @staticmethod
    def GetDividedSurfaceForReference(document,faceReference):
        pass
    def GetGridNodeLocation(self,gridNode):
        pass
    def GetGridNodeReference(self,gridNode):
        pass
    def GetGridNodeUV(self,gridNode):
        pass
    def GetGridSegmentReference(self,gridNode,gridSegmentDirection):
        pass
    @staticmethod
    def GetReferencesWithDividedSurfaces(host):
        pass
    def GetTileFamilyInstance(self,gridNode,tileIndex):
        pass
    def GetTileReference(self,gridNode,tileIndex):
        pass
    def IsSeedNode(self,gridNode):
        pass
    def RemoveAllIntersectionElements(self):
        pass
    def RemoveIntersectionElement(self,referenceElemIdToRemove):
        pass
    AllGridRotation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderTile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ComponentRotation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Host=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HostReference=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsComponentFlipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsComponentMirrored=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfUGridlines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfVGridlines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UPatternIndent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    USpacingRule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VPatternIndent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VSpacingRule=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Document(object):
    def AutoJoinElements(self):
        pass
    def CanEnableWorksharing(self):
        pass
    def Close(self,saveModified=None):
        pass
    def CombineElements(self,members):
        pass
    def ConvertDetailToModelCurves(self,view,detailCurves):
        pass
    def ConvertModelToDetailCurves(self,view,modelCurves):
        pass
    def ConvertModelToSymbolicCurves(self,view,modelCurves):
        pass
    def ConvertSymbolicToModelCurves(self,view,symbolicCurve):
        pass
    def Delete(self,*__args):
        pass
    def Dispose(self):
        pass
    def EditFamily(self,loadedFamily):
        pass
    def EnableWorksharing(self,worksetNameGridLevel,worksetName):
        pass
    def Equals(self,obj):
        pass
    def Export(self,folder,name,*__args):
        pass
    def ExportImage(self,options):
        pass
    def GetDefaultElementTypeId(self,defaultTypeId):
        pass
    def GetDefaultFamilyTypeId(self,familyCategoryId):
        pass
    def GetDocumentPreviewSettings(self):
        pass
    @staticmethod
    def GetDocumentVersion(doc):
        pass
    def GetElement(self,*__args):
        pass
    def GetHashCode(self):
        pass
    def GetPaintedMaterial(self,elementId,face):
        pass
    def GetPrintSettingIds(self):
        pass
    def GetRoomAtPoint(self,point,phase=None):
        pass
    def GetSpaceAtPoint(self,point,phase=None):
        pass
    def GetUnits(self):
        pass
    def GetWorksetId(self,id):
        pass
    def GetWorksetTable(self):
        pass
    def GetWorksharingCentralModelPath(self):
        pass
    def HasAllChangesFromCentral(self):
        pass
    def Import(self,file,options,*__args):
        pass
    def IsDefaultElementTypeIdValid(self,defaultTypeId,typeId):
        pass
    def IsDefaultFamilyTypeIdValid(self,familyCategoryId,familyTypeId):
        pass
    def IsPainted(self,elementId,face):
        pass
    def Link(self,file,options,pDBView=None,elementId=None):
        pass
    def LoadFamily(self,*__args):
        pass
    def LoadFamilySymbol(self,filename,name,*__args):
        pass
    def MakeTransientElements(self,maker):
        pass
    def Paint(self,elementId,face,*__args):
        pass
    def PostFailure(self,failure):
        pass
    def Print(self,views,*__args):
        pass
    def Regenerate(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def ReleaseUnmanagedResources_(self,*args):
        pass
    def ReloadLatest(self,reloadOptions):
        pass
    def RemovePaint(self,elementId,face):
        pass
    def Save(self,options=None):
        pass
    def SaveAs(self,*__args):
        pass
    def SaveToProjectAsImage(self,options):
        pass
    def SeparateElements(self,members):
        pass
    def SetDefaultElementTypeId(self,defaultTypeId,typeId):
        pass
    def SetDefaultFamilyTypeId(self,familyCategoryId,familyTypeId):
        pass
    def SetUnits(self,units):
        pass
    def SynchronizeWithCentral(self,transactOptions,syncOptions):
        pass
    def UnpostFailure(self,messageKey):
        pass
    def __enter__(self,*args):
        pass
    def __eq__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __ne__(self,*args):
        pass
    ActiveProjectLocation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ActiveView=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Application=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Create=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayUnitSystem=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyCreate=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsDetached=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsFamilyDocument=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsLinked=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsModifiable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsModified=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsReadOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsReadOnlyFile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsWorkshared=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MassDisplayTemporaryOverride=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MullionTypes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OwnerFamily=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PanelTypes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterBindings=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Phases=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrintManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectInformation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectLocations=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReactionsAreUpToDate=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Settings=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SiteLocation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Title=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WorksharingCentralGUID=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DocumentClosing=None
    DocumentPrinted=None
    DocumentPrinting=None
    DocumentSaved=None
    DocumentSavedAs=None
    DocumentSaving=None
    DocumentSavingAs=None
    ViewPrinted=None
    ViewPrinting=None
class DocumentPreviewSettings(object):
    def Dispose(self):
        pass
    def ForceViewUpdate(self,forceViewUpdate):
        pass
    def IsViewIdValidForPreview(self,viewId):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsViewUpdateForced=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreviewViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DocumentSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DocumentSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DocumentType(Enum):
    BuildingComponent=None
    Family=None
    IFC=None
    Other=None
    Project=None
    Template=None
    value__=None
class DocumentValidation(object):
    @staticmethod
    def CanDeleteElement(document,elementId):
        pass
    __all__=[
        'CanDeleteElement',
    ]
class DocumentVersion(object):
    def Dispose(self):
        pass
    def IsEqual(self,other):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfSaves=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VersionGUID=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Domain(Enum):
    DomainCableTrayConduit=None
    DomainElectrical=None
    DomainHvac=None
    DomainPiping=None
    DomainUndefined=None
    value__=None
class DoubleArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DoubleArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ParameterValue(object):
    def Copy(self):
        pass
    def Dispose(self):
        pass
    def IsEqual(self,other):
        pass
    def IsSameType(self,other):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DoubleParameterValue(ParameterValue):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,value=None):
        pass
    Value=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DuplicateTypeAction(Enum):
    Abort=None
    UseDestinationTypes=None
    value__=None
class DuplicateTypeNamesHandlerArgs(object):
    def Dispose(self):
        pass
    def GetTypeIds(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Document=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DWFExportOptions(CADExportOptions):
    CropBoxVisible=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportingAreas=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportObjectData=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportTexture=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ImageFormat=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ImageQuality=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MergedViews=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PaperFormat=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PortraitLayout=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StopOnError=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DWFImageFormat(Enum):
    Lossless=None
    Lossy=None
    value__=None
class DWFImageQuality(Enum):
    Default=None
    High=None
    Low=None
    Medium=None
    value__=None
class DWFImportOptions(object):
    def Dispose(self):
        pass
    def GetSheetViews(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetSheetViews(self,sheetViews):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DWFXExportOptions(DWFExportOptions):
class DWGExportOptions(ACADExportOptions):
    def Dispose(self):
        pass
    @staticmethod
    def GetPredefinedOptions(document,setup):
        pass
    @staticmethod # known case of __new__
    def __new__(self,option=None):
        pass
    MergedViews=property(lambda self:object(),lambda self,v:None,lambda self:None)
class DWGImportOptions(BaseImportOptions):
    def Dispose(self):
        pass
    def GetLineWeights(self):
        pass
    def SetLineWeights(self,lineWeight):
        pass
    @staticmethod # known case of __new__
    def __new__(self,option=None):
        pass
class DXFExportOptions(ACADExportOptions):
    def Dispose(self):
        pass
    @staticmethod
    def GetPredefinedOptions(document,setup):
        pass
    @staticmethod # known case of __new__
    def __new__(self,option=None):
        pass
class EaveCutterType(Enum):
    PlumbCut=None
    TwoCutPlumb=None
    TwoCutSquare=None
    value__=None
class Edge(GeometryObject):
    def AsCurve(self):
        pass
    def AsCurveFollowingFace(self,faceForDir):
        pass
    def ComputeDerivatives(self,parameter):
        pass
    def Dispose(self):
        pass
    def Evaluate(self,param):
        pass
    def EvaluateOnFace(self,param,face):
        pass
    def GetEndPointReference(self,index):
        pass
    def GetFace(self,index):
        pass
    def Tessellate(self):
        pass
    def TessellateOnFace(self,face):
        pass
    ApproximateLength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Reference=property(lambda self:object(),lambda self,v:None,lambda self:None)
class EdgeArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class EdgeArrayArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class EdgeArrayArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class EdgeArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class EditScope(object):
    def Cancel(self):
        pass
    def Commit(self,failurePreprocessor):
        pass
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsActive=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementBinding(Binding):
    def Dispose(self):
        pass
    Categories=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementCategoryFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    CategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementClassFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    def GetElementClass(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,type,inverted=None):
        pass
class ElementDesignOptionFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,designOptionId,inverted=None):
        pass
    DesignOptionId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementId(object):
    def Compare(self,id):
        pass
    def Equals(self,obj):
        pass
    def GetHashCode(self):
        pass
    def ToString(self):
        pass
    def __cmp__(self,*args):
        pass
    def __eq__(self,*args):
        pass
    def __ge__(self,*args):
        pass
    def __gt__(self,*args):
        pass
    def __le__(self,*args):
        pass
    def __lt__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    def __ne__(self,*args):
        pass
    IntegerValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InvalidElementId=None
class ElementIdParameterValue(ParameterValue):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,value=None):
        pass
    Value=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementIntersectsFilter(ElementSlowFilter):
    def Dispose(self):
        pass
    @staticmethod
    def IsCategorySupported(element):
        pass
    @staticmethod
    def IsElementSupported(element):
        pass
class ElementIntersectsElementFilter(ElementIntersectsFilter):
    def Dispose(self):
        pass
    def GetElement(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,element,inverted=None):
        pass
class ElementIntersectsSolidFilter(ElementIntersectsFilter):
    def Dispose(self):
        pass
    def GetSolid(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,solid,inverted=None):
        pass
class ElementIsCurveDrivenFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,inverted=None):
        pass
class ElementIsElementTypeFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,inverted=None):
        pass
class ElementLevelFilter(ElementSlowFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,levelId,inverted=None):
        pass
    LevelId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementLogicalFilter(ElementFilter):
    def Dispose(self):
        pass
class ElementMulticategoryFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    def GetCategoryIds(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
class ElementMulticlassFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,typeList,inverted=None):
        pass
class ElementOnPhaseStatus(Enum):
    Demolished=None
    Existing=None
    Future=None
    New=None
    None_JEDIFIX=None
    Past=None
    Temporary=None
    value__=None
class ElementOwnerViewFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,viewId,inverted=None):
        pass
    ViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementParameterFilter(ElementSlowFilter):
    def Dispose(self):
        pass
    def GetRules(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
class ElementPhaseStatusFilter(ElementSlowFilter):
    def Dispose(self):
        pass
    def GetPhaseStatuses(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,phaseId,*__args):
        pass
    PhaseId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementRecord(object):
    def Dispose(self):
        pass
    def GetBoundingBox(self):
        pass
    def GetCategoryId(self):
        pass
    def GetDesignOptionId(self):
        pass
    def GetId(self):
        pass
    def GetOwnerViewId(self):
        pass
    def HasBoundingBox(self):
        pass
    def IsAnElementType(self):
        pass
    def IsCurveDriven(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WorksetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementReferenceType(Enum):
    REFERENCE_TYPE_CUT_EDGE=None
    REFERENCE_TYPE_FOREIGN=None
    REFERENCE_TYPE_INSTANCE=None
    REFERENCE_TYPE_LINEAR=None
    REFERENCE_TYPE_MESH=None
    REFERENCE_TYPE_NONE=None
    REFERENCE_TYPE_SURFACE=None
    value__=None
class ElementSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementStructuralTypeFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,structuralType,inverted=None):
        pass
    StructuralType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElementTransformUtils(object):
    @staticmethod
    def CanMirrorElement(ADoc,elemId):
        pass
    @staticmethod
    def CanMirrorElements(ADoc,elemIds):
        pass
    @staticmethod
    def CopyElement(document,elementToCopy,translation):
        pass
    @staticmethod
    def CopyElements(*__args):
        pass
    @staticmethod
    def GetTransformFromViewToView(sourceView,destinationView):
        pass
    @staticmethod
    def MirrorElement(document,elementToMirror,plane):
        pass
    @staticmethod
    def MirrorElements(document,elementsToMirror,plane,mirrorCopies):
        pass
    @staticmethod
    def MoveElement(document,elementToMove,translation):
        pass
    @staticmethod
    def MoveElements(document,elementsToMove,translation):
        pass
    @staticmethod
    def RotateElement(document,elementToRotate,axis,angle):
        pass
    @staticmethod
    def RotateElements(document,elementsToRotate,axis,angle):
        pass
    __all__=[
        'CanMirrorElement',
        'CanMirrorElements',
        'CopyElement',
        'CopyElements',
        'GetTransformFromViewToView',
        'MirrorElement',
        'MirrorElements',
        'MoveElement',
        'MoveElements',
        'RotateElement',
        'RotateElements',
    ]
class ElementTypeGroup(Enum):
    AnalyticalLinkType=None
    AngularDimensionType=None
    ArcLengthDimensionType=None
    AreaLoadType=None
    AreaReinforcementType=None
    AttachedDetailGroupType=None
    BeamSystemType=None
    BuildingPadType=None
    CableTrayType=None
    CalloutType=None
    CeilingType=None
    ColorFillType=None
    ConduitType=None
    ContourLabelingType=None
    CorniceType=None
    CurtainSystemType=None
    DecalType=None
    DetailGroupType=None
    DiameterDimensionType=None
    DuctInsulationType=None
    DuctLiningType=None
    DuctType=None
    EdgeSlabType=None
    EndTreatmentType=None
    FabricAreaType=None
    FabricSheetType=None
    FasciaType=None
    FilledRegionType=None
    FlexDuctType=None
    FlexPipeType=None
    FloorType=None
    FootingSlabType=None
    GridType=None
    GutterType=None
    LevelType=None
    LinearDimensionType=None
    LineLoadType=None
    ModelGroupType=None
    ModelTextType=None
    MultiReferenceAnnotationType=None
    PathReinforcementType=None
    PipeInsulationType=None
    PipeType=None
    PointLoadType=None
    RadialDimensionType=None
    RailingsTypeForRamps=None
    RailingsTypeForStairs=None
    RampType=None
    RebarBarType=None
    RebarContainerType=None
    ReferenceViewerType=None
    RepeatingDetailType=None
    RevealType=None
    RoofSoffitType=None
    RoofType=None
    SpotCoordinateType=None
    SpotElevationType=None
    SpotSlopeType=None
    StairsBySketchType=None
    StairsRailingType=None
    StairsType=None
    StructuralConnectionHandlerType=None
    TagNoteType=None
    TextNoteType=None
    value__=None
    ViewportType=None
    ViewType3D=None
    ViewTypeCeilingPlan=None
    ViewTypeCostReport=None
    ViewTypeDetailView=None
    ViewTypeDrafting=None
    ViewTypeElevation=None
    ViewTypeFloorPlan=None
    ViewTypeGraphScheduleColumn=None
    ViewTypeLegend=None
    ViewTypeLoadsReport=None
    ViewTypePanelSchedule=None
    ViewTypePressureLossReport=None
    ViewTypeRendering=None
    ViewTypeSchedule=None
    ViewTypeSection=None
    ViewTypeSheet=None
    ViewTypeStructuralElevation=None
    ViewTypeStructuralPlan=None
    ViewTypeWalkthrough=None
    WallFoundationType=None
    WallType=None
    WireType=None
class ElementWorksetFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,worksetId,inverted=None):
        pass
    WorksetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ElevationMarker(Element):
    def CreateElevation(self,document,viewPlanId,index):
        pass
    @staticmethod
    def CreateElevationMarker(document,viewFamilyTypeId,origin,initialViewScale):
        pass
    def CreateReferenceElevation(self,document,index,viewIdToReference):
        pass
    @staticmethod
    def CreateReferenceElevationMarker(document,viewFamilyTypeId,origin,viewPlanId):
        pass
    def Dispose(self):
        pass
    def GetViewId(self,index):
        pass
    def HasElevations(self):
        pass
    def IsAvailableIndex(self,index):
        pass
    CurrentViewCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsReference=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaximumViewCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Ellipse(Curve):
    @staticmethod
    def Create(center,xRadius,yRadius,xAxis,yAxis,startParameter,endParameter):
        pass
    @staticmethod
    def CreateCurve(center,xRadius,yRadius,xAxis,yAxis,startParameter,endParameter):
        pass
    def Dispose(self):
        pass
    Center=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Normal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RadiusX=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RadiusY=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
class EndCapCondition(Enum):
    Exterior=None
    Interior=None
    NoEndCap=None
    None_JEDIFIX=None
    value__=None
class ExclusionFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    def GetIdsToExclude(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,idsToExclude):
        pass
class ExportColorMode(Enum):
    IndexColors=None
    TrueColor=None
    TrueColorPerView=None
    value__=None
class ExportColumnHeaders(Enum):
    MultipleRows=None
    None_JEDIFIX=None
    OneRow=None
    value__=None
class ExportDGNSettings(Element):
    @staticmethod
    def Create(document,name,options=None):
        pass
    def Dispose(self):
        pass
    def GetDGNExportOptions(self):
        pass
    @staticmethod
    def ListNames(aDoc):
        pass
    def SetDGNExportOptions(self,options):
        pass
class ExportDWGSettings(Element):
    @staticmethod
    def Create(document,name,options=None):
        pass
    def Dispose(self):
        pass
    def GetDWGExportOptions(self):
        pass
    def GetDXFExportOptions(self):
        pass
    @staticmethod
    def ListNames(aDoc):
        pass
    def SetDWGExportOptions(self,options):
        pass
    def SetDXFExportOptions(self,options):
        pass
class ExportEnergyModelType(Enum):
    BuildingElement=None
    SpatialElement=None
    value__=None
class ExportFontInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    DestinationFontName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportFontKey(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OriginalFontName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportFontTable(object):
    def Add(self,exportFontKey,exportFontInfo):
        pass
    def Clear(self):
        pass
    def ContainsKey(self,exportfontKey):
        pass
    def Dispose(self):
        pass
    def GetEnumerator(self):
        pass
    def GetExportFontInfo(self,exportFontKey):
        pass
    def GetFontTableIterator(self):
        pass
    def GetKeys(self):
        pass
    def GetValues(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Remove(self,exportFontKey):
        pass
    def __add__(self,*args):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    Count=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportFontTableIterator(object):
    def Dispose(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLayerInfo(object):
    def AddCutLayerModifier(self,layerModifier):
        pass
    def AddLayerModifier(self,layerModifier):
        pass
    def ClearCutLayerModifiers(self):
        pass
    def ClearLayerModifiers(self):
        pass
    def Dispose(self):
        pass
    def GetCutLayerModifiers(self):
        pass
    def GetLayerModifiers(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveCutLayerModifier(self,layerModifier):
        pass
    def RemoveLayerModifier(self,layerModifier):
        pass
    def SetCutLayerModifiers(self,cutLayermodifiers):
        pass
    def SetLayerModifiers(self,layermodifiers):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    CategoryType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ColorName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ColorNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutColorNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutLayerName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LayerName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLayerKey(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,categoryName=None,subCategoryName=None,num=None):
        pass
    CategoryName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpecialType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SubCategoryName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLayerTable(object):
    def Add(self,exportLayerKey,exportLayerInfo):
        pass
    def Clear(self):
        pass
    def ContainsKey(self,exportlayerKey):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetAvaliableLayerModifierTypes(document,exportLayerKey):
        pass
    def GetEnumerator(self):
        pass
    def GetExportLayerInfo(self,exportLayerKey):
        pass
    def GetKeys(self):
        pass
    def GetLayerTableIterator(self):
        pass
    def GetValues(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Remove(self,exportLayerKey):
        pass
    def __add__(self,*args):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    Count=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLayerTableIterator(object):
    def Dispose(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLinetypeInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    DestinationLinetypeName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLinetypeKey(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OriginalLinetypeName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLinetypeTable(object):
    def Add(self,exportLinetypeKey,exportLinetypeInfo):
        pass
    def Clear(self):
        pass
    def ContainsKey(self,exportLinetypeKey):
        pass
    def Dispose(self):
        pass
    def GetEnumerator(self):
        pass
    def GetExportLinetypeInfo(self,exportLinetypeKey):
        pass
    def GetKeys(self):
        pass
    def GetLinetypeTableIterator(self):
        pass
    def GetValues(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Remove(self,exportLinetypeKey):
        pass
    def __add__(self,*args):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    Count=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLinetypeTableIterator(object):
    def Dispose(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLineweightInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    DestinationLineweightName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLineweightKey(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OriginalLineweight=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLineweightTable(object):
    def Add(self,exportLineweightKey,exportLineweightInfo):
        pass
    def Clear(self):
        pass
    def ContainsKey(self,exportLineweightKey):
        pass
    def Dispose(self):
        pass
    def GetEnumerator(self):
        pass
    def GetExportLineweightInfo(self,exportLineweightKey):
        pass
    def GetKeys(self):
        pass
    def GetLineweightTableIterator(self):
        pass
    def GetValues(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Remove(self,exportLineweightKey):
        pass
    def __add__(self,*args):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    Count=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportLineweightTableIterator(object):
    def Dispose(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportPaperFormat(Enum):
    ANSI_A=None
    ANSI_B=None
    ANSI_C=None
    ANSI_D=None
    ANSI_E=None
    ARCH_A=None
    ARCH_B=None
    ARCH_C=None
    ARCH_D=None
    ARCH_E=None
    ARCH_E1=None
    ARCH_E2=None
    ARCH_E3=None
    Default=None
    ISO_A0=None
    ISO_A1=None
    ISO_A2=None
    ISO_A3=None
    ISO_A4=None
    ISO_B1=None
    ISO_B2=None
    ISO_B3=None
    ISO_B4=None
    value__=None
class ExportPatternInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    DestinationPatternName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportPatternKey(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OriginalFillPatternName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OriginalFillPatternType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportPatternTable(object):
    def Add(self,exportPatternKey,exportPatternInfo):
        pass
    def Clear(self):
        pass
    def ContainsKey(self,exportpatternKey):
        pass
    def Dispose(self):
        pass
    def GetEnumerator(self):
        pass
    def GetExportPatternInfo(self,exportPatternKey):
        pass
    def GetKeys(self):
        pass
    def GetPatternTableIterator(self):
        pass
    def GetValues(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Remove(self,exportPatternKey):
        pass
    def __add__(self,*args):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    Count=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportPatternTableIterator(object):
    def Dispose(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExportRange(Enum):
    CurrentView=None
    SetOfViews=None
    value__=None
    VisibleRegionOfCurrentView=None
class ExportSheetType(Enum):
    ST_Current=None
    ST_Select=None
    ST_Visible=None
    value__=None
class ExportTextQualifier(Enum):
    DoubleQuote=None
    None_JEDIFIX=None
    Quote=None
    value__=None
class ExportUnit(Enum):
    Centimeter=None
    Default=None
    Foot=None
    Inch=None
    Meter=None
    Millimeter=None
    value__=None
class ExportUtils(object):
    @staticmethod
    def GetExportId(document,elementId):
        pass
    @staticmethod
    def GetGBXMLDocumentId(document):
        pass
    @staticmethod
    def GetNurbsSurfaceDataForFace(face):
        pass
    __all__=[
        'GetExportId',
        'GetGBXMLDocumentId',
        'GetNurbsSurfaceDataForFace',
    ]
class ExternalDBApplicationResult(Enum):
    Failed=None
    Succeeded=None
    value__=None
class ExternalDefinition(Definition):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GUID=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OwnerGroup=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterGroup=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UserModifiable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visible=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalDefinitionCreationOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,name,type):
        pass
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GUID=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Type=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UserModifiable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visible=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalDefinitions(Definitions):
    def Dispose(self):
        pass
class ExternalFileReference(object):
    def Dispose(self):
        pass
    def GetAbsolutePath(self):
        pass
    def GetLinkedFileStatus(self):
        pass
    def GetPath(self):
        pass
    def GetReferencingId(self):
        pass
    @staticmethod
    def IsValidExternalFileReference(data):
        pass
    def IsValidPathTypeForExternalFileReference(self,pathType):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ExternalFileReferenceType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalFileReferenceType(Enum):
    AssemblyCodeTable=None
    CADLink=None
    Decal=None
    DWFMarkup=None
    KeynoteTable=None
    Material=None
    None_JEDIFIX=None
    RevitLink=None
    value__=None
class ExternalFileUtils(object):
    @staticmethod
    def GetAllExternalFileReferences(aDoc):
        pass
    @staticmethod
    def GetExternalFileReference(aDoc,elemId):
        pass
    @staticmethod
    def IsExternalFileReference(aDoc,elemId):
        pass
    __all__=[
        'GetAllExternalFileReferences',
        'GetExternalFileReference',
        'IsExternalFileReference',
    ]
class ExternalResourceBrowserData(object):
    def AddResource(self,resourceName,*__args):
        pass
    def AddSubFolder(self,folderName):
        pass
    def CallingDocumentHasModelPath(self):
        pass
    def Dispose(self):
        pass
    def GetCallingDocumentModelPath(self):
        pass
    def GetMatchOptions(self):
        pass
    def GetResources(self):
        pass
    def GetSubFolders(self):
        pass
    def IsValidFolderName(self,folderName):
        pass
    def IsValidResouceName(self,resourceName):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document,serverId,folderPath,matchOptions):
        pass
    FolderPath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServerId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalResourceLoadContent(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LoadStatus=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Version=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalResourceLoadContext(object):
    def CallingDocumentHasModelPath(self):
        pass
    def Dispose(self):
        pass
    def GetCallingDocumentModelPath(self):
        pass
    def GetCurrentlyLoadedReference(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LoadOperationType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalResourceLoadData(object):
    def Dispose(self):
        pass
    def GetExternalResourceReference(self):
        pass
    def GetLoadContent(self):
        pass
    def GetLoadContext(self):
        pass
    def GetLoadRequestId(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ErrorsReported=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExternalResourceType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LoadStatus=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalResourceLoadStatus(Enum):
    CannotFindServer=None
    Failure=None
    ResourceAlreadyCurrent=None
    ServerThrewException=None
    Success=None
    Uninitialized=None
    value__=None
class ExternalResourceMatchOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,resourceType):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ResourceType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalResourceReference(object):
    @staticmethod
    def CreateLocalResource(doc,resourceType,path,pathType):
        pass
    def Dispose(self):
        pass
    def GetReferenceInformation(self):
        pass
    def GetResourceShortDisplayName(self):
        pass
    def GetResourceVersionStatus(self):
        pass
    def HasValidDisplayPath(self):
        pass
    def IsValidReference(self,resourceType):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    InSessionPath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServerId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Version=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalResourceServerExtensions(object):
    def Dispose(self):
        pass
    def GetRevitLinkOperations(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalResourceServerUtils(object):
    @staticmethod
    def IsValidShortName(serverId,serverName):
        pass
    @staticmethod
    def ServerSupportsAssemblyCodeData(extRef):
        pass
    @staticmethod
    def ServerSupportsKeynotes(extRef):
        pass
    @staticmethod
    def ServerSupportsRevitLinks(extRef):
        pass
    __all__=[
        'IsValidShortName',
        'ServerSupportsAssemblyCodeData',
        'ServerSupportsKeynotes',
        'ServerSupportsRevitLinks',
    ]
class ExternalResourceServiceUtils(object):
    @staticmethod
    def GetServersByType(type):
        pass
    __all__=[
        'GetServersByType',
    ]
class GuidEnum(object):
    def Equals(self,obj):
        pass
    def GetHashCode(self):
        pass
    def __eq__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,guid):
        pass
    def __ne__(self,*args):
        pass
    Guid=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExternalResourceType(GuidEnum):
    @staticmethod # known case of __new__
    def __new__(self,guid):
        pass
class ExternalResourceTypes(object):
    BuiltInExternalResourceTypes=None
    __all__=[
        'BuiltInExternalResourceTypes',
    ]
class ExternalResourceUIBrowseResultType(Enum):
    FolderNotFound=None
    ResourceNotFound=None
    Success=None
    value__=None
class ExternalResourceUtils(object):
    @staticmethod
    def GetAllExternalResourceReferences(document,resourceType=None):
        pass
    __all__=[
        'GetAllExternalResourceReferences',
    ]
class Extrusion(GenericForm):
    def Dispose(self):
        pass
    EndOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Sketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExtrusionAnalyzer(object):
    def CalculateFaceAlignment(self):
        pass
    @staticmethod
    def Create(solidGeometry,plane,direction):
        pass
    def Dispose(self):
        pass
    def GetExtrusionBase(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EndParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExtrusionDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExtrusionAnalyzerFaceAlignment(Enum):
    FullyAligned=None
    PartiallyAligned=None
    Unaligned=None
    value__=None
class RoofBase(HostObject):
    def Dispose(self):
        pass
    EaveCuts=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FasciaDepth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RoofType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SlabShapeEditor=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ExtrusionRoof(RoofBase):
    def Dispose(self):
        pass
    def GetProfile(self):
        pass
    CurtainGrids=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationAncillaryUsage(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AncillaryDepth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AncillaryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AncillaryWidthOrDiameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Length=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductCode=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Quantity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Type=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UsageType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationConfiguration(Element):
    def CanBeSwapped(self):
        pass
    def Dispose(self):
        pass
    def GetAllDampers(self):
        pass
    def GetAllFabricationConnectorDefinitions(self,domain,shape):
        pass
    def GetAllInsulationSpecifications(self,pFabPart):
        pass
    def GetAllLoadedServices(self):
        pass
    def GetAllMaterials(self,part):
        pass
    def GetAllPartCustomData(self):
        pass
    def GetAllPartStatuses(self):
        pass
    def GetAllServices(self):
        pass
    def GetAllSpecifications(self,part):
        pass
    def GetAllUsedServices(self):
        pass
    def GetAncillaries(self,type,includeKits,filterKits):
        pass
    def GetAncillaryGroup(self,ancillaryId):
        pass
    def GetAncillaryGroupName(self,ancillaryId):
        pass
    def GetAncillaryName(self,ancillaryId):
        pass
    def GetDamperName(self,damperId):
        pass
    @staticmethod
    def GetFabricationConfiguration(doc):
        pass
    def GetFabricationConfigurationInfo(self):
        pass
    def GetFabricationConnectorDomain(self,fabricationConnectorId):
        pass
    def GetFabricationConnectorGroup(self,fabricationConnectorId):
        pass
    def GetFabricationConnectorName(self,fabricationConnectorId):
        pass
    def GetFabricationConnectorShape(self,fabricationConnectorId):
        pass
    def GetInsulationSpecificationAbbreviation(self,insulationSpecificationId):
        pass
    def GetInsulationSpecificationGroup(self,specId):
        pass
    def GetInsulationSpecificationName(self,specId):
        pass
    def GetMaterialAbbreviation(self,materialId):
        pass
    def GetMaterialGroup(self,materialId):
        pass
    def GetMaterialName(self,materialId):
        pass
    def GetMaterialThickness(self,materialId,gaugeId):
        pass
    def GetPartCustomDataName(self,statusId):
        pass
    def GetPartCustomDataType(self,statusId):
        pass
    def GetPartStatusDescription(self,statusId):
        pass
    def GetProfile(self):
        pass
    def GetService(self,serviceId):
        pass
    def GetSpecificationAbbreviation(self,specificationId):
        pass
    def GetSpecificationGroup(self,specId):
        pass
    def GetSpecificationName(self,specId):
        pass
    def HasValidConfiguration(self):
        pass
    def IsAncillaryKit(self,ancillaryId):
        pass
    def LoadServices(self,serviceIds):
        pass
    def LocateFabricationConnector(self,group,name,domain,shape):
        pass
    def LocateInsulationSpecification(self,group,name):
        pass
    def LocateMaterial(self,group,name):
        pass
    def LocateSpecification(self,group,name):
        pass
    def ReloadConfiguration(self):
        pass
    def SetConfiguration(self,fabricationConfigurationInfo,profile=None):
        pass
    def UnloadServices(self,serviceIds):
        pass
class FabricationConfigurationInfo(object):
    def Dispose(self):
        pass
    @staticmethod
    def FindSourceFabricationConfiguration(fabricationConfiguration):
        pass
    @staticmethod
    def GetAllFabricationConfigurations():
        pass
    def GetProfiles(self):
        pass
    def IsValid(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GUID=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsLocked=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Path=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UnitSystem=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Version=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationConnectorInfo(object):
    def Dispose(self):
        pass
    def HasDoubleWallConnector(self):
        pass
    def IsValid(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    BodyConnectorId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DoubleWallConnectorId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FabricationIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsBodyConnectorLocked=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsDoubleWallConnectorLocked=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationDimensionDefinition(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsModifiable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Type=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UnitType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationDimensionType(Enum):
    Angle=None
    Depth=None
    Diameter=None
    Internal=None
    Length=None
    value__=None
    Width=None
class FabricationDimensionUnitType(Enum):
    Angular=None
    Linear=None
    NoUnits=None
    value__=None
class FabricationHostedInfo(object):
    def DisconnectFromHost(self):
        pass
    def Dispose(self):
        pass
    def GetBearerCenterline(self):
        pass
    def PlaceOnHost(self,hostId,hostConnector,distance):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    HostId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationPart(Element):
    def AdjustEndLength(self,partConn,lengthToAdjust,totalLengthOnly):
        pass
    @staticmethod
    def AlignPartByConnectors(doc,partConn,toConn,axisRotation):
        pass
    def CanAdjustEndLength(self,partConn):
        pass
    def CanSplitStraight(self,document,partId,position):
        pass
    @staticmethod
    def ConnectAndCouple(doc,partConn,toConn):
        pass
    @staticmethod
    def Create(document,button,*__args):
        pass
    @staticmethod
    def CreateHanger(document,button,*__args):
        pass
    def Dispose(self):
        pass
    def GetCalculatedDimensionValue(self,dim):
        pass
    def GetDimensionCalculatedOptions(self,dim):
        pass
    def GetDimensions(self):
        pass
    def GetDimensionValue(self,dim):
        pass
    def GetHostedInfo(self):
        pass
    def GetPartAncillaryUsage(self):
        pass
    def GetPartCustomDataInteger(self,customId):
        pass
    def GetPartCustomDataReal(self,customId):
        pass
    def GetPartCustomDataText(self,customId):
        pass
    def GetProductListEntryCount(self):
        pass
    def GetProductListEntryName(self,index):
        pass
    def GetRodInfo(self):
        pass
    def GetTransform(self):
        pass
    def HasCustomData(self,customId):
        pass
    def IsAHanger(self):
        pass
    def IsAStraight(self):
        pass
    def IsATap(self):
        pass
    def IsDimensionCalculated(self,dim):
        pass
    def IsProductList(self):
        pass
    def IsProductListEntryCompatibleSize(self,productEntry):
        pass
    def IsStraightSegment(self,document,partId):
        pass
    @staticmethod
    def OptimizeLengths(doc,partIds):
        pass
    @staticmethod
    def PlaceAsTap(doc,tapPartConn,hostPartConn,distance,axisRotation,secondaryAxisRotation):
        pass
    @staticmethod
    def PlaceFittingAsCutIn(doc,straightId,fittingId,position,fittingConn,axisRotation):
        pass
    @staticmethod
    def Reposition(doc,partId):
        pass
    @staticmethod
    def RotateConnectedPartByConnector(doc,conn,axisRotationBy):
        pass
    @staticmethod
    def RotateConnectedTap(doc,tap,primaryAxisRotateBy,secondaryAxisRotateBy):
        pass
    def SetCalculatedDimensionValue(self,dim,value):
        pass
    def SetDimensionValue(self,dim,newValue):
        pass
    def SetPartCustomDataText(self,customId,value):
        pass
    def SetPositionByEnd(self,connector,position):
        pass
    def SplitStraight(self,document,partId,position):
        pass
    @staticmethod
    def StretchAndFit(document,stretchConnector,target,newPartIds):
        pass
    Alias=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BottomOfPartElevation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConnectorManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DomainType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DoubleWallMaterial=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DoubleWallMaterialArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DoubleWallMaterialThickness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HangerRodKit=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasDoubleWall=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasInsulation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasLining=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InsulationArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InsulationSpecification=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InsulationThickness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InsulationType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsBoughtOut=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ItemCustomId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ItemNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LevelOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LiningArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LiningThickness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LiningType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Material=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialThickness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Notes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OverallSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PartGuid=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PartStatus=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductCode=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductDataRange=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductFinishDescription=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductInstallType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductListEntry=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductLongDescription=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductMaterialDescription=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductOriginalEquipmentManufacture=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductShortDescription=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductSizeDescription=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProductSpecificationDescription=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServiceAbbreviation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServiceId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServiceName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SheetMetalArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Slope=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Specification=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopOfPartElevation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ValidationStatus=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Vendor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VendorCode=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Weight=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationPartType(ElementType):
    @staticmethod
    def Create(document,button,condition):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def Lookup(document,button,condition):
        pass
class FabricationRodInfo(object):
    def AttachToHanger(self,hangerId,rodIndex,position):
        pass
    def AttachToStructure(self):
        pass
    def Dispose(self):
        pass
    def GetBearerExtension(self,rodIndex):
        pass
    def GetRodAttachedElementId(self,rodIndex):
        pass
    def GetRodEndPosition(self,rodIndex):
        pass
    def IsRodLockedWithHost(self,rodIndex):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetBearerExtension(self,rodIndex,length):
        pass
    def SetRodEndPosition(self,rodIndex,position):
        pass
    def SetRodLockedWithHost(self,rodIndex,locked):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsAttachedToStructure=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RodCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationService(object):
    def Dispose(self):
        pass
    def GetButton(self,groupIndex,buttonIndex):
        pass
    def GetButtonCount(self,group):
        pass
    def GetGroupName(self,group):
        pass
    def IsGroupExcluded(self,groupIndex):
        pass
    def IsValidButtonIndex(self,groupIndex,buttonIndex):
        pass
    def IsValidGroupIndex(self,groupIndex):
        pass
    def OverrideServiceButtonExclusion(self,groupIndex,buttonIndex,exclude):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def ResetServiceExclusionOverrides(self):
        pass
    def SetServiceGroupExclusions(self,excludedGroups):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Abbreviation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FabricationSystemName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GroupCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServiceId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FabricationServiceButton(object):
    def ContainsFabricationPartType(self,partType):
        pass
    def Dispose(self):
        pass
    def GetConditionDescription(self,condition):
        pass
    def GetConditionImage(self,condition):
        pass
    def GetConditionLowerValue(self,condition):
        pass
    def GetConditionName(self,condition):
        pass
    def GetConditionUpperValue(self,condition):
        pass
    def GetImage(self):
        pass
    def IsExcluded(self):
        pass
    def IsUnrestrictedCondition(self,condition):
        pass
    def IsValid(self):
        pass
    @staticmethod
    def IsValidConditionIndex(button,condition):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ButtonIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Code=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConditionCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GroupIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsAHanger=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServiceId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FaceArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FaceArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FaceIntersectionFaceResult(Enum):
    Intersecting=None
    NonIntersecting=None
    value__=None
class FaceNode(RenderNode):
    def Dispose(self):
        pass
    def GetFace(self):
        pass
class FaceSecondDerivatives(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MixedDerivative=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UUDerivative=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VVDerivative=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FaceSplitter(Element):
    def Dispose(self):
        pass
    SplitElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FacetingUtils(object):
    @staticmethod
    def ConvertTrianglesToQuads(triangulation):
        pass
    __all__=[
        'ConvertTrianglesToQuads',
    ]
class FaceWall(HostObject):
    @staticmethod
    def Create(document,wallType,locationLine,faceReference):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def IsValidFaceReferenceForFaceWall(document,faceReference):
        pass
    @staticmethod
    def IsWallTypeValidForFaceWall(document,wallType):
        pass
class FailureDefinition(object):
    def AddResolutionType(self,type,caption,classOfResolution):
        pass
    @staticmethod
    def CreateFailureDefinition(id,severity,messageString):
        pass
    def Dispose(self):
        pass
    def GetApplicableResolutionTypes(self):
        pass
    def GetDefaultResolutionType(self):
        pass
    def GetDescriptionText(self):
        pass
    def GetResolutionCaption(self,type):
        pass
    def HasResolutions(self):
        pass
    def IsResolutionApplicable(self,type):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetDefaultResolutionType(self,type):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Severity=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureDefinitionAccessor(object):
    def Dispose(self):
        pass
    def GetApplicableResolutionTypes(self):
        pass
    def GetDefaultResolutionType(self):
        pass
    def GetDescriptionText(self):
        pass
    def GetId(self):
        pass
    def GetResolutionCaption(self,type):
        pass
    def GetSeverity(self):
        pass
    def HasResolutions(self):
        pass
    def IsResolutionApplicable(self,type):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetDefaultResolutionType(self,type):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureDefinitionId(GuidEnum):
    @staticmethod # known case of __new__
    def __new__(self,guid):
        pass
class FailureDefinitionRegistry(object):
    def Dispose(self):
        pass
    def FindFailureDefinition(self,id):
        pass
    def ListAllFailureDefinitions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureHandlingOptions(object):
    def Dispose(self):
        pass
    def GetClearAfterRollback(self):
        pass
    def GetDelayedMiniWarnings(self):
        pass
    def GetFailuresPreprocessor(self):
        pass
    def GetForcedModalHandling(self):
        pass
    def GetTransactionFinalizer(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetClearAfterRollback(self,bFlag):
        pass
    def SetDelayedMiniWarnings(self,bFlag):
        pass
    def SetFailuresPreprocessor(self,preprocessor):
        pass
    def SetForcedModalHandling(self,bFlag):
        pass
    def SetTransactionFinalizer(self,finalizer):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureMessage(object):
    def AddResolution(self,type,resolution):
        pass
    def Dispose(self):
        pass
    def GetAdditionalElements(self):
        pass
    def GetDefaultResolutionCaption(self):
        pass
    def GetDescriptionText(self):
        pass
    def GetFailingElements(self):
        pass
    def GetFailureDefinitionId(self):
        pass
    def GetSeverity(self):
        pass
    def HasResolutionOfType(self,type):
        pass
    def HasResolutions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetAdditionalElement(self,additionalElement):
        pass
    def SetAdditionalElements(self,additionalElements):
        pass
    def SetFailingElement(self,id):
        pass
    def SetFailingElements(self,idsToShow):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,id):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureMessageAccessor(object):
    def CloneFailureMessage(self):
        pass
    def Dispose(self):
        pass
    def GetAdditionalElementIds(self):
        pass
    def GetCurrentResolutionType(self):
        pass
    def GetDefaultResolutionCaption(self):
        pass
    def GetDescriptionText(self):
        pass
    def GetFailingElementIds(self):
        pass
    def GetFailureDefinitionId(self):
        pass
    def GetNumberOfResolutions(self):
        pass
    def GetSeverity(self):
        pass
    def HasResolutionOfType(self,type):
        pass
    def HasResolutions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetCurrentResolutionType(self,resolutionType):
        pass
    def ShouldMergeWithMessage(self,messageToMergeWith):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureMessageKey(object):
    def Dispose(self):
        pass
    def Equals(self,obj):
        pass
    def GetHashCode(self):
        pass
    def IsEqual(self,other):
        pass
    def IsValid(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __eq__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __ne__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureProcessingResult(Enum):
    Continue=None
    ProceedWithCommit=None
    ProceedWithRollBack=None
    value__=None
    WaitForUserInput=None
class FailureResolutionType(Enum):
    CreateElements=None
    Default=None
    DeleteElements=None
    DetachElements=None
    FixElements=None
    Invalid=None
    MoveElements=None
    Others=None
    QuitEditMode=None
    SaveDocument=None
    SetValue=None
    ShowElements=None
    SkipElements=None
    UnlockConstraints=None
    value__=None
class FailuresAccessor(object):
    def CanCommitPendingTransaction(self):
        pass
    def CanRollBackPendingTransaction(self):
        pass
    def CommitPendingTransaction(self):
        pass
    def DeleteAllWarnings(self):
        pass
    def DeleteElements(self,idsToDelete):
        pass
    def DeleteWarning(self,failure):
        pass
    def Dispose(self):
        pass
    def GetAttemptedResolutionTypes(self,failure):
        pass
    def GetDocument(self):
        pass
    def GetFailureHandlingOptions(self):
        pass
    def GetFailureMessages(self,severity=None):
        pass
    def GetSeverity(self):
        pass
    def GetTransactionName(self):
        pass
    def IsActive(self):
        pass
    def IsElementsDeletionPermitted(self,idsToDelete=None,reason=None):
        pass
    def IsFailureResolutionPermitted(self,failure=None,resolutionType=None):
        pass
    def IsPending(self):
        pass
    def IsTransactionBeingCommitted(self):
        pass
    def JournalFailures(self,failures):
        pass
    def PostFailure(self,failure):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def ReplaceFailures(self,failure):
        pass
    def ResolveFailure(self,failure):
        pass
    def ResolveFailures(self,failures):
        pass
    def RollBackPendingTransaction(self):
        pass
    def SetFailureHandlingOptions(self,options):
        pass
    def SetTransactionName(self,transactionName):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FailureSeverity(Enum):
    DocumentCorruption=None
    Error=None
    None_JEDIFIX=None
    value__=None
    Warning=None
class Family(Element):
    def CanHaveStructuralSection(self):
        pass
    def Dispose(self):
        pass
    def ExtractPartAtom(self,xmlFilePath):
        pass
    def GetFamilySymbolIds(self):
        pass
    def GetFamilyTypeParameterValues(self,parameterId):
        pass
    def HasLargeSketches(self):
        pass
    def IsAppropriateCategoryId(self,categoryId):
        pass
    CurtainPanelHorizontalSpacing=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CurtainPanelTilePattern=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CurtainPanelVerticalSpacing=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyCategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyCategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyPlacementType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsConceptualMassFamily=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCurtainPanelFamily=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsEditable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsInPlace=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsOwnerFamily=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsParametric=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsUserCreated=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowSpatialElementCalculationPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralCodeName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralFamilyNameKey=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralMaterialType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralSectionShape=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyElementVisibility(APIObject):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,visibilityType):
        pass
    IsShownInCoarse=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShownInFine=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShownInFrontBack=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShownInLeftRight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShownInMedium=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShownInPlanRCPCut=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShownInTopBottom=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShownOnlyWhenCut=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VisibilityType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyElementVisibilityType(Enum):
    Model=None
    value__=None
    ViewSpecific=None
class FamilyHostingBehavior(Enum):
    Ceiling=None
    Face=None
    Floor=None
    None_JEDIFIX=None
    Roof=None
    value__=None
    Wall=None
class FamilyInstanceFilter(ElementSlowFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document,familySymbolId):
        pass
    FamilySymbolId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyManager(APIObject):
    def AddParameter(self,*__args):
        pass
    def AssociateElementParameterToFamilyParameter(self,elementParameter,familyParameter):
        pass
    def CanElementParameterBeAssociated(self,elementParameter):
        pass
    def DeleteCurrentType(self):
        pass
    def Dispose(self):
        pass
    def GetAssociatedFamilyParameter(self,elementParameter):
        pass
    def GetParameters(self):
        pass
    def IsParameterLockable(self,familyParameter):
        pass
    def IsParameterLocked(self,familyParameter):
        pass
    def IsUserAssignableParameterGroup(self,parameterGroup):
        pass
    def MakeInstance(self,familyParameter):
        pass
    def MakeNonReporting(self,familyParameter):
        pass
    def MakeReporting(self,familyParameter):
        pass
    def MakeType(self,familyParameter):
        pass
    def NewType(self,typeName):
        pass
    def RemoveParameter(self,familyParameter):
        pass
    def RenameCurrentType(self,typeName):
        pass
    def RenameParameter(self,familyParameter,name):
        pass
    def ReorderParameters(self,parameters):
        pass
    def ReplaceParameter(self,currentParameter,*__args):
        pass
    def Set(self,familyParameter,value):
        pass
    def SetDescription(self,familyParameter,description):
        pass
    def SetFormula(self,familyParameter,formula):
        pass
    def SetParameterLocked(self,familyParameter,locked):
        pass
    def SetValueString(self,familyParameter,value):
        pass
    def SortParameters(self,order):
        pass
    CurrentType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Parameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Types=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyParameter(APIObject):
    def Dispose(self):
        pass
    AssociatedParameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanAssignFormula=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Definition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayUnitType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Formula=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GUID=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsDeterminedByFormula=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsInstance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsReadOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsReporting=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShared=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StorageType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UserModifiable=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyParameterSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyParameterSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyPlacementType(Enum):
    Adaptive=None
    CurveBased=None
    CurveBasedDetail=None
    CurveDrivenStructural=None
    Invalid=None
    OneLevelBased=None
    OneLevelBasedHosted=None
    TwoLevelsBased=None
    value__=None
    ViewBased=None
    WorkPlaneBased=None
class FamilyPointLocation(APIObject):
    def Dispose(self):
        pass
    def GetLocation(self):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyPointPlacementReference(APIObject):
    def Dispose(self):
        pass
    def getCDA(self,*args):
        pass
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PointReference=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilySizeTable(object):
    def AsValueString(self,row,column):
        pass
    def Dispose(self):
        pass
    def GetColumnHeader(self,index):
        pass
    def IsValidColumnIndex(self,index):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfColumns=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfRows=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilySizeTableColumn(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    DisplayUnitType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UnitType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilySizeTableErrorInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    FamilySizeTableErrorType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FilePath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InvalidColumnIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InvalidHeaderText=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InvalidRowIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilySizeTableErrorType(Enum):
    CannotOpenFile=None
    CannotParseColumnHeader=None
    CannotReadFile=None
    FileNotFound=None
    IncorrectNumberOfColumns=None
    InvalidHeaderSeparator=None
    Undefined=None
    value__=None
class FamilySizeTableManager(object):
    @staticmethod
    def CreateFamilySizeTableManager(document,familyId):
        pass
    def Dispose(self):
        pass
    def ExportSizeTable(self,tableName,filePath):
        pass
    def GetAllSizeTableNames(self):
        pass
    @staticmethod
    def GetFamilySizeTableManager(document,familyId):
        pass
    def GetSizeTable(self,tableName):
        pass
    def HasSizeTable(self,tableName):
        pass
    def ImportSizeTable(self,document,filePath,errorInfo):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveSizeTable(self,tableName):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfSizeTables=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilySource(Enum):
    Family=None
    Project=None
    value__=None
class FamilySymbolFilter(ElementQuickFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,familyId):
        pass
    FamilyId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilySymbolProfile(SweepProfile):
    def Dispose(self):
        pass
    Angle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsFlipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Profile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyThermalProperties(object):
    def Dispose(self):
        pass
    @staticmethod
    def Find(pADoc,constructionId):
        pass
    def IsValid(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AnalyticConstructionName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AnalyticConstructionTypeId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HeatTransferCoefficient=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SolarHeatGainCoefficient=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalResistance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VisualLightTransmittance=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyType(APIObject):
    def AsDouble(self,familyParameter):
        pass
    def AsElementId(self,familyParameter):
        pass
    def AsInteger(self,familyParameter):
        pass
    def AsString(self,familyParameter):
        pass
    def AsValueString(self,familyParameter):
        pass
    def Dispose(self):
        pass
    def HasValue(self,familyParameter):
        pass
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyTypeSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyTypeSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FamilyUtils(object):
    @staticmethod
    def ConvertFamilyToFaceHostBased(document,familyId):
        pass
    @staticmethod
    def FamilyCanConvertToFaceHostBased(document,familyId):
        pass
    @staticmethod
    def GetProfileSymbols(document,profileFamilyUsage,oneCurveLoopOnly):
        pass
    __all__=[
        'ConvertFamilyToFaceHostBased',
        'FamilyCanConvertToFaceHostBased',
        'GetProfileSymbols',
    ]
class FBXExportOptions(object):
    LevelsOfDetailValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StopOnError=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UseLevelsOfDetail=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WithoutBoundaryEdges=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ModelPath(object):
    def Compare(self,otherPath):
        pass
    def Dispose(self):
        pass
    def GetModelGUID(self):
        pass
    def GetProjectGUID(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __cmp__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    CentralServerPath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Empty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServerPath=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilePath(ModelPath):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,path):
        pass
class FilledRegion(Element):
    @staticmethod
    def Create(document,typeId,viewId,boundaries):
        pass
    def Dispose(self):
        pass
    def GetBoundaries(self):
        pass
    @staticmethod
    def GetValidLineStyleIdsForFilledRegion(document):
        pass
    @staticmethod
    def IsValidFilledRegionTypeId(document,typeId):
        pass
    @staticmethod
    def IsValidLineStyleIdForFilledRegion(document,lineStyleId):
        pass
    def SetLineStyleId(self,lineStyleId):
        pass
    IsMasking=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilledRegionBackground(Enum):
    Opaque=None
    Transparent=None
    value__=None
class LineAndTextAttrSymbol(ElementType):
    def Dispose(self):
        pass
class FilledRegionType(LineAndTextAttrSymbol):
    def Dispose(self):
        pass
    @staticmethod
    def IsValidLineWeight(lineWeight):
        pass
    Background=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Color=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FillPatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineWeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FillGrid(object):
    def CalculateLengthPerArea(self):
        pass
    def CalculateLinesPerLength(self):
        pass
    def CalculateStrokesPerArea(self):
        pass
    def Dispose(self):
        pass
    def GetHatchingDirection(self):
        pass
    def GetPointLineZone(self,point,nearestPoint=None):
        pass
    def GetSegmentDirection(self):
        pass
    def GetSegments(self):
        pass
    def IsEqual(self,other):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetSegments(self,segArr):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    Angle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Offset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Shift=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FillPattern(object):
    def Dispose(self):
        pass
    def ExpandDots(self):
        pass
    def GetFillGrid(self,gridIdx):
        pass
    def GetFillGrids(self):
        pass
    def IsEqual(self,other):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetFillGrid(self,gridIdx,fillGrid):
        pass
    def SetFillGrids(self,fillGrids):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    GridCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HostOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsSolidFill=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LengthPerArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LinesPerLength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StrokesPerArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Target=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FillPatternElement(Element):
    @staticmethod
    def Create(document,fillPattern):
        pass
    def Dispose(self):
        pass
    def GetFillPattern(self):
        pass
    @staticmethod
    def GetFillPatternElementByName(document,target,name):
        pass
    def SetFillPattern(self,newFillPattern):
        pass
class FillPatternHostOrientation(Enum):
    AsText=None
    ToHost=None
    ToView=None
    value__=None
class FillPatternTarget(Enum):
    Drafting=None
    Model=None
    None_JEDIFIX=None
    value__=None
class FilterableValueProvider(object):
    def Dispose(self):
        pass
    def GetAssociatedGlobalParameterValue(self,element):
        pass
    def GetDoubleValue(self,element):
        pass
    def GetElementIdValue(self,element):
        pass
    def GetIntegerValue(self,element):
        pass
    def GetStringValue(self,element):
        pass
    def IsDoubleValueSupported(self,element):
        pass
    def IsElementIdValueSupported(self,element):
        pass
    def IsIntegerValueSupported(self,element):
        pass
    def IsStringValueSupported(self,element):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilterRule(object):
    def Dispose(self):
        pass
    def ElementPasses(self,element):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilterCategoryRule(FilterRule):
    @staticmethod
    def AllCategoriesFilterable(categories):
        pass
    def Dispose(self):
        pass
    def GetCategories(self):
        pass
    def SetCategories(self,categories):
        pass
    @staticmethod # known case of __new__
    def __new__(self,categories):
        pass
class FilterValueRule(FilterRule):
    def Dispose(self):
        pass
class FilterNumericValueRule(FilterValueRule):
    def Dispose(self):
        pass
    def GetEvaluator(self):
        pass
    def SetEvaluator(self,evaluator):
        pass
class FilterDoubleRule(FilterNumericValueRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,valueProvider,evaluator,ruleValue,epsilon):
        pass
    Epsilon=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RuleValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilteredElementCollector(object):
    def ContainedInDesignOption(self,designOptionId):
        pass
    def Dispose(self):
        pass
    def Excluding(self,idsToExclude):
        pass
    def FirstElement(self):
        pass
    def FirstElementId(self):
        pass
    def GetElementCount(self):
        pass
    def GetElementIdIterator(self):
        pass
    def GetElementIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def IntersectWith(self,other):
        pass
    @staticmethod
    def IsViewValidForElementIteration(document,viewId):
        pass
    def OfCategory(self,category):
        pass
    def OfCategoryId(self,categoryId):
        pass
    def OfClass(self,type):
        pass
    def OwnedByView(self,viewId):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def ToElementIds(self):
        pass
    def ToElements(self):
        pass
    def UnionWith(self,other):
        pass
    def WhereElementIsCurveDriven(self):
        pass
    def WhereElementIsElementType(self):
        pass
    def WhereElementIsNotElementType(self):
        pass
    def WhereElementIsViewIndependent(self):
        pass
    def WherePasses(self,filter):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilteredElementIdIterator(object):
    def Dispose(self):
        pass
    def GetCurrent(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilteredElementIterator(object):
    def Dispose(self):
        pass
    def GetCurrent(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilteredWorksetCollector(object):
    def Dispose(self):
        pass
    def FirstWorkset(self):
        pass
    def FirstWorksetId(self):
        pass
    def GetEnumerator(self):
        pass
    def GetWorksetIdIterator(self):
        pass
    def GetWorksetIterator(self):
        pass
    def OfKind(self,worksetKind):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def ToWorksetIds(self):
        pass
    def ToWorksets(self):
        pass
    def WherePasses(self,filter):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilteredWorksetIdIterator(object):
    def Dispose(self):
        pass
    def GetCurrent(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilteredWorksetIterator(object):
    def Dispose(self):
        pass
    def GetCurrent(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilterElement(Element):
    def Dispose(self):
        pass
    @staticmethod
    def IsNameUnique(*__args):
        pass
class FilterElementIdRule(FilterNumericValueRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,valueProvider,evaluator,ruleValue):
        pass
    RuleValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilterGlobalParameterAssociationRule(FilterNumericValueRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,valueProvider,evaluator,ruleValue):
        pass
    RuleValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilterIntegerRule(FilterNumericValueRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,valueProvider,evaluator,ruleValue):
        pass
    RuleValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilterInverseRule(FilterRule):
    def Dispose(self):
        pass
    def GetInnerRule(self):
        pass
    def SetInnerRule(self,innerRule):
        pass
    @staticmethod # known case of __new__
    def __new__(self,innerRule):
        pass
class FilterNumericRuleEvaluator(object):
    def Dispose(self):
        pass
    def Evaluate(self,lhs,rhs,epsilon=None):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilterNumericEquals(FilterNumericRuleEvaluator):
    def Dispose(self):
        pass
class FilterNumericGreater(FilterNumericRuleEvaluator):
    def Dispose(self):
        pass
class FilterNumericGreaterOrEqual(FilterNumericRuleEvaluator):
    def Dispose(self):
        pass
class FilterNumericLess(FilterNumericRuleEvaluator):
    def Dispose(self):
        pass
class FilterNumericLessOrEqual(FilterNumericRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringRuleEvaluator(object):
    def Dispose(self):
        pass
    def Evaluate(self,lhs,rhs,caseSensitive):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FilterStringBeginsWith(FilterStringRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringContains(FilterStringRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringEndsWith(FilterStringRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringEquals(FilterStringRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringGreater(FilterStringRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringGreaterOrEqual(FilterStringRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringLess(FilterStringRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringLessOrEqual(FilterStringRuleEvaluator):
    def Dispose(self):
        pass
class FilterStringRule(FilterValueRule):
    def Dispose(self):
        pass
    def GetEvaluator(self):
        pass
    def SetEvaluator(self,evaluator):
        pass
    @staticmethod # known case of __new__
    def __new__(self,valueProvider,evaluator,ruleString,caseSensitive):
        pass
    RuleString=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FindReferenceTarget(Enum):
    All=None
    Curve=None
    Edge=None
    Element=None
    Face=None
    Mesh=None
    value__=None
class FitDirectionType(Enum):
    Horizontal=None
    value__=None
    Vertical=None
class FittingAndAccessoryCalculationType(Enum):
    CalculateDefaultSettings=None
    CalculatePressureDrop=None
    Undefined=None
    ValidateCurrentSettings=None
    value__=None
class FittingAngleUsage(Enum):
    UseAnAngleIncrement=None
    UseAnyAngle=None
    UseSpecificAngles=None
    value__=None
class Floor(CeilingAndFloor):
    def Dispose(self):
        pass
    def GetNormalAtVerticalProjectionPoint(self,modelLocation,floorFace):
        pass
    def GetSpanDirectionSymbolIds(self):
        pass
    def GetVerticalProjectionPoint(self,modelLocation,floorFace):
        pass
    FloorType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SlabShapeEditor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpanDirectionAngle=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FloorFace(Enum):
    Bottom=None
    Top=None
    value__=None
class FloorType(HostObjAttributes):
    def Dispose(self):
        pass
    IsFoundationSlab=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralMaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FlowDirectionType(Enum):
    Bidirectional=None
    In=None
    Out=None
    value__=None
class FolderItemInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FootPrintRoof(RoofBase):
    def Dispose(self):
        pass
    def GetProfiles(self):
        pass
    CurtainGrids=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Form(GenericForm):
    def AddEdge(self,*__args):
        pass
    def AddProfile(self,edgeReference,param):
        pass
    def CanManipulateProfile(self,profileIndex):
        pass
    def CanManipulateSubElement(self,subElementReference):
        pass
    def ConstrainProfiles(self,masterProfileIndex):
        pass
    def DeleteProfile(self,profileIndex):
        pass
    def DeleteSubElement(self,subElementReference):
        pass
    def Dispose(self):
        pass
    def GetControlPoints(self,curveOrEdgeOrFaceReference):
        pass
    def GetCurvesAndEdgesReference(self,pointReference):
        pass
    def GetPathCurveIndexByCurveReference(self,curveReference):
        pass
    def GetProfileAndCurveLoopIndexFromReference(self,curveOrEdgeReference,profileIndex,curveLoopIndex):
        pass
    def IsAutoCreaseEdge(self,edgeReference):
        pass
    def IsBeginningFace(self,faceReference):
        pass
    def IsConnectingEdge(self,edgeReference):
        pass
    def IsCurveReference(self,curveReference):
        pass
    def IsEdgeReference(self,edgeReference):
        pass
    def IsEndFace(self,faceReference):
        pass
    def IsFaceReference(self,faceReference):
        pass
    def IsProfileEdge(self,curveOrEdgeReference):
        pass
    def IsReferenceOnlyProfile(self,profileIndex):
        pass
    def IsSideFace(self,faceReference):
        pass
    def IsVertexReference(self,vertexReference):
        pass
    def MoveProfile(self,profileIndex,offset):
        pass
    def MoveSubElement(self,subElementReference,offset):
        pass
    def Rehost(self,*__args):
        pass
    def RotateProfile(self,profileIndex,axis,angle):
        pass
    def RotateSubElement(self,subElementReference,axis,angle):
        pass
    def ScaleProfile(self,profileIndex,factor,origin):
        pass
    def ScaleSubElement(self,subElementReference,factor,origin):
        pass
    AreProfilesConstrained=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BaseOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasOneOrMoreReferenceProfiles=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasOpenGeometry=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsInXRayMode=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathCurveCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FormArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FormArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FormatOptions(object):
    def CanHaveUnitSymbol(self,displayUnit=None):
        pass
    def CanSuppressLeadingZeros(self,displayUnit=None):
        pass
    def CanSuppressSpaces(self,displayUnit=None):
        pass
    def CanSuppressTrailingZeros(self,displayUnit=None):
        pass
    def CanUsePlusPrefix(self,displayUnit=None):
        pass
    def Dispose(self):
        pass
    def GetValidUnitSymbols(self,displayUnit=None):
        pass
    def IsValidAccuracy(self,*__args):
        pass
    def IsValidForUnitType(self,unitType):
        pass
    def IsValidUnitSymbol(self,*__args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    Accuracy=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayUnits=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RoundingMethod=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SuppressLeadingZeros=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SuppressSpaces=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SuppressTrailingZeros=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UnitSymbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UseDefault=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UseDigitGrouping=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UsePlusPrefix=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FormatStatus(Enum):
    All=None
    Mixed=None
    None_JEDIFIX=None
    value__=None
class FormattedText(object):
    def AsTextRange(self):
        pass
    def Dispose(self):
        pass
    def Find(self,searchString,startIndex,matchCase,matchWholeWord):
        pass
    def GetAllCapsStatus(self,textRange=None):
        pass
    def GetBoldStatus(self,textRange=None):
        pass
    def GetIndentLevel(self,textRange):
        pass
    def GetItalicStatus(self,textRange=None):
        pass
    def GetListStartNumber(self,textRange):
        pass
    def GetListType(self,textRange):
        pass
    def GetMaximumIndentLevel(self):
        pass
    def GetMaximumListStartNumber(self):
        pass
    def GetMinimumListStartNumber(self):
        pass
    def GetPlainText(self,textRange=None):
        pass
    def GetSubscriptStatus(self,textRange=None):
        pass
    def GetSuperscriptStatus(self,textRange=None):
        pass
    def GetUnderlineStatus(self,textRange=None):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetAllCapsStatus(self,*__args):
        pass
    def SetBoldStatus(self,*__args):
        pass
    def SetIndentLevel(self,textRange,level):
        pass
    def SetItalicStatus(self,*__args):
        pass
    def SetListStartNumber(self,textRange,value):
        pass
    def SetListType(self,textRange,listType):
        pass
    def SetPlainText(self,*__args):
        pass
    def SetSubscriptStatus(self,*__args):
        pass
    def SetSuperscriptStatus(self,*__args):
        pass
    def SetUnderlineStatus(self,*__args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,plainText=None):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FormattedTextRun(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    BaselineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Bold=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Italic=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ListStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NewLine=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NewParagraph=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TabNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Text=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Underlined=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FormatUtils(object):
    @staticmethod
    def Format(document,unitType,value):
        pass
    __all__=[
        'Format',
    ]
class FormatValueOptions(object):
    def Dispose(self):
        pass
    def GetFormatOptions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetFormatOptions(self,formatOptions):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AppendUnitSymbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FormUtils(object):
    @staticmethod
    def CanBeDissolved(ADoc,elements):
        pass
    @staticmethod
    def DissolveForms(ADoc,elements,BondingPointSet=None):
        pass
    __all__=[
        'CanBeDissolved',
        'DissolveForms',
    ]
class Frame(object):
    @staticmethod
    def CanDefineRevitGeometry(frameOfReference):
        pass
    def Dispose(self):
        pass
    def IsOrthogonal(self):
        pass
    def IsOrthonormal(self):
        pass
    def IsRightHanded(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Transform(self,trf):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,origin=None,vec1=None,vec2=None,vec3=None):
        pass
    BasisX=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BasisY=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BasisZ=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
class FreeFormElement(GenericForm):
    def CanOffsetFace(self,face):
        pass
    @staticmethod
    def Create(document,geometry):
        pass
    def Dispose(self):
        pass
    def SetFaceOffset(self,face,offset):
        pass
    def UpdateSolidGeometry(self,newGeometry):
        pass
class GBXMLExportOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ExportEnergyModelType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GBXMLImportOptions(object):
class GenericImportOptions(object):
    RefPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GeomCombination(CombinableElement):
    def Dispose(self):
        pass
    AllMembers=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GeomCombinationSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GeomCombinationSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GeometryCreationUtilities(object):
    @staticmethod
    def CreateBlendGeometry(firstLoop,secondLoop,vertexPairs,solidOptions=None):
        pass
    @staticmethod
    def CreateExtrusionGeometry(profileLoops,extrusionDir,extrusionDist,solidOptions=None):
        pass
    @staticmethod
    def CreateFixedReferenceSweptGeometry(sweepPath,pathAttachmentCrvIdx,pathAttachmentParam,profileLoops,fixedReferenceDirection,solidOptions=None):
        pass
    @staticmethod
    def CreateLoftGeometry(profileLoops,solidOptions):
        pass
    @staticmethod
    def CreateRevolvedGeometry(coordinateFrame,profileLoops,startAngle,endAngle,solidOptions=None):
        pass
    @staticmethod
    def CreateSweptBlendGeometry(pathCurve,pathParams,profileLoops,vertexPairs,solidOptions=None):
        pass
    @staticmethod
    def CreateSweptGeometry(sweepPath,pathAttachmentCrvIdx,pathAttachmentParam,profileLoops,solidOptions=None):
        pass
    __all__=[
        'CreateBlendGeometry',
        'CreateExtrusionGeometry',
        'CreateFixedReferenceSweptGeometry',
        'CreateLoftGeometry',
        'CreateRevolvedGeometry',
        'CreateSweptBlendGeometry',
        'CreateSweptGeometry',
    ]
class GeometryElement(GeometryObject):
    def Dispose(self):
        pass
    def GetBoundingBox(self):
        pass
    def GetEnumerator(self):
        pass
    def GetTransformed(self,transform):
        pass
    def __contains__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    MaterialElement=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GeometryInstance(GeometryObject):
    def Dispose(self):
        pass
    def GetInstanceGeometry(self,transform=None):
        pass
    def GetSymbolGeometry(self,transform=None):
        pass
    Symbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SymbolGeometry=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transform=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ParameterElement(Element):
    def Dispose(self):
        pass
    def GetDefinition(self):
        pass
class GlobalParameter(ParameterElement):
    def CanChangeReporting(self):
        pass
    def CanLabelDimension(self,dimensionId):
        pass
    @staticmethod
    def Create(document,name,datatype):
        pass
    def Dispose(self):
        pass
    def GetAffectedElements(self):
        pass
    def GetAffectedGlobalParameters(self):
        pass
    def GetFormula(self):
        pass
    def GetLabeledDimensions(self):
        pass
    def GetLabelName(self):
        pass
    def GetValue(self):
        pass
    def HasValidTypeForReporting(self):
        pass
    @staticmethod
    def IsValidDataType(datatype):
        pass
    def IsValidFormula(self,expression):
        pass
    def LabelDimension(self,dimensionId):
        pass
    def SetDrivingDimension(self,dimensionId):
        pass
    def SetFormula(self,expression):
        pass
    def SetValue(self,value):
        pass
    def UnlabelDimension(self,dimensionId):
        pass
    IsDrivenByDimension=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsDrivenByFormula=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsReporting=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GlobalParametersManager(object):
    @staticmethod
    def AreGlobalParametersAllowed(document):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def FindByName(document,name):
        pass
    @staticmethod
    def GetAllGlobalParameters(document):
        pass
    @staticmethod
    def GetGlobalParametersOrdered(document):
        pass
    @staticmethod
    def IsUniqueName(document,name):
        pass
    @staticmethod
    def IsValidGlobalParameter(document,parameterId):
        pass
    @staticmethod
    def MoveParameterDownOrder(document,parameterId):
        pass
    @staticmethod
    def MoveParameterUpOrder(document,parameterId):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    @staticmethod
    def SortParameters(document,order):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GradientBackgroundSettings(BackgroundSettings):
    def Dispose(self):
        pass
    GroundColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizonColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SkyColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GraphicsStyle(Element):
    def Dispose(self):
        pass
    GraphicsStyleCategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GraphicsStyleType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GraphicsStyleType(Enum):
    Cut=None
    Projection=None
    value__=None
class Grid(DatumPlane):
    @staticmethod
    def Create(document,*__args):
        pass
    def Dispose(self):
        pass
    def GetExtents(self):
        pass
    def SetVerticalExtents(self,bottom,top):
        pass
    Curve=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCurved=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GridNode(object):
    @staticmethod # known case of __new__
    def __new__(self,uIndex,vIndex):
        pass
    UIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GridNodeLocation(Enum):
    Boundary=None
    Exterior=None
    Interior=None
    value__=None
class GridSegmentDirection(Enum):
    NegativeU=None
    NegativeV=None
    PositiveU=None
    PositiveV=None
    value__=None
class GridType(LineAndTextAttrSymbol):
    def Dispose(self):
        pass
class Group(Element):
    def Dispose(self):
        pass
    def GetMemberIds(self):
        pass
    def UngroupMembers(self):
        pass
    GroupType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GroupNode(RenderNode):
    def Dispose(self):
        pass
    def GetSymbolId(self):
        pass
    def GetTransform(self):
        pass
class GroupSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GroupSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class GroupType(ElementType):
    def Dispose(self):
        pass
    Groups=property(lambda self:object(),lambda self,v:None,lambda self:None)
class HermiteFace(Face):
    def Dispose(self):
        pass
    MixedDerivs=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Points=property(lambda self:object(),lambda self,v:None,lambda self:None)
class HermiteSpline(Curve):
    @staticmethod
    def Create(controlPoints,periodic,tangents=None):
        pass
    def Dispose(self):
        pass
    ControlPoints=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsPeriodic=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Parameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Tangents=property(lambda self:object(),lambda self,v:None,lambda self:None)
class HermiteSplineTangents(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EndTangent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartTangent=property(lambda self:object(),lambda self,v:None,lambda self:None)
class HermiteSurface(Surface):
    @staticmethod
    def Create(nU,nV,points,periodicU=None,periodicV=None):
        pass
    def Dispose(self):
        pass
    def IsValid(self):
        pass
class HiddenLineViewsType(Enum):
    RasterProcessing=None
    value__=None
    VectorProcessing=None
class HomeCamera(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other):
        pass
    BottomAngleOfFieldOfView=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Center=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EyePosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeftAngleOfFieldOfView=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OrthogonalProjectionHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OrthogonalProjectionWidth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Pivot=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RightAngleOfFieldOfView=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopAngleOfFieldOfView=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UpDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class HorizontalAlign(Enum):
    Center=None
    Left=None
    Right=None
    value__=None
class HorizontalAlignmentStyle(Enum):
    Center=None
    Left=None
    Right=None
    value__=None
class HorizontalTextAlignment(Enum):
    Center=None
    Left=None
    Right=None
    value__=None
class HostedSweep(HostObject):
    def AddSegment(self,targetRef):
        pass
    def Dispose(self):
        pass
    def GetEndPointParameter(self,targetRef,endIdx):
        pass
    def HorizontalFlip(self):
        pass
    def RemoveSegment(self,targetRef):
        pass
    def SetEndPointParameter(self,targetRef,endIdx,param):
        pass
    def VerticalFlip(self):
        pass
    Angle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalFlipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Length=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VerticalFlipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VerticalOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
class HostedSweepType(HostObjAttributes):
    def Dispose(self):
        pass
class HostObjectUtils(object):
    @staticmethod
    def GetBottomFaces(hostObject):
        pass
    @staticmethod
    def GetSideFaces(hostObject,side):
        pass
    @staticmethod
    def GetTopFaces(hostObject):
        pass
    __all__=[
        'GetBottomFaces',
        'GetSideFaces',
        'GetTopFaces',
    ]
class ICentralLockedCallback:
    def ShouldWaitForLockAvailability(self):
        pass
    def __init__(self,*args):
        pass
class IConnector:
    def __init__(self,*args):
        pass
    CoordinateSystem=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Domain=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Height=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Radius=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Shape=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
class IDataConversionMonitor:
    def GetVerbosity(self):
        pass
    def ProcessMessage(self,messageId,messageSeverity,entityIds):
        pass
    def __init__(self,*args):
        pass
class IDuplicateTypeNamesHandler:
    def OnDuplicateTypeNamesFound(self,args):
        pass
    def __init__(self,*args):
        pass
class IExportContext:
    def Finish(self):
        pass
    def IsCanceled(self):
        pass
    def OnElementBegin(self,elementId):
        pass
    def OnElementEnd(self,elementId):
        pass
    def OnFaceBegin(self,node):
        pass
    def OnFaceEnd(self,node):
        pass
    def OnInstanceBegin(self,node):
        pass
    def OnInstanceEnd(self,node):
        pass
    def OnLight(self,node):
        pass
    def OnLinkBegin(self,node):
        pass
    def OnLinkEnd(self,node):
        pass
    def OnMaterial(self,node):
        pass
    def OnPolymesh(self,node):
        pass
    def OnRPC(self,node):
        pass
    def OnViewBegin(self,node):
        pass
    def OnViewEnd(self,elementId):
        pass
    def Start(self):
        pass
    def __init__(self,*args):
        pass
class IExtension:
    def __init__(self,*args):
        pass
class IExternalDBApplication:
    def OnShutdown(self,application):
        pass
    def OnStartup(self,application):
        pass
    def __init__(self,*args):
        pass
class IExternalResourceServer(IExternalServer):
    def AreSameResources(self,reference1,reference2):
        pass
    def GetIconPath(self):
        pass
    def GetInformationLink(self):
        pass
    def GetInSessionPath(self,reference,originalDisplayPath):
        pass
    def GetResourceVersionStatus(self,reference):
        pass
    def GetShortName(self):
        pass
    def GetTypeSpecificServerOperations(self,extensions):
        pass
    def IsResourceWellFormed(self,extRef):
        pass
    def LoadResource(self,loadRequestId,resourceType,desiredResource,loadContext,loadResults):
        pass
    def SetupBrowserData(self,browseData):
        pass
    def SupportsExternalResourceType(self,type):
        pass
    def __init__(self,*args):
        pass
class IFailuresPreprocessor:
    def PreprocessFailures(self,failuresAccessor):
        pass
    def __init__(self,*args):
        pass
class IFailuresProcessor:
    def Dismiss(self,document):
        pass
    def ProcessFailures(self,data):
        pass
    def __init__(self,*args):
        pass
class IFamilyLoadOptions:
    def OnFamilyFound(self,familyInUse,overwriteParameterValues):
        pass
    def OnSharedFamilyFound(self,sharedFamily,familyInUse,source,overwriteParameterValues):
        pass
    def __init__(self,*args):
        pass
class IFCExportOptions(object):
    def AddOption(self,name,value):
        pass
    def Assign(self,sourceOptions):
        pass
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,from_JEDIFIX=None):
        pass
    ExportBaseQuantities=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyMappingFile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FileVersion=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FilterViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpaceBoundaryLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WallAndColumnSplitting=property(lambda self:object(),lambda self,v:None,lambda self:None)
class IFCVersion(Enum):
    Default=None
    IFC2x2=None
    IFC2x3=None
    IFC2x3BFM=None
    IFC2x3CV2=None
    IFC2x3FM=None
    IFC4=None
    IFC4DTV=None
    IFC4RV=None
    IFCBCA=None
    IFCCOBIE=None
    value__=None
class IGetLocalPathForOpenCallback:
    def GetLocalPathForOpen(self,desiredResource):
        pass
    def __init__(self,*args):
        pass
class ImageBackgroundSettings(BackgroundSettings):
    def Dispose(self):
        pass
    BackgroundImageFit=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FilePath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OffsetHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OffsetWidth=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ImageExportOptions(object):
    def Dispose(self):
        pass
    @staticmethod
    def GetFileName(aDoc,dbViewId):
        pass
    def GetViewsAndSheets(self):
        pass
    @staticmethod
    def IsValidFileName(filePath):
        pass
    @staticmethod
    def IsValidForSaveToProjectAsImage(options,doc):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetViewsAndSheets(self,viewsAndSheets):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ExportRange=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FilePath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FitDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HLRandWFViewsFileType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ImageResolution=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PixelSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShadowViewsFileType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShouldCreateWebSite=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Zoom=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ZoomType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ImageFileType(Enum):
    BMP=None
    JPEGLossless=None
    JPEGMedium=None
    JPEGSmallest=None
    PNG=None
    TARGA=None
    TIFF=None
    value__=None
class ImageImportOptions(GenericImportOptions):
    Placement=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Resolution=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ImageResolution(Enum):
    DPI_150=None
    DPI_300=None
    DPI_600=None
    DPI_72=None
    value__=None
class ImageType(ElementType):
    @staticmethod
    def Create(document,imagePath):
        pass
    def Dispose(self):
        pass
    def GetImage(self):
        pass
    def IsLoadedFromFile(self):
        pass
    def Reload(self):
        pass
    def ReloadFrom(self,imagePath):
        pass
    Path=property(lambda self:object(),lambda self,v:None,lambda self:None)
class View(Element):
    def AddFilter(self,filterElementId):
        pass
    def AllowsAnalysisDisplay(self):
        pass
    def ApplyViewTemplateParameters(self,otherView):
        pass
    def AreGraphicsOverridesAllowed(self):
        pass
    def CanCategoryBeHidden(self,elementId):
        pass
    def CanCategoryBeHiddenTemporary(self,elementId):
        pass
    def CanEnableTemporaryViewPropertiesMode(self):
        pass
    def CanModifyDetailLevel(self):
        pass
    def CanModifyDisplayStyle(self):
        pass
    def CanModifyViewDiscipline(self):
        pass
    def CanUseDepthCueing(self):
        pass
    def CanUseTemporaryVisibilityModes(self):
        pass
    def CanViewBeDuplicated(self,duplicateOption):
        pass
    def ConvertTemporaryHideIsolateToPermanent(self):
        pass
    def ConvertToIndependent(self):
        pass
    def DisableTemporaryViewMode(self,mode):
        pass
    def Dispose(self):
        pass
    def Duplicate(self,duplicateOption):
        pass
    def EnableRevealHiddenMode(self):
        pass
    def EnableTemporaryViewPropertiesMode(self,viewTemplateId):
        pass
    def GetBackground(self):
        pass
    def GetCategoryHidden(self,categoryId):
        pass
    def GetCategoryOverrides(self,categoryId):
        pass
    def GetCropRegionShapeManager(self):
        pass
    @staticmethod
    def GetCropRegionShapeManagerForReferenceCallout(doc,callout):
        pass
    def GetDependentViewIds(self):
        pass
    def GetDepthCueing(self):
        pass
    def GetElementOverrides(self,elementId):
        pass
    def GetFilterOverrides(self,filterElementId):
        pass
    def GetFilters(self):
        pass
    def GetFilterVisibility(self,filterElementId):
        pass
    def GetNonControlledTemplateParameterIds(self):
        pass
    def GetPointCloudOverrides(self):
        pass
    def GetPrimaryViewId(self):
        pass
    def GetReferenceCallouts(self):
        pass
    def GetReferenceElevations(self):
        pass
    def GetReferenceSections(self):
        pass
    def GetSketchyLines(self):
        pass
    def GetTemplateParameterIds(self):
        pass
    def GetTemporaryViewPropertiesId(self):
        pass
    def GetTemporaryViewPropertiesName(self):
        pass
    def GetViewDisplayModel(self):
        pass
    def GetVisibility(self,category):
        pass
    def GetWorksetVisibility(self,worksetId):
        pass
    def GetWorksharingDisplayMode(self):
        pass
    def HasDetailLevel(self):
        pass
    def HasDisplayStyle(self):
        pass
    def HasViewDiscipline(self):
        pass
    def HideActiveWorkPlane(self):
        pass
    def HideCategoriesTemporary(self,elementIds):
        pass
    def HideCategoryTemporary(self,elementId):
        pass
    def HideElements(self,elementIdSet):
        pass
    def HideElementsTemporary(self,elementIdSet):
        pass
    def HideElementTemporary(self,elementId):
        pass
    def IsCategoryOverridable(self,categoryId):
        pass
    def IsElementVisibleInTemporaryViewMode(self,mode,id):
        pass
    def IsFilterApplied(self,filterElementId):
        pass
    def IsInTemporaryViewMode(self,mode):
        pass
    def IsolateCategoriesTemporary(self,elementIds):
        pass
    def IsolateCategoryTemporary(self,elementId):
        pass
    def IsolateElementsTemporary(self,elementIds):
        pass
    def IsolateElementTemporary(self,elementId):
        pass
    def IsTemporaryHideIsolateActive(self):
        pass
    def IsTemporaryViewPropertiesModeEnabled(self):
        pass
    @staticmethod
    def IsValidViewScale(viewScale):
        pass
    def IsValidViewTemplate(self,templateId):
        pass
    def IsWorksetVisible(self,worksetId):
        pass
    def Print(self,*__args):
        pass
    def RemoveFilter(self,filterElementId):
        pass
    def SetBackground(self,background):
        pass
    def SetCategoryHidden(self,categoryId,hide):
        pass
    def SetCategoryOverrides(self,categoryId,overrideGraphicSettings):
        pass
    def SetDepthCueing(self,depthCueing):
        pass
    def SetElementOverrides(self,elementId,overrideGraphicSettings):
        pass
    def SetFilterOverrides(self,filterElementId,overrideGraphicSettings):
        pass
    def SetFilterVisibility(self,filterElementId,visibility):
        pass
    def SetNonControlledTemplateParameterIds(self,newSet):
        pass
    def SetSketchyLines(self,sketchyLines):
        pass
    def SetViewDisplayModel(self,viewDisplayModel):
        pass
    def SetVisibility(self,category,visible):
        pass
    def SetWorksetVisibility(self,worksetId,visible):
        pass
    def SetWorksharingDisplayMode(self,displayMode):
        pass
    def ShowActiveWorkPlane(self):
        pass
    def SupportsRevealConstraints(self):
        pass
    def SupportsWorksharingDisplayMode(self,mode):
        pass
    def UnhideElements(self,elementIdSet):
        pass
    AnalysisDisplayStyleId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AreAnalyticalModelCategoriesHidden=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AreAnnotationCategoriesHidden=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AreImportCategoriesHidden=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AreModelCategoriesHidden=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ArePointCloudsHidden=property(lambda self:object(),lambda self,v:None,lambda self:None)
    AssociatedAssemblyInstanceId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanBePrinted=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CropBox=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CropBoxActive=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CropBoxVisible=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DetailLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Discipline=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GenLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsAssemblyView=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTemplate=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Outline=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PartsVisibility=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RevealConstraintsMode=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RightDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Scale=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShadowIntensity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SketchPlane=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SunAndShadowSettings=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SunlightIntensity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TemporaryViewModes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Title=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UpDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewTemplateId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewDrafting(View):
    @staticmethod
    def Create(document,viewFamilyTypeId):
        pass
    def Dispose(self):
        pass
class ImageView(ViewDrafting):
    @staticmethod
    def Create(document,imageFileName):
        pass
    def Dispose(self):
        pass
    ImageInstanceId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class IModelExportContext(IExportContext):
    def OnCurve(self,node):
        pass
    def OnLineSegment(self,segment):
        pass
    def OnPoint(self,node):
        pass
    def OnPolyline(self,node):
        pass
    def OnPolylineSegments(self,segments):
        pass
    def OnText(self,node):
        pass
    def __init__(self,*args):
        pass
class ImportColorMode(Enum):
    BlackAndWhite=None
    Inverted=None
    Preserved=None
    value__=None
class ImportExportFileFormat(Enum):
    Civil3D=None
    DGN=None
    DWF=None
    DWFX=None
    DWG=None
    DXF=None
    FBX=None
    GBXML=None
    IFC=None
    Image=None
    Inventor=None
    NWC=None
    SAT=None
    value__=None
class ImportInstance(Instance):
    def Dispose(self):
        pass
    def GetVisibility(self):
        pass
    def SetVisibility(self,visibility):
        pass
    IsLinked=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ImportPlacement(Enum):
    Centered=None
    Origin=None
    Shared=None
    Site=None
    value__=None
class ImportUnit(Enum):
    Centimeter=None
    Custom=None
    Decimeter=None
    Default=None
    Foot=None
    Inch=None
    Meter=None
    Millimeter=None
    value__=None
class INavisworksExporter(IExternalServer):
    def Export(self,document,folder,name,options):
        pass
    def ValidateExportOptions(self,document,folder,name,options,exceptionMessage):
        pass
    def __init__(self,*args):
        pass
class IndependentTag(Element):
    def CanLeaderEndConditionBeAssigned(self,leaderEndCondition):
        pass
    def Dispose(self):
        pass
    def GetTaggedLocalElement(self):
        pass
    HasLeader=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsMaterialTag=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsMulticategoryTag=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsOrphaned=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderElbow=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderEnd=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderEndCondition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MultiReferenceAnnotationId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TaggedElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TaggedLocalElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagHeadPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagText=property(lambda self:object(),lambda self,v:None,lambda self:None)
class InSessionPrintSetting(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    PrintParameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
class InSessionViewSheetSet(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Views=property(lambda self:object(),lambda self,v:None,lambda self:None)
class InstanceBinding(ElementBinding):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,categories=None):
        pass
class InstanceNode(GroupNode):
    def Dispose(self):
        pass
class InstanceVoidCutUtils(object):
    @staticmethod
    def AddInstanceVoidCut(document,element,cuttingInstance):
        pass
    @staticmethod
    def CanBeCutWithVoid(element):
        pass
    @staticmethod
    def GetCuttingVoidInstances(element):
        pass
    @staticmethod
    def GetElementsBeingCut(cuttingInstance):
        pass
    @staticmethod
    def InstanceVoidCutExists(element,cuttingInstance):
        pass
    @staticmethod
    def IsVoidInstanceCuttingElement(element):
        pass
    @staticmethod
    def RemoveInstanceVoidCut(document,element,cuttingInstance):
        pass
    __all__=[
        'AddInstanceVoidCut',
        'CanBeCutWithVoid',
        'GetCuttingVoidInstances',
        'GetElementsBeingCut',
        'InstanceVoidCutExists',
        'IsVoidInstanceCuttingElement',
        'RemoveInstanceVoidCut',
    ]
class MEPCurve(HostObject):
    def Dispose(self):
        pass
    ConnectorManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Diameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Height=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LevelOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MEPSystem=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReferenceLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
class InsulationLiningBase(MEPCurve):
    def Dispose(self):
        pass
    @staticmethod
    def GetInsulationIds(document,elemId):
        pass
    @staticmethod
    def GetLiningIds(document,elemId):
        pass
    @staticmethod
    def IsValidThickness(thickness):
        pass
    HostElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Thickness=property(lambda self:object(),lambda self,v:None,lambda self:None)
class IntegerParameterValue(ParameterValue):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,value=None):
        pass
    Value=property(lambda self:object(),lambda self,v:None,lambda self:None)
class IntegerRange(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    High=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Low=property(lambda self:object(),lambda self,v:None,lambda self:None)
class InternalDefinition(Definition):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetAllowVaryBetweenGroups(self,document,allowVaryBetweenGroups):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    BuiltInParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterGroup=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VariesAcrossGroups=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visible=property(lambda self:object(),lambda self,v:None,lambda self:None)
class InternalDefinitions(Definitions):
    def Dispose(self):
        pass
class IntersectionResult(APIObject):
    def Dispose(self):
        pass
    Distance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EdgeObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EdgeParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Parameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UVPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XYZPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
class IntersectionResultArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class IntersectionResultArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class IOnLocalLinkSharedCoordinatesSavedCallback:
    def OnLocalLinkSharedCoordinatesSaved(self,changedResource):
        pass
    def __init__(self,*args):
        pass
class IPerformanceAdviserRule:
    def ExecuteElementCheck(self,document,element):
        pass
    def FinalizeCheck(self,document):
        pass
    def GetDescription(self):
        pass
    def GetElementFilter(self,document):
        pass
    def GetName(self):
        pass
    def InitCheck(self,document):
        pass
    def WillCheckElements(self):
        pass
    def __init__(self,*args):
        pass
class IPhotoRenderContext(IExportContext):
    def __init__(self,*args):
        pass
class IPrintSetting:
    def __init__(self,*args):
        pass
    PrintParameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ISaveSharedCoordinatesCallback:
    def GetSaveModifiedLinksOption(self,link):
        pass
    def __init__(self,*args):
        pass
class ISaveSharedCoordinatesCallbackForUnloadLocally:
    def GetSaveModifiedLinksOptionForUnloadLocally(self,link):
        pass
    def __init__(self,*args):
        pass
class ITransactionFinalizer:
    def OnCommitted(self,document,strTransactionName):
        pass
    def OnRolledBack(self,document,strTransactionName):
        pass
    def __init__(self,*args):
        pass
class ITransientElementMaker:
    def Execute(self):
        pass
    def __init__(self,*args):
        pass
class IUpdater:
    def Execute(self,data):
        pass
    def GetAdditionalInformation(self):
        pass
    def GetChangePriority(self):
        pass
    def GetUpdaterId(self):
        pass
    def GetUpdaterName(self):
        pass
    def __init__(self,*args):
        pass
class IViewSheetSet:
    def __init__(self,*args):
        pass
    Views=property(lambda self:object(),lambda self,v:None,lambda self:None)
class JoinGeometryUtils(object):
    @staticmethod
    def AreElementsJoined(document,firstElement,secondElement):
        pass
    @staticmethod
    def GetJoinedElements(document,element):
        pass
    @staticmethod
    def IsCuttingElementInJoin(document,firstElement,secondElement):
        pass
    @staticmethod
    def JoinGeometry(document,firstElement,secondElement):
        pass
    @staticmethod
    def SwitchJoinOrder(document,firstElement,secondElement):
        pass
    @staticmethod
    def UnjoinGeometry(document,firstElement,secondElement):
        pass
    __all__=[
        'AreElementsJoined',
        'GetJoinedElements',
        'IsCuttingElementInJoin',
        'JoinGeometry',
        'SwitchJoinOrder',
        'UnjoinGeometry',
    ]
class JoinType(Enum):
    Abut=None
    Extension=None
    Miter=None
    None_JEDIFIX=None
    SquareOff=None
    value__=None
class JunctionType(Enum):
    Tap=None
    Tee=None
    value__=None
class KeyBasedTreeEntriesIterator(object):
    def Dispose(self):
        pass
    def IsDone(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Reset(self):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class KeyBasedTreeEntriesLoadContent(ExternalResourceLoadContent):
    def AddEntry(self,entry):
        pass
    def BuildEntries(self):
        pass
    def CanAddEntry(self,entry):
        pass
    def Dispose(self):
        pass
    def GetEntries(self):
        pass
    def GetLoadResults(self):
        pass
    @staticmethod
    def IsEntriesBuilt(content):
        pass
    def Reset(self):
        pass
class KeyBasedTreeEntriesLoadResults(object):
    def Dispose(self):
        pass
    def GetFailureMessages(self):
        pass
    def GetFileReadErrors(self):
        pass
    def GetFileSyntaxErrors(self):
        pass
    def GetKeyBasedTreeEntryErrors(self,type=None):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class KeyBasedTreeEntryError(object):
    def Dispose(self):
        pass
    def GetEntry(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ErrorType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class KeyBasedTreeEntryErrorType(Enum):
    BadClassificationCategoryId=None
    BadClassificationLevel=None
    CircularParentage=None
    DuplicateEntry=None
    InvalidClassificationCode=None
    MissingParent=None
    value__=None
class KeynoteEntries(KeyBasedTreeEntries):
    def Dispose(self):
        pass
    @staticmethod
    def LoadKeynoteEntriesFromFile(filePath,keynoteContent):
        pass
class KeynoteEntry(KeyBasedTreeEntry):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,key,*__args):
        pass
    KeynoteText=property(lambda self:object(),lambda self,v:None,lambda self:None)
class KeynoteTable(KeyBasedTreeEntryTable):
    def Dispose(self):
        pass
    @staticmethod
    def GetKeynoteTable(aDoc):
        pass
class LabelType(Enum):
    LengthOfSegment=None
    NumberOfSegments=None
    NumberOfWitnessLines=None
    TotalLength=None
    value__=None
class LabelUtils(object):
    def Dispose(self):
        pass
    @staticmethod
    def GetLabelFor(*__args):
        pass
    @staticmethod
    def GetStructuralSectionShapeName(shape):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LayerCategoryType(Enum):
    AnalyticalModel=None
    Annotation=None
    Imported=None
    Model=None
    Modifier=None
    Unsorted=None
    value__=None
class LayerModifier(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,modifierType=None,separator=None):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ModifierType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Separator=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LayoutRule(APIObject):
    def Dispose(self):
        pass
class LayoutRuleClearSpacing(LayoutRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,spacing,justifyType):
        pass
    JustifyType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Spacing=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LayoutRuleFixedDistance(LayoutRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,spacing,justifyType):
        pass
    JustifyType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Spacing=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LayoutRuleFixedNumber(LayoutRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,numberOfLines):
        pass
    NumberOfLines=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LayoutRuleMaximumSpacing(LayoutRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,spacing):
        pass
    Spacing=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Leader(APIObject):
    def Dispose(self):
        pass
    Anchor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Elbow=property(lambda self:object(),lambda self,v:None,lambda self:None)
    End=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderShape=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LeaderArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LeaderArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LeaderAtachement(Enum):
    BottomLine=None
    Midpoint=None
    TopLine=None
    value__=None
class LeaderEndCondition(Enum):
    Attached=None
    Free=None
    value__=None
class LeaderShape(Enum):
    Arc=None
    Kinked=None
    Straight=None
    value__=None
class Level(DatumPlane):
    @staticmethod
    def Create(document,elevation):
        pass
    def Dispose(self):
        pass
    def GetPlaneReference(self):
        pass
    Elevation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectElevation=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LevelType(LineAndTextAttrSymbol):
    def Dispose(self):
        pass
class LightAndMaterialAccuracyMode(Enum):
    Advanced=None
    Simplified=None
    value__=None
class LightingSource(Enum):
    ExteriorArtificial=None
    ExteriorSun=None
    ExteriorSunAndArtificial=None
    InteriorArtificial=None
    InteriorSun=None
    InteriorSunAndArtificial=None
    value__=None
class LightNode(ContentNode):
    def Dispose(self):
        pass
class Line(Curve):
    @staticmethod
    def CreateBound(endpoint1,endpoint2):
        pass
    @staticmethod
    def CreateUnbound(origin,direction):
        pass
    def Dispose(self):
        pass
    Direction=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LinearArray(BaseArray):
    @staticmethod
    def ArrayElementsWithoutAssociation(aDoc,dBView,ids,count,translationToAnchorMember,anchorMember):
        pass
    @staticmethod
    def ArrayElementWithoutAssociation(aDoc,dBView,id,count,translationToAnchorMember,anchorMember):
        pass
    @staticmethod
    def Create(aDoc,dBView,*__args):
        pass
    def Dispose(self):
        pass
    def GetCopiedMemberIds(self):
        pass
    def GetOriginalMemberIds(self):
        pass
    @staticmethod
    def IsElementArrayable(aDoc,id):
        pass
    @staticmethod
    def IsValidArraySize(count):
        pass
    NumMembers=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LinePattern(object):
    def Dispose(self):
        pass
    def GetSegments(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetSegments(self,lineSegs):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,name=None):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LinePatternElement(Element):
    @staticmethod
    def Create(document,linePattern):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetLinePattern(document=None,elementId=None):
        pass
    @staticmethod
    def GetLinePatternElementByName(document,name):
        pass
    @staticmethod
    def GetSolidPatternId():
        pass
    def SetLinePattern(self,newLinePattern):
        pass
class LinePatternSegment(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,type=None,length=None):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Length=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Type=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LinePatternSegmentType(Enum):
    Dash=None
    Dot=None
    Invalid=None
    Space=None
    value__=None
class LineProperties(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Color=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineWidth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transparency=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LineScaling(Enum):
    ModelSpace=None
    PaperSpace=None
    value__=None
    ViewScale=None
class LineSegment(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EndParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EndPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LinkConversionData(object):
    def Dispose(self):
        pass
    def GetOptions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Path=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServerId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LinkedFileStatus(Enum):
    CanBeUpgraded=None
    Imported=None
    InClosedWorkset=None
    Invalid=None
    Loaded=None
    LocallyUnloaded=None
    NotFound=None
    Unloaded=None
    value__=None
class LinkElementId(object):
    def Equals(self,obj):
        pass
    def __eq__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    def __ne__(self,*args):
        pass
    HostElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LinkedElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LinkInstanceId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LinkLoadContent(ExternalResourceLoadContent):
    def Dispose(self):
        pass
    def GetLinkDataPath(self):
        pass
    def GetLinkLoadResult(self):
        pass
    def SetLinkDataPath(self,linkPath):
        pass
class LinkNode(GroupNode):
    def Dispose(self):
        pass
    def GetDocument(self):
        pass
class ListType(Enum):
    ArabicNumbers=None
    Bullet=None
    LowerCaseLetters=None
    Mixed=None
    None_JEDIFIX=None
    UpperCaseLetters=None
    value__=None
class LoadOperationType(Enum):
    Automatic=None
    Explicit=None
    value__=None
class Location(APIObject):
    def Dispose(self):
        pass
    def Move(self,translation):
        pass
    def Rotate(self,axis,angle):
        pass
class LocationCurve(Location):
    def Dispose(self):
        pass
    Curve=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LocationPoint(Location):
    def Dispose(self):
        pass
    Point=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Rotation=property(lambda self:object(),lambda self,v:None,lambda self:None)
class LogicalAndFilter(ElementLogicalFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
class LogicalOrFilter(ElementLogicalFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
class MarginType(Enum):
    NoMargin=None
    PrinterLimit=None
    UserDefined=None
    value__=None
class MassDisplayTemporaryOverrideType(Enum):
    ShowMassByViewSettings=None
    ShowMassFormAndFloors=None
    ShowMassSurfaceTypes=None
    ShowMassZonesAndShades=None
    value__=None
class MassInstanceUtils(object):
    @staticmethod
    def AddMassLevelDataToMassInstance(document,massInstanceId,levelId):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetGrossFloorArea(document,massInstanceId):
        pass
    @staticmethod
    def GetGrossSurfaceArea(document,massInstanceId):
        pass
    @staticmethod
    def GetGrossVolume(document,massInstanceId):
        pass
    @staticmethod
    def GetJoinedElementIds(document,massInstanceId):
        pass
    @staticmethod
    def GetMassLevelDataIds(document,massInstanceId):
        pass
    @staticmethod
    def GetMassLevelIds(document,massInstanceId):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    @staticmethod
    def RemoveMassLevelDataFromMassInstance(document,massInstanceId,levelId):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Material(Element):
    def ClearMaterialAspect(self,aspect):
        pass
    @staticmethod
    def Create(document,name):
        pass
    def Dispose(self):
        pass
    def Duplicate(self,name):
        pass
    @staticmethod
    def IsMaterialOrValidDefault(pElem,materialId):
        pass
    @staticmethod
    def IsNameUnique(aDocument,name):
        pass
    def SetMaterialAspectByPropertySet(self,aspect,propertySetId):
        pass
    AppearanceAssetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Color=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutPatternColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutPatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Glow=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialCategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialClass=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Shininess=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Smoothness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralAssetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SurfacePatternColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SurfacePatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalAssetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transparency=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UseRenderAppearanceForShading=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MaterialAspect(Enum):
    Structural=None
    Thermal=None
    value__=None
class MaterialFunctionAssignment(Enum):
    Finish1=None
    Finish2=None
    Insulation=None
    Membrane=None
    None_JEDIFIX=None
    StructuralDeck=None
    Structure=None
    Substrate=None
    value__=None
class MaterialNode(RenderNode):
    def Dispose(self):
        pass
    def GetAppearance(self):
        pass
    def GetAppearanceOverride(self):
        pass
    Color=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Glossiness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasOverriddenAppearance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Smoothness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThumbnailFile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transparency=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MaterialPropertyPathType(Enum):
    Bump=None
    Cutouts=None
    FinishBumps=None
    General=None
    ReliefPattern=None
    Transparency=None
    value__=None
    Weathering=None
class MEPCalculationServerInfo(object):
    def Dispose(self):
        pass
    @staticmethod
    def GetMEPCalculationServerInfo(famInst):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServerId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ServerName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PipeUseDefinitionOnTypeGUID=None
class MEPConnectorInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsPrimary=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsSecondary=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LinkedConnector=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MEPCurveType(HostObjAttributes):
    def Dispose(self):
        pass
    Cross=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Elbow=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MultiShapeTransition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreferredJunctionType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Roughness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RoutingPreferenceManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Tap=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Tee=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Union=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MEPFamilyConnectorInfo(MEPConnectorInfo):
    def Dispose(self):
        pass
    def GetAssociateFamilyParameterId(self,connectorParameterId):
        pass
    def GetConnectorParameterValue(self,connectorParameterId):
        pass
class MEPModel(APIObject):
    def Dispose(self):
        pass
    AssignedElectricalSystems=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConnectorManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ElectricalSystems=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MEPSize(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,nominalDiameter,innerDiameter,outerDiameter,usedInSizeLists,usedInSizing):
        pass
    InnerDiameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NominalDiameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OuterDiameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UsedInSizeLists=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UsedInSizing=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MEPSystem(Element):
    def Add(self,connectors):
        pass
    def Dispose(self):
        pass
    def DivideSystem(self,ADoc):
        pass
    def GetCriticalPathSectionNumbers(self):
        pass
    def getElementsInNetwork(self,*args):
        pass
    def getFlow(self,*args):
        pass
    def GetPhysicalNetworksNumber(self):
        pass
    def GetSectionByIndex(self,index):
        pass
    def GetSectionByNumber(self,sectionNumber):
        pass
    def getStaticPressure(self,*args):
        pass
    def IsSystemDividable(self):
        pass
    def Remove(self,*__args):
        pass
    def __add__(self,*args):
        pass
    BaseEquipment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BaseEquipmentConnector=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConnectorManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Elements=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasDesignParts=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasFabricationParts=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasPlaceholders=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsMultipleNetwork=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValid=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PressureLossOfCriticalPath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SectionsCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MEPSystemClassification(Enum):
    CableTrayConduit=None
    Communication=None
    CondensateDrain=None
    Controls=None
    DataCircuit=None
    DomesticColdWater=None
    DomesticHotWater=None
    ExhaustAir=None
    FireAlarm=None
    FireProtectDry=None
    FireProtectOther=None
    FireProtectPreaction=None
    FireProtectWet=None
    Fitting=None
    Global=None
    NurseCall=None
    OtherAir=None
    OtherPipe=None
    PowerBalanced=None
    PowerCircuit=None
    PowerUnBalanced=None
    Recirculation=None
    ReturnAir=None
    ReturnHydronic=None
    Sanitary=None
    Security=None
    Storm=None
    SupplyAir=None
    SupplyHydronic=None
    SwitchTopology=None
    Telephone=None
    UndefinedSystemClassification=None
    value__=None
    Vent=None
class MEPSystemType(ElementType):
    def Dispose(self):
        pass
    Abbreviation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CalculationLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LinePatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineWeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SystemClassification=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Mesh(GeometryObject):
    def Dispose(self):
        pass
    MaterialElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumTriangles=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Vertices=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MeshFromGeometryOperationIssue(Enum):
    AllFine=None
    CurveLoopsWithoutCurvesInInput=None
    EmptyCurveLoopsInInput=None
    InputCurveLoopProblemWithFallback=None
    InputCurveLoopWrongOpenFlag=None
    InternalError=None
    InternalMissingError=None
    InternalUtilityError=None
    MissingCurveLoopsInInput=None
    MissingCurvesInInputLoop=None
    NonContinuousInputCurveLoop=None
    NonPlanarProfileLoop=None
    NotSetYet=None
    NoUsableCurveLoopsInInput=None
    NumberOfIssueTypes=None
    value__=None
class MeshFromGeometryOperationResult(object):
    def Dispose(self):
        pass
    def GetIssues(self):
        pass
    def GetMesh(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    HasInvalidData=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsMeshAvailable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Tessellated=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MeshTriangle(object):
class ModelCurve(CurveElement):
    def ChangeToReferenceLine(self):
        pass
    def Dispose(self):
        pass
    def GetVisibility(self):
        pass
    def SetVisibility(self,visibility):
        pass
    IsReferenceLine=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Subcategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TrussCurveType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ModelArc(ModelCurve):
    def Dispose(self):
        pass
class ModelCurveArrArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ModelCurveArrArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ModelCurveArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ModelCurveArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ModelEllipse(ModelCurve):
    def Dispose(self):
        pass
class ModelHermiteSpline(ModelCurve):
    def Dispose(self):
        pass
class ModelLine(ModelCurve):
    def Dispose(self):
        pass
class ModelNurbSpline(ModelCurve):
    def Dispose(self):
        pass
class ModelPathUtils(object):
    @staticmethod
    def ConvertModelPathToUserVisiblePath(path):
        pass
    @staticmethod
    def ConvertUserVisiblePathToModelPath(strPath):
        pass
    @staticmethod
    def IsValidUserVisibleFullServerPath(strPath):
        pass
    __all__=[
        'ConvertModelPathToUserVisiblePath',
        'ConvertUserVisiblePathToModelPath',
        'IsValidUserVisibleFullServerPath',
    ]
class ModelText(Element):
    def Dispose(self):
        pass
    def GetVisibility(self):
        pass
    def SetVisibility(self,visibility):
        pass
    Depth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ModelTextType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Subcategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Text=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ModelTextType(ElementType):
    def Dispose(self):
        pass
class ModelUpdatesStatus(Enum):
    CurrentWithCentral=None
    DeletedInCentral=None
    NotYetInCentral=None
    UpdatedInCentral=None
    value__=None
class ModifierType(Enum):
    AnalyzesAs=None
    Category=None
    Custom1=None
    Custom2=None
    Custom3=None
    DomainType=None
    FabricationService=None
    FireRating=None
    Function=None
    Level=None
    PhaseCreated=None
    PhaseDemolished=None
    PhaseStatus=None
    StructuralMaterialType=None
    StructuralUsage=None
    SystemClassification=None
    SystemName=None
    SystemType=None
    Underlay=None
    UnknownType=None
    value__=None
    ViewType=None
    Workset=None
class Mullion(FamilyInstance):
    def BreakMullion(self):
        pass
    def Dispose(self):
        pass
    def JoinMullion(self):
        pass
    LocationCurve=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Lock=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Lockable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MullionType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MullionType(FamilySymbol):
    def Dispose(self):
        pass
class MullionTypeSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MullionTypeSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MultiReferenceAnnotation(Element):
    @staticmethod
    def AreReferencesValidForLinearDimension(document,ownerViewId,options):
        pass
    @staticmethod
    def AreReferencesValidForLinearFixedDimension(document,ownerViewId,options):
        pass
    @staticmethod
    def Create(document,ownerViewId,options):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def IsLinearFixedDimensionDirectionValid(document,viewId,options):
        pass
    DimensionId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MultiReferenceAnnotationOptions(object):
    def Dispose(self):
        pass
    def ElementsMatchReferenceCategory(self,elements):
        pass
    def GetElementsToDimension(self):
        pass
    def IsAllowedDimensionStyleType(self,dimensionStyleType):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetElementsToDimension(self,elementsToDimension):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,multiReferenceAnnotationType):
        pass
    DimensionLineDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DimensionLineOrigin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DimensionPlaneNormal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DimensionStyleType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MultiReferenceAnnotationType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagHasLeader=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagHeadPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MultiReferenceAnnotationType(ElementType):
    @staticmethod
    def CreateDefault(document):
        pass
    def Dispose(self):
        pass
    def GetAllowedTagCategory(self):
        pass
    def IsAllowedDimensionStyle(self,dimensionStyleId):
        pass
    def IsAllowedReferenceCategory(self,referenceCategoryId):
        pass
    @staticmethod
    def IsAllowedTagCategory(tagCategoryId):
        pass
    def IsAllowedTagType(self,tagTypeId):
        pass
    DimensionStyleId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GroupTagHeads=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReferenceCategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowDimensionText=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TagTypeId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class MultiSegmentGrid(Element):
    @staticmethod
    def AreGridsInSameMultiSegmentGrid(grid1,grid2):
        pass
    @staticmethod
    def Create(document,typeId,curveLoop,sketchPlaneId):
        pass
    def Dispose(self):
        pass
    def GetGridIds(self):
        pass
    @staticmethod
    def GetMultiSegementGridId(grid):
        pass
    @staticmethod
    def IsValidCurveLoop(curveLoop):
        pass
    @staticmethod
    def IsValidSketchPlaneId(document,elemId):
        pass
    Text=property(lambda self:object(),lambda self,v:None,lambda self:None)
class NamingUtils(object):
    @staticmethod
    def CompareNames(nameA,nameB):
        pass
    @staticmethod
    def IsValidName(string):
        pass
    __all__=[
        'CompareNames',
        'IsValidName',
    ]
class NavisworksCoordinates(Enum):
    Internal=None
    Shared=None
    value__=None
class NavisworksExportOptions(object):
    def Dispose(self):
        pass
    def GetSelectedElementIds(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetSelectedElementIds(self,ids):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ConvertElementProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Coordinates=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DivideFileIntoLevels=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportElementIds=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportLinks=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportParts=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportRoomAsAttribute=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportRoomGeometry=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportScope=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ExportUrls=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FindMissingMaterials=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Parameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class NavisworksExportScope(Enum):
    Model=None
    SelectedElements=None
    value__=None
    View=None
class NavisworksParameters(Enum):
    All=None
    Elements=None
    None_JEDIFIX=None
    value__=None
class NestedFamilyTypeReference(Element):
    def Dispose(self):
        pass
    CategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TypeName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class NullParameterValue(ParameterValue):
    def Dispose(self):
        pass
class NumberingSchema(Element):
    def AppendSequence(self,fromPartition,toPartition):
        pass
    def AssignElementsToSequence(self,elementIds,partitionName):
        pass
    def ChangeNumber(self,partition,fromNumber,toNumber):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetMinimumNumberOfDigits(document):
        pass
    @staticmethod
    def GetNumberingSchema(document,schemaType):
        pass
    def GetNumberingSequences(self):
        pass
    def GetNumbers(self,partition):
        pass
    @staticmethod
    def GetSchemasInDocument(document):
        pass
    @staticmethod
    def IsValidPartitionName(name,message):
        pass
    def MergeSequences(self,sourcePartitions,newPartition):
        pass
    def MoveSequence(self,fromPartition,newPartition):
        pass
    def RemoveGaps(self,partition):
        pass
    @staticmethod
    def SetMinimumNumberOfDigits(document,value):
        pass
    def ShiftNumbers(self,partition,firstNumber):
        pass
    NumberingParameterId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SchemaType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaximumStartingNumber=1073741822
class NumberingSchemaType(GuidEnum):
    @staticmethod # known case of __new__
    def __new__(self,guid):
        pass
class NumberingSchemaTypes(object):
    StructuralNumberingSchemas=None
    __all__=[
        'StructuralNumberingSchemas',
    ]
class NumberSystem(Element):
    def Dispose(self):
        pass
    def GetReferencePick(self):
        pass
    def SetReferencePick(self,referencePick):
        pass
    JustifyOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    JustifyOption=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberDisplayRule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberedElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReferenceOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
class NumberSystemDisplayRule(Enum):
    All=None
    Even=None
    Odd=None
    StartAndEnd=None
    value__=None
class NumberSystemJustifyOption(Enum):
    Back=None
    Center=None
    Front=None
    value__=None
class NumericRevisionSettings(object):
    def Dispose(self):
        pass
    def IsEqual(self,other):
        pass
    def IsValid(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Prefix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Suffix=property(lambda self:object(),lambda self,v:None,lambda self:None)
class NurbSpline(Curve):
    @staticmethod
    def Create(*__args):
        pass
    @staticmethod
    def CreateCurve(*__args):
        pass
    def Dispose(self):
        pass
    def SetControlPointsAndWeights(self,ctrlPoints,weights):
        pass
    CtrlPoints=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Degree=property(lambda self:object(),lambda self,v:None,lambda self:None)
    isClosed=property(lambda self:object(),lambda self,v:None,lambda self:None)
    isRational=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Knots=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Weights=property(lambda self:object(),lambda self,v:None,lambda self:None)
class NurbsSurfaceData(object):
    @staticmethod
    def Create(degreeU,degreeV,knotsU,knotsV,controlPoints,weights,bReverseOrientation):
        pass
    def Dispose(self):
        pass
    def GetControlPoints(self):
        pass
    def GetKnotsU(self):
        pass
    def GetKnotsV(self):
        pass
    def GetWeights(self):
        pass
    def IsValid(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other):
        pass
    DegreeU=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DegreeV=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsRational=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReverseOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Opening(Element):
    def Dispose(self):
        pass
    BoundaryCurves=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BoundaryRect=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Host=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsRectBoundary=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTransparentIn3D=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTransparentInElevation=property(lambda self:object(),lambda self,v:None,lambda self:None)
class OpeningWrappingCondition(Enum):
    Exterior=None
    ExteriorAndInterior=None
    Interior=None
    None_JEDIFIX=None
    value__=None
class OpenOptions(object):
    def Dispose(self):
        pass
    def GetOpenWorksetsConfiguration(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetOpenWorksetsConfiguration(self,openConfiguration):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AllowOpeningLocalByWrongUser=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Audit=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DetachFromCentralOption=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class OptionalFunctionalityUtils(object):
    @staticmethod
    def IsDGNExportAvailable():
        pass
    @staticmethod
    def IsDGNImportLinkAvailable():
        pass
    @staticmethod
    def IsDWFExportAvailable():
        pass
    @staticmethod
    def IsDWGExportAvailable():
        pass
    @staticmethod
    def IsDWGImportLinkAvailable():
        pass
    @staticmethod
    def IsDXFExportAvailable():
        pass
    @staticmethod
    def IsFBXExportAvailable():
        pass
    @staticmethod
    def IsGraphicsAvailable():
        pass
    @staticmethod
    def IsIFCAvailable():
        pass
    @staticmethod
    def IsNavisworksExporterAvailable():
        pass
    @staticmethod
    def IsSATImportLinkAvailable():
        pass
    @staticmethod
    def IsShapeImporterAvailable():
        pass
    @staticmethod
    def IsSKPImportLinkAvailable():
        pass
    __all__=[
        'IsDGNExportAvailable',
        'IsDGNImportLinkAvailable',
        'IsDWFExportAvailable',
        'IsDWGExportAvailable',
        'IsDWGImportLinkAvailable',
        'IsDXFExportAvailable',
        'IsFBXExportAvailable',
        'IsGraphicsAvailable',
        'IsIFCAvailable',
        'IsNavisworksExporterAvailable',
        'IsSATImportLinkAvailable',
        'IsShapeImporterAvailable',
        'IsSKPImportLinkAvailable',
    ]
class Options(APIObject):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,pOptions=None):
        pass
    ComputeReferences=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DetailLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IncludeNonVisibleObjects=property(lambda self:object(),lambda self,v:None,lambda self:None)
    View=property(lambda self:object(),lambda self,v:None,lambda self:None)
class OrdinateDimensionLineStyle(Enum):
    Continuous=None
    None_JEDIFIX=None
    Segmented=None
    value__=None
class OrdinateDimensionSetting(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    DimensionLineLength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DimensionLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OriginTickMarkId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OriginVisibility=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
class OrdinateOriginVisibility(Enum):
    None_JEDIFIX=None
    value__=None
    WitnessLineOnly=None
    WitnessLineWithText=None
class OrdinateTextOrientation(Enum):
    ParallelToDimensionLine=None
    ParallelToWitnessLine=None
    value__=None
class OrdinateTextPosition(Enum):
    EndOfWitnessLine=None
    NextToWitnessLine=None
    value__=None
class Outline(object):
    def AddPoint(self,point):
        pass
    def Contains(self,point,tolerance):
        pass
    def ContainsOtherOutline(self,otherOutline,tolerance):
        pass
    def Dispose(self):
        pass
    def GetDiagonalLength(self):
        pass
    def Intersects(self,outline,tolerance):
        pass
    def IsScaleValid(self,scale):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def Scale(self,scale):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaximumPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinimumPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
class OverrideGraphicSettings(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetCutFillColor(self,color):
        pass
    def SetCutFillPatternId(self,fillPatternId):
        pass
    def SetCutFillPatternVisible(self,cutFillPatternVisible):
        pass
    def SetCutLineColor(self,color):
        pass
    def SetCutLinePatternId(self,linePatternId):
        pass
    def SetCutLineWeight(self,lineWeight):
        pass
    def SetDetailLevel(self,detailLevel):
        pass
    def SetHalftone(self,halftone):
        pass
    def SetProjectionFillColor(self,color):
        pass
    def SetProjectionFillPatternId(self,fillPatternId):
        pass
    def SetProjectionFillPatternVisible(self,projectFillPatternVisible):
        pass
    def SetProjectionLineColor(self,color):
        pass
    def SetProjectionLinePatternId(self,linePatternId):
        pass
    def SetProjectionLineWeight(self,lineWeight):
        pass
    def SetSurfaceTransparency(self,transparency):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,overrideGraphicSettings=None):
        pass
    CutFillColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutFillPatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutLineColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutLinePatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CutLineWeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DetailLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Halftone=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCutFillPatternVisible=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsProjectionFillPatternVisible=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectionFillColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectionFillPatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectionLineColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectionLinePatternId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectionLineWeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transparency=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InvalidPenNumber=-1
class OverridePermissions(Enum):
    CutFills=None
    CutLines=None
    Halftone=None
    ProjectionFills=None
    ProjectionLines=None
    Surfaces=None
    value__=None
    ViewDetailLevel=None
class PageOrientationType(Enum):
    Landscape=None
    Portrait=None
    value__=None
class Panel(FamilyInstance):
    def Dispose(self):
        pass
    def FindHostPanel(self):
        pass
    def GetRefGridLines(self,uGridLineId,vGridLineId):
        pass
    Lockable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PanelType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transform=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PanelType(FamilySymbol):
    def Dispose(self):
        pass
class PanelTypeSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PanelTypeSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PaperPlacementType(Enum):
    Center=None
    Margins=None
    value__=None
class PaperSize(APIObject):
    def Dispose(self):
        pass
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PaperSizeSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PaperSizeSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PaperSource(APIObject):
    def Dispose(self):
        pass
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PaperSourceSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PaperSourceSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Parameter(APIObject):
    def AsDouble(self):
        pass
    def AsElementId(self):
        pass
    def AsInteger(self):
        pass
    def AssociateWithGlobalParameter(self,gpId):
        pass
    def AsString(self):
        pass
    def AsValueString(self,formatOptions=None):
        pass
    def CanBeAssociatedWithGlobalParameter(self,gpId):
        pass
    def CanBeAssociatedWithGlobalParameters(self):
        pass
    def Dispose(self):
        pass
    def DissociateFromGlobalParameter(self):
        pass
    def GetAssociatedGlobalParameter(self):
        pass
    def Set(self,value):
        pass
    def SetValueString(self,valueString):
        pass
    Definition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayUnitType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Element=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GUID=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsReadOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsShared=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StorageType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UserModifiable=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ParameterFilterElement(FilterElement):
    @staticmethod
    def AllRuleParametersApplicable(*__args):
        pass
    def ClearRules(self):
        pass
    @staticmethod
    def Create(aDocument,name,categories,rules=None):
        pass
    def Dispose(self):
        pass
    def GetCategories(self):
        pass
    @staticmethod
    def GetRuleParameter(rule):
        pass
    def GetRuleParameters(self):
        pass
    def GetRules(self):
        pass
    def SetCategories(self,categories):
        pass
    def SetRules(self,rules):
        pass
class ParameterFilterRuleFactory(object):
    @staticmethod
    def CreateBeginsWithRule(parameter,value,caseSensitive):
        pass
    @staticmethod
    def CreateContainsRule(parameter,value,caseSensitive):
        pass
    @staticmethod
    def CreateEndsWithRule(parameter,value,caseSensitive):
        pass
    @staticmethod
    def CreateEqualsRule(parameter,value,*__args):
        pass
    @staticmethod
    def CreateGreaterOrEqualRule(parameter,value,*__args):
        pass
    @staticmethod
    def CreateGreaterRule(parameter,value,*__args):
        pass
    @staticmethod
    def CreateIsAssociatedWithGlobalParameterRule(parameter,value):
        pass
    @staticmethod
    def CreateIsNotAssociatedWithGlobalParameterRule(parameter,value):
        pass
    @staticmethod
    def CreateLessOrEqualRule(parameter,value,*__args):
        pass
    @staticmethod
    def CreateLessRule(parameter,value,*__args):
        pass
    @staticmethod
    def CreateNotBeginsWithRule(parameter,value,caseSensitive):
        pass
    @staticmethod
    def CreateNotContainsRule(parameter,value,caseSensitive):
        pass
    @staticmethod
    def CreateNotEndsWithRule(parameter,value,caseSensitive):
        pass
    @staticmethod
    def CreateNotEqualsRule(parameter,value,*__args):
        pass
    @staticmethod
    def CreateSharedParameterApplicableRule(parameterName):
        pass
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ParameterFilterUtilities(object):
    @staticmethod
    def GetAllFilterableCategories():
        pass
    @staticmethod
    def GetFilterableParametersInCommon(aDoc,categories):
        pass
    @staticmethod
    def GetInapplicableParameters(aDoc,categories,parameters):
        pass
    @staticmethod
    def IsParameterApplicable(element,parameter):
        pass
    @staticmethod
    def RemoveUnfilterableCategories(categories):
        pass
    __all__=[
        'GetAllFilterableCategories',
        'GetFilterableParametersInCommon',
        'GetInapplicableParameters',
        'IsParameterApplicable',
        'RemoveUnfilterableCategories',
    ]
class ParameterMap(APIObject):
    def Clear(self):
        pass
    def Contains(self,key):
        pass
    def Dispose(self):
        pass
    def Erase(self,key):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,key,item):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ParameterMapIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Key=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ParameterSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ParameterSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ParametersOrder(Enum):
    Ascending=None
    Descending=None
    value__=None
class ParameterType(Enum):
    Acceleration=None
    Angle=None
    Area=None
    AreaForce=None
    AreaForcePerLength=None
    BarDiameter=None
    ColorTemperature=None
    CrackWidth=None
    Currency=None
    DisplacementDeflection=None
    ElectricalApparentPower=None
    ElectricalCableTraySize=None
    ElectricalConduitSize=None
    ElectricalCurrent=None
    ElectricalDemandFactor=None
    ElectricalEfficacy=None
    ElectricalFrequency=None
    ElectricalIlluminance=None
    ElectricalLuminance=None
    ElectricalLuminousFlux=None
    ElectricalLuminousIntensity=None
    ElectricalPotential=None
    ElectricalPower=None
    ElectricalPowerDensity=None
    ElectricalResistivity=None
    ElectricalTemperature=None
    ElectricalTemperatureDifference=None
    ElectricalWattage=None
    Energy=None
    FamilyType=None
    FixtureUnit=None
    Force=None
    ForceLengthPerAngle=None
    ForcePerLength=None
    HVACAirflow=None
    HVACAirflowDensity=None
    HVACAirflowDividedByCoolingLoad=None
    HVACAirflowDividedByVolume=None
    HVACAreaDividedByCoolingLoad=None
    HVACAreaDividedByHeatingLoad=None
    HVACCoefficientOfHeatTransfer=None
    HVACCoolingLoad=None
    HVACCoolingLoadDividedByArea=None
    HVACCoolingLoadDividedByVolume=None
    HVACCrossSection=None
    HVACDensity=None
    HVACDuctInsulationThickness=None
    HVACDuctLiningThickness=None
    HVACDuctSize=None
    HVACEnergy=None
    HVACFactor=None
    HVACFriction=None
    HVACHeatGain=None
    HVACHeatingLoad=None
    HVACHeatingLoadDividedByArea=None
    HVACHeatingLoadDividedByVolume=None
    HVACPermeability=None
    HVACPower=None
    HVACPowerDensity=None
    HVACPressure=None
    HVACRoughness=None
    HVACSlope=None
    HVACSpecificHeat=None
    HVACSpecificHeatOfVaporization=None
    HVACTemperature=None
    HVACTemperatureDifference=None
    HVACThermalConductivity=None
    HVACThermalMass=None
    HVACThermalResistance=None
    HVACVelocity=None
    HVACViscosity=None
    Image=None
    Integer=None
    Invalid=None
    Length=None
    LinearForce=None
    LinearForceLengthPerAngle=None
    LinearForcePerLength=None
    LinearMoment=None
    LoadClassification=None
    Mass=None
    MassDensity=None
    MassPerUnitArea=None
    MassPerUnitLength=None
    Material=None
    Moment=None
    MomentOfInertia=None
    MultilineText=None
    Number=None
    NumberOfPoles=None
    Period=None
    PipeDimension=None
    PipeInsulationThickness=None
    PipeMass=None
    PipeMassPerUnitLength=None
    PipeSize=None
    PipingDensity=None
    PipingFlow=None
    PipingFriction=None
    PipingPressure=None
    PipingRoughness=None
    PipingSlope=None
    PipingTemperature=None
    PipingTemperatureDifference=None
    PipingVelocity=None
    PipingViscosity=None
    PipingVolume=None
    Pulsation=None
    ReinforcementArea=None
    ReinforcementAreaPerUnitLength=None
    ReinforcementCover=None
    ReinforcementLength=None
    ReinforcementSpacing=None
    ReinforcementVolume=None
    Rotation=None
    SectionArea=None
    SectionDimension=None
    SectionModulus=None
    SectionProperty=None
    Slope=None
    Stress=None
    StructuralFrequency=None
    StructuralVelocity=None
    SurfaceArea=None
    Text=None
    ThermalExpansion=None
    UnitWeight=None
    URL=None
    value__=None
    Volume=None
    WarpingConstant=None
    Weight=None
    WeightPerUnitLength=None
    WireSize=None
    YesNo=None
class ParameterValueProvider(FilterableValueProvider):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,parameter):
        pass
    Parameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Part(Element):
    def CanOffsetFace(self,face):
        pass
    def Dispose(self):
        pass
    def GetSourceElementIds(self):
        pass
    def GetSourceElementOriginalCategoryIds(self):
        pass
    def ResetPartShape(self):
        pass
    def SetFaceOffset(self,face,offset):
        pass
    Excluded=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OriginalCategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PartMaker=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PartEdgeConditionOrientation(Enum):
    Complement=None
    Mirrored=None
    MirroredAndRotated=None
    value__=None
class PartMaker(Element):
    def Dispose(self):
        pass
    def GetSourceElementIds(self):
        pass
    def IsSourceElement(self,elemId):
        pass
    def SetSourceElementIds(self,sourceElementIds):
        pass
class PartMakerMethodToDivideVolumes(object):
    def AddIntersectingReference(self,intersectingReference,offset):
        pass
    @staticmethod
    def AreElementsValidIntersectingReferences(*__args):
        pass
    def CanBeDivisionProfile(self,familyId,familyDocument=None):
        pass
    def Dispose(self):
        pass
    def GetOffsetForIntersectingReference(self,intersectingReference):
        pass
    def GetPlaneOfSketch(self):
        pass
    def GetSketchCurves(self,curveArray):
        pass
    def GetSplitRefsOffsets(self):
        pass
    @staticmethod
    def IsElementValidIntersectingReference(*__args):
        pass
    @staticmethod
    def IsValidSketchPlane(document,sketchPlaneId):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveIntersectingReference(self,intersectingReference):
        pass
    def SetOffsetForIntersectingReference(self,intersectingReference,offset):
        pass
    def UsesReference(self,intersectingReference):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    DivisionGap=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DivisionPatternMirror=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DivisionRotationAngle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DivisionRuleId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileFlipAcross=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileFlipAlong=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileMatch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UConstDivisionIndent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VConstDivisionIndent=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PartsVisibility(Enum):
    ShowOriginalOnly=None
    ShowPartsAndOriginal=None
    ShowPartsOnly=None
    Unset=None
    value__=None
class PartType(Enum):
    AttachesTo=None
    BreaksInto=None
    Cap=None
    ChannelCableTrayCross=None
    ChannelCableTrayElbow=None
    ChannelCableTrayMultiPort=None
    ChannelCableTrayOffset=None
    ChannelCableTrayTee=None
    ChannelCableTrayTransition=None
    ChannelCableTrayUnion=None
    ChannelCableTrayVerticalElbow=None
    Cross=None
    Damper=None
    DuctMounted=None
    Elbow=None
    EndCap=None
    EquipmentSwitch=None
    HandrailBracketHardware=None
    Handrails=None
    InlineSensor=None
    JunctionBox=None
    JunctionBoxCross=None
    JunctionBoxElbow=None
    JunctionBoxTee=None
    LadderCableTrayCross=None
    LadderCableTrayElbow=None
    LadderCableTrayMultiPort=None
    LadderCableTrayOffset=None
    LadderCableTrayTee=None
    LadderCableTrayTransition=None
    LadderCableTrayUnion=None
    LadderCableTrayVerticalElbow=None
    LateralCross=None
    LateralTee=None
    MultiPort=None
    Normal=None
    Offset=None
    OtherPanel=None
    PanelBoard=None
    PanelBracketHardware=None
    Pants=None
    PipeFlange=None
    PipeMechanicalCoupling=None
    Rails=None
    Sensor=None
    SpudAdjustable=None
    SpudPerpendicular=None
    Switch=None
    SwitchBoard=None
    TapAdjustable=None
    TapPerpendicular=None
    Tee=None
    TerminationHardware=None
    TopRails=None
    Transformer=None
    Transition=None
    Undefined=None
    Union=None
    value__=None
    ValveBreaksInto=None
    ValveNormal=None
    Wye=None
class PartUtils(object):
    @staticmethod
    def AreElementsValidForCreateParts(document,elementIds):
        pass
    @staticmethod
    def ArePartsValidForDivide(document,elementIdsToDivide):
        pass
    @staticmethod
    def ArePartsValidForMerge(document,partIds):
        pass
    @staticmethod
    def CreateMergedPart(document,partIds):
        pass
    @staticmethod
    def CreateParts(document,*__args):
        pass
    @staticmethod
    def DivideParts(document,elementIdsToDivide,intersectingReferenceIds,curveArray,sketchPlaneId):
        pass
    @staticmethod
    def FindMergeableClusters(doc,partIds):
        pass
    @staticmethod
    def GetAssociatedPartMaker(hostDocument,*__args):
        pass
    @staticmethod
    def GetAssociatedParts(hostDocument,*__args):
        pass
    @staticmethod
    def GetChainLengthToOriginal(part):
        pass
    @staticmethod
    def GetMergedParts(part):
        pass
    @staticmethod
    def GetPartMakerMethodToDivideVolumeFW(partMaker):
        pass
    @staticmethod
    def HasAssociatedParts(hostDocument,*__args):
        pass
    @staticmethod
    def IsMergedPart(part):
        pass
    @staticmethod
    def IsPartDerivedFromLink(dPart):
        pass
    @staticmethod
    def IsValidForCreateParts(document,hostOrLinkElementId):
        pass
    __all__=[
        'AreElementsValidForCreateParts',
        'ArePartsValidForDivide',
        'ArePartsValidForMerge',
        'CreateMergedPart',
        'CreateParts',
        'DivideParts',
        'FindMergeableClusters',
        'GetAssociatedPartMaker',
        'GetAssociatedParts',
        'GetChainLengthToOriginal',
        'GetMergedParts',
        'GetPartMakerMethodToDivideVolumeFW',
        'HasAssociatedParts',
        'IsMergedPart',
        'IsPartDerivedFromLink',
        'IsValidForCreateParts',
    ]
class SketchBase(Element):
    def Dispose(self):
        pass
class Path3d(SketchBase):
    def Dispose(self):
        pass
    AllCurveLoops=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumCurveLoops=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PathType(Enum):
    Absolute=None
    Content=None
    Relative=None
    Server=None
    value__=None
class PerformanceAdviser(object):
    def AddRule(self,id,rule):
        pass
    def DeleteRule(self,id):
        pass
    def Dispose(self):
        pass
    def ExecuteAllRules(self,document):
        pass
    def ExecuteRules(self,document,rules):
        pass
    def GetAllRuleIds(self):
        pass
    def GetElementFilterFromRule(self,*__args):
        pass
    def GetNumberOfRules(self):
        pass
    @staticmethod
    def GetPerformanceAdviser():
        pass
    def GetRuleDescription(self,*__args):
        pass
    def GetRuleId(self,index):
        pass
    def GetRuleName(self,*__args):
        pass
    def IsRuleEnabled(self,*__args):
        pass
    def PostWarning(self,message):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetRuleEnabled(self,*__args):
        pass
    def WillRuleCheckElements(self,*__args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PerformanceAdviserRuleId(GuidEnum):
    @staticmethod # known case of __new__
    def __new__(self,guid):
        pass
class PerformanceAdviserRules(object):
    __all__=[]
class Phase(Element):
    def Dispose(self):
        pass
class PhaseArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PhaseArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PhaseFilter(Element):
    @staticmethod
    def Create(document,name):
        pass
    def Dispose(self):
        pass
    def GetPhaseStatusPresentation(self,status):
        pass
    def SetPhaseStatusPresentation(self,status,presentation):
        pass
    IsDefault=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PhaseStatusPresentation(Enum):
    DontShow=None
    ShowByCategory=None
    ShowOverriden=None
    value__=None
class PlanarFace(Face):
    def Dispose(self):
        pass
    FaceNormal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XVector=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YVector=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PlanCircuit(APIObject):
    def Dispose(self):
        pass
    def GetPointInside(self):
        pass
    Area=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsRoomLocated=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SideNum=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PlanCircuitSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PlanCircuitSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Plane(Surface):
    @staticmethod
    def Create(frameOfReference):
        pass
    @staticmethod
    def CreateByNormalAndOrigin(normal,origin):
        pass
    @staticmethod
    def CreateByOriginAndBasis(origin,basisX,basisY):
        pass
    @staticmethod
    def CreateByThreePoints(point1,point2,point3):
        pass
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    Normal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XVec=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YVec=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PlanTopology(APIObject):
    def Dispose(self):
        pass
    def GetRoomIds(self):
        pass
    Circuits=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Level=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Phase=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PlanTopologySet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PlanTopologySetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PlanViewDirection(Enum):
    Down=None
    Undefined=None
    Up=None
    value__=None
class PlanViewPlane(Enum):
    BottomClipPlane=None
    CutPlane=None
    TopClipPlane=None
    UnderlayBottom=None
    value__=None
    ViewDepthPlane=None
class PlanViewRange(object):
    def Dispose(self):
        pass
    def GetLevelId(self,planViewPlane):
        pass
    def GetOffset(self,planViewPlane):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetLevelId(self,planViewPlane,id):
        pass
    def SetOffset(self,planViewPlane,offset):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Current=None
    LevelAbove=None
    LevelBelow=None
    Unlimited=None
class PlanViewRangeError(Enum):
    BottomClipAboveCutPlane=None
    TopClipBelowCutPlane=None
    value__=None
    ViewDepthAboveBottomClip=None
    ViewDepthBelowTopClip=None
class PlanViewRangeLevel(Enum):
    Above=None
    Below=None
    Current=None
    Unlimited=None
    Unused=None
    value__=None
class Point(GeometryObject):
    @staticmethod
    def Create(coord,id=None):
        pass
    def Dispose(self):
        pass
    Coord=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Reference=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PointCloudColorMode(Enum):
    Elevation=None
    FixedColor=None
    Intensity=None
    NoOverride=None
    Normals=None
    value__=None
class PointCloudFoundStatus(Enum):
    FoundOK=None
    NotFound=None
    Unknown=None
    value__=None
class PointCloudInstance(Instance):
    def ContainsScan(self,scanName):
        pass
    @staticmethod
    def Create(document,typeId,transform):
        pass
    def Dispose(self):
        pass
    def GetPoints(self,filter,averageDistance,numPoints):
        pass
    def GetRegions(self):
        pass
    def GetScanOrigin(self,scanName):
        pass
    def GetScans(self):
        pass
    def GetSelectionFilter(self):
        pass
    def HasColor(self):
        pass
    def SetSelectionFilter(self,pFilter):
        pass
    FilterAction=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SupportsOverrides=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PointCloudType(ElementType):
    @staticmethod
    def Create(document,engineIdentifier,typeIdentifier):
        pass
    def Dispose(self):
        pass
    def GetPath(self):
        pass
    ColorEncoding=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EngineIdentifier=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FoundStatus=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Offset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Scale=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PointElementReference(object):
class PointLocationOnCurve(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,measType,measValue,measFrom):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MeasureFrom=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MeasurementType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MeasurementValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PointNode(ModelCurveNode):
    def Dispose(self):
        pass
    def GetPoint(self):
        pass
class PointOnCurveMeasureFrom(Enum):
    Beginning=None
    End=None
    value__=None
class PointOnCurveMeasurementType(Enum):
    Angle=None
    ChordLength=None
    NonNormalizedCurveParameter=None
    NormalizedCurveParameter=None
    NormalizedSegmentLength=None
    SegmentLength=None
    value__=None
class PointOnEdge(PointElementReference):
    def GetEdgeReference(self):
        pass
    def SetEdgeReference(self,reference):
        pass
    LocationOnCurve=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PointOnEdgeEdgeIntersection(PointElementReference):
    def GetEdgeReference1(self):
        pass
    def GetEdgeReference2(self):
        pass
    def SetEdgeReference1(self,edgeReference):
        pass
    def SetEdgeReference2(self,edgeReference):
        pass
class PointOnEdgeFaceIntersection(PointElementReference):
    def GetEdgeReference(self):
        pass
    def GetFaceReference(self):
        pass
    def SetEdgeReference(self,edgeReference):
        pass
    def SetFaceReference(self,reference):
        pass
    OrientWithEdge=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PointOnFace(PointElementReference):
    def GetFaceReference(self):
        pass
    def SetFaceReference(self,reference):
        pass
    UV=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PointOnPlane(PointElementReference):
    def GetPlaneReference(self):
        pass
    @staticmethod
    def IsValidPlaneReference(doc,planeReference):
        pass
    @staticmethod
    def NewPointOnPlane(doc,planeReference,position,xvec):
        pass
    def SetPlaneReference(self,planeReference):
        pass
    Offset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Position=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XVec=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PointRelativeToPoint(PointElementReference):
    def GetHostPointReference(self):
        pass
    def SetHostPointReference(self,hostPointReference):
        pass
class PolyLine(GeometryObject):
    def Clone(self):
        pass
    @staticmethod
    def Create(coordinates):
        pass
    def Dispose(self):
        pass
    def Evaluate(self,param):
        pass
    def GetCoordinate(self,index):
        pass
    def GetCoordinates(self):
        pass
    def GetOutline(self):
        pass
    def GetTransformed(self,transform):
        pass
    NumberOfCoordinates=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PolylineNode(ModelCurveNode):
    def Dispose(self):
        pass
    def GetPolyline(self):
        pass
class PolylineSegments(object):
    def Dispose(self):
        pass
    def GetVertices(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EndLocalParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EndParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsFilled=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartLocalParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartParameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PolymeshFacet(object):
    def GetVertices(self):
        pass
    def ToString(self):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    V1=property(lambda self:object(),lambda self,v:None,lambda self:None)
    V2=property(lambda self:object(),lambda self,v:None,lambda self:None)
    V3=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PolymeshTopology(object):
    def Dispose(self):
        pass
    def GetFacet(self,idx):
        pass
    def GetFacets(self):
        pass
    def GetNormal(self,idx):
        pass
    def GetNormals(self):
        pass
    def GetPoint(self,idx):
        pass
    def GetPoints(self):
        pass
    def GetUV(self,idx):
        pass
    def GetUVs(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    DistributionOfNormals=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfFacets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfNormals=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfPoints=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfUVs=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PreferredJunctionType(Enum):
    Tap=None
    Tee=None
    value__=None
class PreviewFamilyVisibilityMode(Enum):
    Off=None
    On=None
    Uncut=None
    value__=None
class PrimaryDesignOptionMemberFilter(ElementSlowFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,inverted=None):
        pass
class RoutingCriterionBase(object):
    def Dispose(self):
        pass
    def IsEqual(self,pOther):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PrimarySizeCriterion(RoutingCriterionBase):
    @staticmethod
    def All():
        pass
    def Dispose(self):
        pass
    @staticmethod
    def None_JEDIFIX():
        pass
    @staticmethod # known case of __new__
    def __new__(self,minimumSize,maximumSize):
        pass
    MaximumSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinimumSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PrinterResolution(Enum):
    High=None
    Low=None
    Medium=None
    value__=None
    VeryHigh=None
class PrintManager(APIObject):
    def Apply(self):
        pass
    def Dispose(self):
        pass
    def SelectNewPrintDriver(self,strPrinterName):
        pass
    def SubmitPrint(self,view=None):
        pass
    Collate=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CombinedFile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CopyNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsVirtual=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PaperSizes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PaperSources=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrinterName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrintOrderReverse=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrintRange=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrintSetup=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrintToFile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrintToFileName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewSheetSetting=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PrintParameters(APIObject):
    def Dispose(self):
        pass
    ColorDepth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HiddenLineViews=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HideCropBoundaries=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HideReforWorkPlanes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HideScopeBoxes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HideUnreferencedViewTags=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MarginType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaskCoincidentLines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PageOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PaperPlacement=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PaperSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PaperSource=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RasterQuality=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReplaceHalftoneWithThinLines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UserDefinedMarginX=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UserDefinedMarginY=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewLinksinBlue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Zoom=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ZoomType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PrintRange(Enum):
    Current=None
    Select=None
    value__=None
    Visible=None
class PrintSetting(Element):
    def Dispose(self):
        pass
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrintParameters=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PrintSetup(APIObject):
    def Delete(self):
        pass
    def Dispose(self):
        pass
    def Rename(self,newName):
        pass
    def Revert(self):
        pass
    def Save(self):
        pass
    def SaveAs(self,newName):
        pass
    CurrentPrintSetting=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InSession=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Profile(GeometryObject):
    def Clone(self):
        pass
    def Dispose(self):
        pass
    Curves=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Filled=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ProfileFamilyUsage(Enum):
    Any=None
    ContinuousFooting=None
    Fascia=None
    Gutter=None
    Mullion=None
    Railing=None
    Reveal=None
    SlabEdge=None
    SlabMetalDeck=None
    StairNosing=None
    StairRiser=None
    StairSupport=None
    StairTread=None
    value__=None
    WallSweep=None
class ProfilePlaneLocation(Enum):
    End=None
    MidPoint=None
    Start=None
    value__=None
class ProjectInfo(Element):
    def Dispose(self):
        pass
    Address=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Author=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BuildingName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ClientName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IssueDate=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Number=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OrganizationDescription=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OrganizationName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Status=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ProjectLocation(Instance):
    def Dispose(self):
        pass
    def Duplicate(self,name):
        pass
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SiteLocation=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ProjectLocationSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ProjectLocationSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ProjectPosition(APIObject):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,ew,ns,elevation,angle):
        pass
    Angle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EastWest=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Elevation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NorthSouth=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PropertyLine(Element):
    def Dispose(self):
        pass
class PropertySetElement(Element):
    @staticmethod
    def Create(document,*__args):
        pass
    def Dispose(self):
        pass
    def Duplicate(self,document,name):
        pass
    def GetStructuralAsset(self):
        pass
    def GetThermalAsset(self):
        pass
    def SetStructuralAsset(self,structuralAsset):
        pass
    def SetThermalAsset(self,thermalAsset):
        pass
class PropertySetLibrary(Element):
    def AddPropertySet(self,propertySetId):
        pass
    def AddPropertySetWithName(self,propertySetId,name):
        pass
    def AddToDocument(self,name,document,overwrite):
        pass
    def AddToDocumentWithName(self,name,document,overwrite,addAsName):
        pass
    @staticmethod
    def Create(document):
        pass
    def Dispose(self):
        pass
    def ExportXml(self,fileName):
        pass
    @staticmethod
    def Find(doc,name):
        pass
    def GetName(self):
        pass
    def HasPropertySet(self,name):
        pass
    @staticmethod
    def ImportXml(document,fileName,overwriteExisting):
        pass
    def RemovePropertySet(self,name):
        pass
    def RenamePropertySet(self,name,newName):
        pass
    def RenameSubclass(self,oldSubclass,newSubclass):
        pass
    def SetName(self,name):
        pass
    Locked=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReadOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
class PropOverrideMode(Enum):
    ByEntity=None
    ByLayer=None
    NewLayer=None
    value__=None
class RadialArray(BaseArray):
    @staticmethod
    def ArrayElementsWithoutAssociation(aDoc,dBView,ids,count,axis,angle,anchorMember):
        pass
    @staticmethod
    def ArrayElementWithoutAssociation(aDoc,dBView,id,count,axis,angle,anchorMember):
        pass
    @staticmethod
    def Create(aDoc,dBView,*__args):
        pass
    def Dispose(self):
        pass
    def GetCopiedMemberIds(self):
        pass
    def GetOriginalMemberIds(self):
        pass
    @staticmethod
    def IsValidArraySize(count):
        pass
    NumMembers=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RasterQualityType(Enum):
    High=None
    Low=None
    Medium=None
    Presentation=None
    value__=None
class Rectangle(object):
    def Dispose(self):
        pass
    def IsNormalized(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    Bottom=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Left=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Right=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Top=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RectangularGridSegmentOrientation(Enum):
    Horizontal=None
    value__=None
    Vertical=None
class Reference(APIObject):
    def ConvertToStableRepresentation(self,document):
        pass
    def CreateLinkReference(self,revitLinkInstance):
        pass
    def CreateReferenceInLink(self):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def ParseFromStableRepresentation(document,representation):
        pass
    @staticmethod # known case of __new__
    def __new__(self,element):
        pass
    ElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ElementReferenceType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GlobalPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LinkedElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UVPoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferenceableViewUtils(object):
    @staticmethod
    def ChangeReferencedView(document,referenceId,desiredViewId):
        pass
    @staticmethod
    def GetReferencedViewId(document,referenceId):
        pass
    __all__=[
        'ChangeReferencedView',
        'GetReferencedViewId',
    ]
class ReferenceArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferenceArrayArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferenceArrayArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferenceArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferenceIntersector(object):
    def Dispose(self):
        pass
    def Find(self,origin,direction):
        pass
    def FindNearest(self,origin,direction):
        pass
    def GetFilter(self):
        pass
    def GetTargetElementIds(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetFilter(self,filter):
        pass
    def SetTargetElementIds(self,elementIds):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    FindReferencesInRevitLinks=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TargetType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferencePlane(DatumPlane):
    def Dispose(self):
        pass
    def Flip(self):
        pass
    def GetPlane(self):
        pass
    def GetReference(self):
        pass
    BubbleEnd=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Direction=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FreeEnd=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Normal=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferencePoint(Element):
    def Dispose(self):
        pass
    def GetCoordinatePlaneReferenceXY(self):
        pass
    def GetCoordinatePlaneReferenceXZ(self):
        pass
    def GetCoordinatePlaneReferenceYZ(self):
        pass
    def GetCoordinateSystem(self):
        pass
    def GetHubId(self):
        pass
    def GetInterpolatingCurves(self):
        pass
    def GetPointElementReference(self):
        pass
    def GetVisibility(self):
        pass
    def SetCoordinateSystem(self,coordinateSystem):
        pass
    def SetPointElementReference(self,pointElementReference):
        pass
    def SetVisibility(self,visibility):
        pass
    CoordinatePlaneVisibility=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Position=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowNormalReferencePlaneOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visible=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferencePointArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferencePointArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReferenceType(Enum):
    None_JEDIFIX=None
    StrongReference=None
    value__=None
    WeakReference=None
class ReferenceWithContext(object):
    def Dispose(self):
        pass
    def GetInstanceTransform(self):
        pass
    def GetReference(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Proximity=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RelinquishedItems(object):
    def Dispose(self):
        pass
    def GetRelinquishedElements(self):
        pass
    def GetRelinquishedWorksets(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RelinquishOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,relinquishEverything):
        pass
    CheckedOutElements=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyWorksets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StandardWorksets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UserWorksets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewWorksets=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ReloadLatestOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RenderDuration(Enum):
    ByLevel=None
    ByTime=None
    UntilSatisfactory=None
    value__=None
class RenderingImageExposureSettings(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ExposureValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Highlights=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Saturation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Shadows=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WhitePoint=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RenderingQuality(Enum):
    Custom=None
    Draft=None
    High=None
    Medium=None
    value__=None
    VeryHigh=None
class RenderingQualitySettings(object):
    def Dispose(self):
        pass
    def IsCustomQuality(self):
        pass
    def IsValidRenderLevel(self,value):
        pass
    def IsValidRenderTime(self,value):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LightAndMaterialAccuracyMode=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RenderDuration=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RenderingQuality=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RenderLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RenderTime=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RenderingSettings(object):
    def Dispose(self):
        pass
    def GetBackgroundSettings(self):
        pass
    def GetRenderingImageExposureSettings(self):
        pass
    def GetRenderingQualitySettings(self):
        pass
    def GetRenderingRegionOutline(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetBackgroundSettings(self,background):
        pass
    def SetRenderingImageExposureSettings(self,exposure):
        pass
    def SetRenderingQualitySettings(self,settings):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    BackgroundStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LightingSource=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PrinterResolution=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ResolutionTarget=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ResolutionValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UsesRegionRendering=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RenderNodeAction(Enum):
    Proceed=None
    Skip=None
    value__=None
class RepeaterBounds(object):
    def AdjustForCyclicalBounds(self,coordinates):
        pass
    def AreCoordinatesInBounds(self,coordinates,treatCyclicalBoundsAsInfinite):
        pass
    def Dispose(self):
        pass
    def GetLowerBound(self,dimension):
        pass
    def GetUpperBound(self,dimension):
        pass
    def IsCyclical(self,dimension):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    DimensionCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RepeaterCoordinates(object):
    def Dispose(self):
        pass
    def GetCoordinate(self,dimension):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,x=None,y=None):
        pass
    DimensionCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RepeatingReferenceSource(object):
    def Dispose(self):
        pass
    def GetBounds(self):
        pass
    @staticmethod
    def GetDefaultRepeatingReferenceSource(document,elementId):
        pass
    def GetReference(self,coordinates):
        pass
    @staticmethod
    def HasRepeatingReferenceSource(document,elementId):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    DimensionCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ResolutionTarget(Enum):
    Printer=None
    Screen=None
    value__=None
class ResourceVersionStatus(Enum):
    Current=None
    OutOfDate=None
    Unknown=None
    value__=None
class Revision(Element):
    @staticmethod
    def CombineWithNext(document,revisionId):
        pass
    @staticmethod
    def CombineWithPrevious(document,revisionId):
        pass
    @staticmethod
    def Create(document):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetAllRevisionIds(document):
        pass
    @staticmethod
    def ReorderRevisionSequence(document,newSequence):
        pass
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Issued=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IssuedBy=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IssuedTo=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RevisionDate=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RevisionNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SequenceNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visibility=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RevisionCloud(Element):
    @staticmethod
    def Create(document,view,revisionId,curves):
        pass
    def Dispose(self):
        pass
    def GetSheetIds(self):
        pass
    def GetSketchCurves(self):
        pass
    def IsRevisionIssued(self):
        pass
    RevisionId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RevisionNumbering(Enum):
    PerProject=None
    PerSheet=None
    value__=None
class RevisionNumberType(Enum):
    Alphanumeric=None
    None_JEDIFIX=None
    Numeric=None
    value__=None
class RevisionSettings(Element):
    def Dispose(self):
        pass
    def GetAlphanumericRevisionSettings(self):
        pass
    def GetNumericRevisionSettings(self):
        pass
    @staticmethod
    def GetRevisionSettings(ccda):
        pass
    def IsAcceptableRevisionCloudSpacing(self,rawValue):
        pass
    @staticmethod
    def RoundRevisionCloudSpacing(ccda,rawValue):
        pass
    def SetAlphanumericRevisionSettings(self,newSettings):
        pass
    def SetNumericRevisionSettings(self,newSettings):
        pass
    RevisionCloudSpacing=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RevisionNumbering=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RevisionVisibility(Enum):
    CloudAndTagVisible=None
    Hidden=None
    TagVisible=None
    value__=None
class RevitLinkInstance(Instance):
    @staticmethod
    def Create(document,revitLinkTypeId):
        pass
    def Dispose(self):
        pass
    def GetLinkDocument(self):
        pass
    def MoveBasePointToHostBasePoint(self,resetToOriginalRotation):
        pass
    def MoveOriginToHostOrigin(self,resetToOriginalRotation):
        pass
class RevitLinkLoadResult(object):
    def Dispose(self):
        pass
    def GetCentralModelName(self):
        pass
    def GetExternalResourceReference(self):
        pass
    def GetExternalResourceReferencesFromFailedLoads(self):
        pass
    def GetLinkLoadResult(self,matchExtResRef):
        pass
    def GetModelName(self):
        pass
    def GetNestedLinkLoadResults(self):
        pass
    def GetParentModelName(self):
        pass
    @staticmethod
    def IsCodeSuccess(code):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other):
        pass
    ElementId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCircularLink=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsNested=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LoadResult=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RevitLinkLoadResultType(Enum):
    ExternalServerMissing=None
    LinkExists=None
    LinkLoaded=None
    LinkMayBeUpgraded=None
    LinkNotFound=None
    LinkNotLoadedOtherError=None
    LinkNotOpenable=None
    LinkOpenAsHost=None
    SameCentralModelAsHost=None
    SameModelAsHost=None
    Uninitialized=None
    value__=None
class RevitLinkOperations(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetGetLocalPathForOpenCallback(self,makeLocalCopyForOpen):
        pass
    def SetOnLocalLinkSharedCoordinatesSavedCallback(self,onLocalLinkSharedCoordinatesSaved):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RevitLinkOptions(object):
    def Dispose(self):
        pass
    def GetWorksetConfiguration(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetWorksetConfiguration(self,config):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsRelative=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RevitLinkType(ElementType):
    @staticmethod
    def Create(document,*__args):
        pass
    @staticmethod
    def CreateFromIFC(document,ifcFilePath,revitLinkedFilePath,recreateLink,options):
        pass
    def Dispose(self):
        pass
    def GetChildIds(self):
        pass
    def GetConversionData(self):
        pass
    def GetParentId(self):
        pass
    def GetRootId(self):
        pass
    @staticmethod
    def GetTopLevelLink(document,*__args):
        pass
    def HasSaveablePositions(self):
        pass
    def IsFromLocalPath(self):
        pass
    def IsFromRevitServer(self):
        pass
    @staticmethod
    def IsLoaded(document,typeId):
        pass
    def IsNotLoadedIntoMultipleOpenDocuments(self):
        pass
    def Load(self):
        pass
    def LoadFrom(self,*__args):
        pass
    def Reload(self):
        pass
    def RevertLocalUnloadStatus(self):
        pass
    def SavePositions(self,callback):
        pass
    def Unload(self,callback):
        pass
    def UnloadLocally(self,callback):
        pass
    def UpdateFromIFC(self,document,ifcFilePath,revitLinkedFilePath,recreateLink):
        pass
    AttachmentType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsNestedLink=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LocallyUnloaded=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Revolution(GenericForm):
    def Dispose(self):
        pass
    Axis=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EndAngle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Sketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartAngle=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RevolvedFace(Face):
    def Dispose(self):
        pass
    Axis=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Curve=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RevolvedSurface(Surface):
    @staticmethod
    def Create(*__args):
        pass
    def Dispose(self):
        pass
    def GetProfileCurve(self):
        pass
    def GetProfileCurveInWorldCoordinates(self):
        pass
    @staticmethod
    def IsValidProfileCurve(*__args):
        pass
    Axis=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    XDir=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YDir=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RoofType(HostObjAttributes):
    def Dispose(self):
        pass
    ThermalProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RoundingMethod(Enum):
    Down=None
    Nearest=None
    Up=None
    value__=None
class RoutingCondition(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,diameter):
        pass
    Diameter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RoutingConditions(object):
    def AppendCondition(self,condition):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def GetConditionAt(self,index):
        pass
    def GetNumberOfConditions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,errorLevel):
        pass
    ErrorLevel=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreferredJunctionType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RoutingPreferenceErrorLevel(Enum):
    Error=None
    None_JEDIFIX=None
    value__=None
    Warning=None
class RoutingPreferenceManager(object):
    def AddRule(self,groupType,rule,index=None):
        pass
    def Dispose(self):
        pass
    def GetMEPPartId(self,groupType,conditions):
        pass
    def GetNumberOfRules(self,eGroupType):
        pass
    def GetRule(self,groupType,index):
        pass
    def GetSharedSizes(self,size,shape):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveRule(self,groupType,index):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OwnerId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreferredJunctionType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RoutingPreferenceRule(object):
    def AddCriterion(self,myCriterion):
        pass
    def Dispose(self):
        pass
    def GetCriterion(self,index):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveCriteron(self,index):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,MEPPartId,description):
        pass
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MEPPartId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfCriteria=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RoutingPreferenceManager=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RoutingPreferenceRuleGroupType(Enum):
    Caps=None
    Crosses=None
    Elbows=None
    Junctions=None
    MechanicalJoints=None
    Segments=None
    Transitions=None
    TransitionsOvalToRound=None
    TransitionsRectangularToOval=None
    TransitionsRectangularToRound=None
    Undefined=None
    Unions=None
    value__=None
class RPCNode(ContentNode):
    def Dispose(self):
        pass
class RuledFace(Face):
    def Dispose(self):
        pass
    IsExtruded=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RulingsAreParallel=property(lambda self:object(),lambda self,v:None,lambda self:None)
class RuledSurface(Surface):
    @staticmethod
    def Create(*__args):
        pass
    def Dispose(self):
        pass
    def GetFirstProfileCurve(self):
        pass
    def GetFirstProfilePoint(self):
        pass
    def GetSecondProfileCurve(self):
        pass
    def GetSecondProfilePoint(self):
        pass
class SATExportOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,option=None):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SATImportOptions(BaseImportOptions):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,option=None):
        pass
class SaveAsOptions(object):
    def Dispose(self):
        pass
    def GetWorksharingOptions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetWorksharingOptions(self,worksharingOptions):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Compact=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaximumBackups=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OverwriteExistingFile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreviewViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SaveModifiedLinksOptions(Enum):
    DisableSharedPositioning=None
    DoNotSaveLinks=None
    SaveLinks=None
    value__=None
class SaveModifiedLinksOptionsForUnloadLocally(Enum):
    DoNotSaveLinks=None
    SaveLinks=None
    value__=None
class SaveOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Compact=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreviewViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SchedulableField(object):
    def Dispose(self):
        pass
    def Equals(self,obj):
        pass
    def GetHashCode(self):
        pass
    def GetName(self,document):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __eq__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,fieldType=None,parameterId=None):
        pass
    def __ne__(self,*args):
        pass
    FieldType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ScheduleDefinition(object):
    def AddEmbeddedSchedule(self,categoryId):
        pass
    def AddField(self,*__args):
        pass
    def AddFilter(self,filter):
        pass
    def AddSortGroupField(self,sortGroupField):
        pass
    def CanFilter(self):
        pass
    def CanFilterByGlobalParameters(self,fieldId):
        pass
    def CanFilterByParameterExistence(self,fieldId):
        pass
    def CanFilterBySubstring(self,fieldId):
        pass
    def CanFilterByValue(self,fieldId):
        pass
    def CanHaveEmbeddedSchedule(self):
        pass
    def CanIncludeLinkedFiles(self):
        pass
    def CanSortByField(self,fieldId):
        pass
    def ClearFields(self):
        pass
    def ClearFilters(self):
        pass
    def ClearSortGroupFields(self):
        pass
    def Dispose(self):
        pass
    def GetField(self,*__args):
        pass
    def GetFieldCount(self):
        pass
    def GetFieldId(self,index):
        pass
    def GetFieldIndex(self,fieldId):
        pass
    def GetFieldOrder(self):
        pass
    def GetFilter(self,index):
        pass
    def GetFilterCount(self):
        pass
    def GetFilters(self):
        pass
    def GetSchedulableFields(self):
        pass
    def GetSortGroupField(self,index):
        pass
    def GetSortGroupFieldCount(self):
        pass
    def GetSortGroupFields(self):
        pass
    def GetValidCategoriesForEmbeddedSchedule(self):
        pass
    def InsertCombinedParameterField(self,data,fieldName,index):
        pass
    def InsertField(self,*__args):
        pass
    def InsertFilter(self,filter,index):
        pass
    def InsertSortGroupField(self,sortGroupField,index):
        pass
    def IsSchedulableField(self,schedulableField):
        pass
    def IsValidCategoryForEmbeddedSchedule(self,categoryId):
        pass
    def IsValidCombinedParameters(self,data):
        pass
    def IsValidFieldId(self,fieldId):
        pass
    def IsValidFieldIndex(self,index):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveEmbeddedSchedule(self):
        pass
    def RemoveField(self,*__args):
        pass
    def RemoveFilter(self,index):
        pass
    def RemoveSortGroupField(self,index):
        pass
    def SetFieldOrder(self,fieldIds):
        pass
    def SetFilter(self,index,filter):
        pass
    def SetFilters(self,filters):
        pass
    def SetSortGroupField(self,index,sortGroupField):
        pass
    def SetSortGroupFields(self,sortGroupFields):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AreaSchemeId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EmbeddedDefinition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FamilyId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GrandTotalTitle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasEmbeddedSchedule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IncludeLinkedFiles=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsEmbedded=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsItemized=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsKeySchedule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsMaterialTakeoff=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowGrandTotal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowGrandTotalCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowGrandTotalTitle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowHeaders=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowTitle=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ScheduleField(object):
    def CanDisplayMinMax(self):
        pass
    def CanTotal(self):
        pass
    def CanTotalByAssemblyType(self):
        pass
    def CreatesCircularReferences(self,fieldId):
        pass
    def Dispose(self):
        pass
    def GetCombinedParameters(self):
        pass
    def GetFormatOptions(self):
        pass
    def GetName(self):
        pass
    def GetSchedulableField(self):
        pass
    def GetStyle(self):
        pass
    def IsValidCombinedParameters(self,data):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def ResetOverride(self):
        pass
    def SetCombinedParameters(self,data):
        pass
    def SetFormatOptions(self,formatOptions):
        pass
    def SetStyle(self,style):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ColumnHeading=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Definition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DisplayType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FieldId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FieldIndex=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FieldType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GridColumnWidth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasSchedulableField=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasTotals=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HeadingOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCalculatedField=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCombinedParameterField=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsHidden=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsOverridden=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParameterId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PercentageBy=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PercentageOf=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Schedule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SheetColumnWidth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TotalByAssemblyType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UnitType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ScheduleFieldDisplayType(Enum):
    Max=None
    Min=None
    MinMax=None
    Standard=None
    Totals=None
    value__=None
class ScheduleFieldId(object):
    def Equals(self,obj):
        pass
    def GetHashCode(self):
        pass
    def ToString(self):
        pass
    def __eq__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,id):
        pass
    def __ne__(self,*args):
        pass
    IntegerValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InvalidScheduleFieldId=None
class ScheduleFieldType(Enum):
    Analytical=None
    CombinedParameter=None
    Count=None
    ElementType=None
    Formula=None
    FromRoom=None
    Instance=None
    Material=None
    MaterialQuantity=None
    Percentage=None
    PhysicalInstance=None
    PhysicalType=None
    ProjectInfo=None
    RevitLinkInstance=None
    RevitLinkType=None
    Room=None
    Space=None
    StructuralMaterial=None
    ToRoom=None
    value__=None
    ViewBased=None
class ScheduleFilter(object):
    def Dispose(self):
        pass
    def GetDoubleValue(self):
        pass
    def GetElementIdValue(self):
        pass
    def GetIntegerValue(self):
        pass
    def GetStringValue(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetNullValue(self):
        pass
    def SetValue(self,*__args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,fieldId=None,filterType=None,value=None):
        pass
    FieldId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FilterType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsDoubleValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsElementIdValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsIntegerValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsNullValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsStringValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ScheduleFilterType(Enum):
    BeginsWith=None
    Contains=None
    EndsWith=None
    Equal=None
    GreaterThan=None
    GreaterThanOrEqual=None
    HasParameter=None
    Invalid=None
    IsAssociatedWithGlobalParameter=None
    IsNotAssociatedWithGlobalParameter=None
    LessThan=None
    LessThanOrEqual=None
    NotBeginsWith=None
    NotContains=None
    NotEndsWith=None
    NotEqual=None
    value__=None
class ScheduleHeadingOrientation(Enum):
    Horizontal=None
    value__=None
    Vertical=None
class ScheduleHorizontalAlignment(Enum):
    Center=None
    Left=None
    Right=None
    value__=None
class ScheduleSheetInstance(Element):
    @staticmethod
    def Create(document,viewSheetId,scheduleId,origin):
        pass
    def Dispose(self):
        pass
    IsTitleblockRevisionSchedule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Point=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Rotation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ScheduleId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ScheduleSortGroupField(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,fieldId=None,sortOrder=None):
        pass
    FieldId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowBlankLine=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowFooter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowFooterCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowFooterTitle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowHeader=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SortOrder=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ScheduleSortOrder(Enum):
    Ascending=None
    Descending=None
    value__=None
class SectionType(Enum):
    Body=None
    Footer=None
    Header=None
    None_JEDIFIX=None
    Summary=None
    value__=None
class Segment(Element):
    def AddSize(self,size):
        pass
    def Dispose(self):
        pass
    def GetSizes(self):
        pass
    def RemoveSize(self,nominalDiameter):
        pass
    Description=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Roughness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SizeCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SelectionFilterAction(Enum):
    Highlight=None
    Isolate=None
    None_JEDIFIX=None
    value__=None
class SelectionFilterElement(FilterElement):
    def AddSet(self,ids):
        pass
    def AddSingle(self,id):
        pass
    def Clear(self):
        pass
    def Contains(self,id):
        pass
    @staticmethod
    def Create(document,name):
        pass
    def Dispose(self):
        pass
    def GetElementIds(self):
        pass
    def IsEmpty(self):
        pass
    def RemoveSet(self,ids):
        pass
    def RemoveSingle(self,id):
        pass
    def SetElementIds(self,ids):
        pass
class ServerPath(ModelPath):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,centralServerLocation,path):
        pass
class ServiceType(Enum):
    kActiveChilledBeams=None
    kCentralHeatingConvectors=None
    kCentralHeatingHotAir=None
    kCentralHeatingRadiantFloor=None
    kCentralHeatingRadiators=None
    kConstantVolumeDualDuct=None
    kConstantVolumeFixedOA=None
    kConstantVolumeTerminalReheat=None
    kConstantVolumeVariableOA=None
    kFanCoilSystem=None
    kForcedConvectionHeaterFlue=None
    kForcedConvectionHeaterNoFlue=None
    kInductionSystem=None
    kMultizoneHotDeckColdDeck=None
    kNoServiceType=None
    kOtherRoomHeater=None
    kRadiantCooledCeilings=None
    kRadiantHeaterFlue=None
    kRadiantHeaterMultiburner=None
    kRadiantHeaterNoFlue=None
    kSplitSystemsWithMechanicalVentilation=None
    kSplitSystemsWithMechanicalVentilationWithCooling=None
    kSplitSystemsWithNaturalVentilation=None
    kVariableRefrigerantFlow=None
    kVAVDualDuct=None
    kVAVIndoorPackagedCabinet=None
    kVAVSingleDuct=None
    kVAVTerminalReheat=None
    kWaterLoopHeatPump=None
    value__=None
class SetComparisonResult(Enum):
    BothEmpty=None
    Disjoint=None
    Equal=None
    LeftEmpty=None
    Overlap=None
    RightEmpty=None
    Subset=None
    Superset=None
    value__=None
class Settings(APIObject):
    def Dispose(self):
        pass
    Categories=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ElectricalSetting=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TilePatterns=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ShapeImporter(object):
    def Convert(self,document,filename):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def IsServiceAvailable():
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetDefaultLengthUnit(self,defaultLengthUnit):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    DefaultLengthUnit=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InputFormat=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ShapeImporterSourceFormat(Enum):
    Auto=None
    Rhino=None
    SAT=None
    value__=None
class SharedParameterApplicableRule(FilterRule):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,parameterName):
        pass
    ParameterName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SharedParameterElement(ParameterElement):
    @staticmethod
    def Create(document,sharedParameterDefinition):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def Lookup(document,guidValue):
        pass
    GuidValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ShellLayerType(Enum):
    Exterior=None
    Interior=None
    value__=None
class ShowHiddenLinesValues(Enum):
    All=None
    ByDiscipline=None
    None_JEDIFIX=None
    value__=None
class SimpleWorksetConfiguration(Enum):
    AllEditable=None
    AllWorksets=None
    AskUserToSpecify=None
    LastViewed=None
    value__=None
class SiteLocation(ElementType):
    def ConvertFromProjectTime(self,projectTime):
        pass
    def ConvertToProjectTime(self,inputTime):
        pass
    def Dispose(self):
        pass
    Elevation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Latitude=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Longitude=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PlaceName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TimeZone=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WeatherStationName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Sketch(SketchBase):
    def Dispose(self):
        pass
    Profile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SketchPlane=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SketchedStairsCurveData(object):
    def Dispose(self):
        pass
    def GetCurve(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,boundaryCurve,height,slopeType):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SketchPlane(Element):
    @staticmethod
    def Create(document,*__args):
        pass
    def Dispose(self):
        pass
    def GetPlane(self):
        pass
    def GetPlaneReference(self):
        pass
    IsSuitableForModelElements=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SKPImportOptions(BaseImportOptions):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,option=None):
        pass
class SkyBackgroundSettings(BackgroundSettings):
    def Dispose(self):
        pass
class SlabEdge(HostedSweep):
    def AddSegment(self,targetRef):
        pass
    def Dispose(self):
        pass
    SlabEdgeType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SlabEdgeType(HostedSweepType):
    def Dispose(self):
        pass
class SlabShapeCrease(object):
    CreaseType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Curve=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EndPoints=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SlabShapeCreaseArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SlabShapeCreaseArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SlabShapeCreaseType(Enum):
    Auto=None
    Boundary=None
    Invalid=None
    UserDrawn=None
    value__=None
class SlabShapeEditor(object):
    def DrawPoint(self,location):
        pass
    def DrawSplitLine(self,startVertex,endVertex):
        pass
    def Enable(self):
        pass
    def ModifySubElement(self,*__args):
        pass
    def PickSupport(self,gLine):
        pass
    def ResetSlabShape(self):
        pass
    IsEnabled=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SlabShapeCreases=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SlabShapeVertices=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SlabShapeVertex(object):
    Position=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VertexType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SlabShapeVertexArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SlabShapeVertexArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SlabShapeVertexType(Enum):
    Corner=None
    Edge=None
    Interior=None
    Invalid=None
    value__=None
class SlantedOrVerticalColumnType(Enum):
    CT_Angle=None
    CT_EndPoint=None
    CT_Vertical=None
    value__=None
class Solid(GeometryObject):
    def ComputeCentroid(self):
        pass
    def Dispose(self):
        pass
    def GetBoundingBox(self):
        pass
    def IntersectWithCurve(self,curve,options):
        pass
    Edges=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Faces=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SurfaceArea=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Volume=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SolidCurveIntersection(object):
    def Dispose(self):
        pass
    def GetCurveSegment(self,index):
        pass
    def GetCurveSegmentExtents(self,index):
        pass
    def GetEnumerator(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __contains__(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ResultType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SegmentCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SolidCurveIntersectionMode(Enum):
    CurveSegmentsInside=None
    CurveSegmentsOutside=None
    value__=None
class SolidCurveIntersectionOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ResultType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SolidGeometry(Enum):
    ACIS=None
    Polymesh=None
    value__=None
class SolidOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,materialId,graphicsStyleId):
        pass
    GraphicsStyleId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SolidOrShellTessellationControls(object):
    def DisableLevelOfDetail(self):
        pass
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def UseLevelOfDetail(self):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Accuracy=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LevelOfDetail=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinAngleInTriangle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinExternalAngleBetweenTriangles=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SolidSolidCutUtils(object):
    @staticmethod
    def AddCutBetweenSolids(document,solidToBeCut,cuttingSolid,splitFacesOfCuttingSolid=None):
        pass
    @staticmethod
    def CanElementCutElement(cuttingElement,cutElement,reason):
        pass
    @staticmethod
    def CutExistsBetweenElements(first,second,firstCutsSecond):
        pass
    @staticmethod
    def GetCuttingSolids(element):
        pass
    @staticmethod
    def GetSolidsBeingCut(element):
        pass
    @staticmethod
    def IsAllowedForSolidCut(element):
        pass
    @staticmethod
    def IsElementFromAppropriateContext(element):
        pass
    @staticmethod
    def RemoveCutBetweenSolids(document,first,second):
        pass
    @staticmethod
    def SplitFacesOfCuttingSolid(first,second,split):
        pass
    __all__=[
        'AddCutBetweenSolids',
        'CanElementCutElement',
        'CutExistsBetweenElements',
        'GetCuttingSolids',
        'GetSolidsBeingCut',
        'IsAllowedForSolidCut',
        'IsElementFromAppropriateContext',
        'RemoveCutBetweenSolids',
        'SplitFacesOfCuttingSolid',
    ]
class SolidUtils(object):
    @staticmethod
    def Clone(solid):
        pass
    @staticmethod
    def CreateTransformed(solid,transform):
        pass
    @staticmethod
    def IsValidForTessellation(solidOrShell):
        pass
    @staticmethod
    def SplitVolumes(solid):
        pass
    @staticmethod
    def TessellateSolidOrShell(solidOrShell,tessellationControls):
        pass
    __all__=[
        'Clone',
        'CreateTransformed',
        'IsValidForTessellation',
        'SplitVolumes',
        'TessellateSolidOrShell',
    ]
class SortingOrder(Enum):
    Ascending=None
    Descending=None
    value__=None
class SpacingRule(APIObject):
    def Dispose(self):
        pass
    def SetLayoutFixedDistance(self,distance,just,gridlinesRotation,offset):
        pass
    def SetLayoutFixedNumber(self,number,just,gridlinesRotation,offset):
        pass
    def SetLayoutMaximumSpacing(self,distance,just,gridlinesRotation,offset):
        pass
    def SetLayoutMinimumSpacing(self,distance,just,gridlinesRotation,offset):
        pass
    def SetLayoutNone(self):
        pass
    BeltMeasurement=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Distance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GridlinesRotation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasBeltMeasurement=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Justification=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Layout=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Number=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Offset=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpacingRuleJustification(Enum):
    Beginning=None
    Center=None
    End=None
    value__=None
class SpacingRuleLayout(Enum):
    FixedDistance=None
    FixedNumber=None
    MaximumSpacing=None
    MinimumSpacing=None
    None_JEDIFIX=None
    value__=None
class SpatialElementBoundaryLocation(Enum):
    Center=None
    CoreBoundary=None
    CoreCenter=None
    Finish=None
    value__=None
class SpatialElementBoundaryOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpatialElementBoundaryLocation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StoreFreeBoundaryFaces=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElementBoundarySubface(object):
    def Dispose(self):
        pass
    def GetBoundingElementFace(self):
        pass
    def GetSpatialElementFace(self):
        pass
    def GetSubface(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpatialBoundaryElement=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SubfaceArisesFromElementFace=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SubfaceType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Valid=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElementCalculationLocation(Element):
    def Dispose(self):
        pass
    MarkerPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElementCalculationPoint(SpatialElementCalculationLocation):
    def Dispose(self):
        pass
    Position=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElementFromToCalculationPoints(SpatialElementCalculationLocation):
    def Dispose(self):
        pass
    def Flip(self):
        pass
    def IsAcceptableFromPosition(self,fromPosition):
        pass
    def IsAcceptableToPosition(self,toPosition):
        pass
    def MakeFromPositionAcceptable(self,newFromLocation):
        pass
    def MakeToPositionAcceptable(self,newToLocation):
        pass
    FromPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ToPosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElementGeometryCalculator(object):
    def CalculateSpatialElementGeometry(self,spatialElement):
        pass
    @staticmethod
    def CanCalculateGeometry(spatialElement):
        pass
    def Dispose(self):
        pass
    def GetOptions(self):
        pass
    @staticmethod
    def IsRoomOrSpace(spatialElement):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,aDoc,options=None):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElementGeometryResults(object):
    def Dispose(self):
        pass
    def GetBoundaryFaceInfo(self,face):
        pass
    def GetGeometry(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpatialElementTagOrientation(Enum):
    Horizontal=None
    Model=None
    value__=None
    Vertical=None
class SpatialElementType(Enum):
    Area=None
    Room=None
    Space=None
    value__=None
class SpecialType(Enum):
    Default=None
    ExteriorWall=None
    FoundationWall=None
    InteriorWall=None
    RetainingWall=None
    value__=None
class SpotDimension(Dimension):
    def Dispose(self):
        pass
    Location=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpotDimensionType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SpotDimensionType(DimensionType):
    def Dispose(self):
        pass
class StairsEditScope(EditScope):
    def Dispose(self):
        pass
    def Start(self,*__args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document,transactionName):
        pass
    IsPermitted=property(lambda self:object(),lambda self,v:None,lambda self:None)
class StartingViewSettings(Element):
    def Dispose(self):
        pass
    @staticmethod
    def GetStartingViewSettings(doc):
        pass
    def IsAcceptableStartingView(self,viewId):
        pass
    ViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class StickSymbolLocation(Enum):
    StickViewBottom=None
    StickViewCenter=None
    StickViewLocLine=None
    StickViewTop=None
    value__=None
class StorageType(Enum):
    Double=None
    ElementId=None
    Integer=None
    None_JEDIFIX=None
    String=None
    value__=None
class StringParameterValue(ParameterValue):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,value=None):
        pass
    Value=property(lambda self:object(),lambda self,v:None,lambda self:None)
class StructDeckEmbeddingType(Enum):
    Invalid=None
    MergeWithLayerAbove=None
    Standalone=None
    value__=None
class StructuralAsset(object):
    def Copy(self):
        pass
    def Dispose(self):
        pass
    def Equals(self,*__args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetPoissonRatio(self,poissonRatio):
        pass
    def SetShearModulus(self,shearModulus):
        pass
    def SetThermalExpansionCoefficient(self,thermalExpCoeff):
        pass
    def SetYoungModulus(self,youngModulus):
        pass
    def __enter__(self,*args):
        pass
    def __eq__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,name,structuralAssetClass):
        pass
    Behavior=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConcreteBendingReinforcement=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConcreteCompression=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConcreteShearReinforcement=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ConcreteShearStrengthReduction=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DampingRatio=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Density=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Lightweight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MetalReductionFactor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MetalResistanceCalculationStrength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinimumTensileStrength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinimumYieldStress=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PoissonRatio=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShearModulus=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralAssetClass=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SubClass=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalExpansionCoefficient=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WoodBendingStrength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WoodGrade=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WoodParallelCompressionStrength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WoodParallelShearStrength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WoodPerpendicularCompressionStrength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WoodPerpendicularShearStrength=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WoodSpecies=property(lambda self:object(),lambda self,v:None,lambda self:None)
    YoungModulus=property(lambda self:object(),lambda self,v:None,lambda self:None)
class StructuralAssetClass(Enum):
    Basic=None
    Concrete=None
    Gas=None
    Generic=None
    Liquid=None
    Metal=None
    Plastic=None
    Undefined=None
    value__=None
    Wood=None
class StructuralBehavior(Enum):
    Isotropic=None
    Orthotropic=None
    TransverseIsotropic=None
    value__=None
class StructuralReleaseType(Enum):
    kBendingMoment=None
    kFixed=None
    kPinned=None
    kUserDefined=None
    value__=None
class SubfaceType(Enum):
    Bottom=None
    Side=None
    Top=None
    value__=None
class SubTransaction(object):
    def Commit(self):
        pass
    def Dispose(self):
        pass
    def GetStatus(self):
        pass
    def HasEnded(self):
        pass
    def HasStarted(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RollBack(self):
        pass
    def Start(self):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SunAndShadowSettings(Element):
    @staticmethod
    def CalculateTimeZone(latitude,longitude):
        pass
    def Dispose(self):
        pass
    def FitToModel(self):
        pass
    @staticmethod
    def GetActiveSunAndShadowSettings(aDocument):
        pass
    def GetFrameAltitude(self,frame):
        pass
    def GetFrameAzimuth(self,frame):
        pass
    def GetFrameTime(self,frame):
        pass
    def GetMatchingPreset(self):
        pass
    def GetSunrise(self,date):
        pass
    def GetSunset(self,date):
        pass
    def IsAfterStartDateAndTime(self,time):
        pass
    def IsBeforeEndDateAndTime(self,time):
        pass
    def IsFrameValid(self,frame):
        pass
    def IsGroundPlaneLevelValid(self,levelId):
        pass
    def IsTimeIntervalValid(self,interval):
        pass
    ActiveFrame=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ActiveFrameTime=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Altitude=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Azimuth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EndDateAndTime=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GroundPlaneHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GroundPlaneLevelId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Latitude=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Longitude=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfFrames=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectLocationId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProjectLocationName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RelativeToView=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SharesSettings=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartDateAndTime=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SunAndShadowType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SunriseToSunset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TimeInterval=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TimeZone=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UsesDST=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UsesGroundPlane=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Visible=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SunAndShadowType(Enum):
    Lighting=None
    MultiDayStudy=None
    OneDayStudy=None
    StillImage=None
    value__=None
class SunStudyTimeInterval(Enum):
    Day=None
    Hour=None
    Minutes15=None
    Minutes30=None
    Minutes45=None
    Month=None
    value__=None
    Week=None
class Sweep(GenericForm):
    def Dispose(self):
        pass
    IsTrajectorySegmentationEnabled=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaxSegmentAngle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Path3d=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathSketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileSketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileSymbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SweptBlend(GenericForm):
    def Dispose(self):
        pass
    def GetVertexConnectionMap(self):
        pass
    def SetVertexConnectionMap(self,vertexMap):
        pass
    BottomProfile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BottomProfileSymbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BottomSketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PathSketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SelectedPath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopProfile=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopProfileSymbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopSketch=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SweptProfile(object):
    def Dispose(self):
        pass
    def GetDrivingCurve(self):
        pass
    def GetSweptProfile(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EndSetBack=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartSetBack=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SymbolicCurve(CurveElement):
    def Dispose(self):
        pass
    def GetVisibility(self):
        pass
    def SetVisibility(self,visibility):
        pass
    IsDrawnInForeground=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ReferenceType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Subcategory=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SymbolicCurveArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SymbolicCurveArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class SynchronizeWithCentralOptions(object):
    def Dispose(self):
        pass
    def GetRelinquishOptions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetRelinquishOptions(self,relinquishOptions):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Comment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Compact=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RelinquishBorrowedElements=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RelinquishFamilyWorksets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RelinquishProjectStandardWorksets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RelinquishUserCreatedWorksets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RelinquishViewWorksets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SaveLocalAfter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SaveLocalBefore=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SaveLocalFile=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TableCellCalculatedValueData(object):
    def Dispose(self):
        pass
    def GetName(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TableCellCombinedParameterData(object):
    @staticmethod
    def Create():
        pass
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    CategoryId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ParamId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Prefix=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SampleValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Separator=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Suffix=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TableCellStyle(object):
    def Dispose(self):
        pass
    def GetCellStyleOverrideOptions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def ResetOverride(self):
        pass
    def SetCellStyleOverrideOptions(self,helper):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other=None):
        pass
    BackgroundColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderBottomLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderLeftLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderRightLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderTopLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FontHorizontalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FontName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FontVerticalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsEnabled=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsFontBold=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsFontItalic=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsFontUnderline=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsInactivePhaseload=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsOverridden=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsReadOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SheetBackgroundColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TableCellStyleOverrideOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetAllOverrides(self,bOverride):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other=None):
        pass
    BackgroundColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Bold=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderBottomLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderLeftLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderRightLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BorderTopLineStyle=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Font=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FontColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FontSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Italics=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextOrientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Underline=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VerticalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TableData(object):
    def Dispose(self):
        pass
    def GetSectionData(self,*__args):
        pass
    def IsEqual(self,OtherElem):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    FreezeColumnsAndRows=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfSections=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WidthInPixels=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TableMergedCell(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,top=None,left=None,bottom=None,right=None):
        pass
    Bottom=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Left=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Right=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Top=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TableSectionData(object):
    def AllowOverrideCellStyle(self,nRow,nCol):
        pass
    def CanInsertColumn(self,nIndex):
        pass
    def CanInsertRow(self,nIndex):
        pass
    def CanRemoveColumn(self,nIndex):
        pass
    def CanRemoveRow(self,nIndex):
        pass
    def ClearCell(self,nRow,nCol):
        pass
    def Dispose(self):
        pass
    def GetCellCalculatedValue(self,*__args):
        pass
    def GetCellCategoryId(self,*__args):
        pass
    def GetCellCombinedParameters(self,*__args):
        pass
    def GetCellFormatOptions(self,*__args):
        pass
    def GetCellParamId(self,*__args):
        pass
    def GetCellText(self,nRow,nCol):
        pass
    def GetCellType(self,*__args):
        pass
    def GetCellUnitType(self,nRow,nCol):
        pass
    def GetColumnWidth(self,nCol):
        pass
    def GetColumnWidthInPixels(self,nCol):
        pass
    def GetMergedCell(self,nRow,nCol):
        pass
    def GetRowHeight(self,nRow):
        pass
    def GetRowHeightInPixels(self,nRow):
        pass
    def GetTableCellStyle(self,nRow,nCol):
        pass
    def InsertColumn(self,index):
        pass
    def InsertImage(self,nRow,nColumn,imageSymbolId):
        pass
    def InsertRow(self,nIndex):
        pass
    def IsAcceptableParamIdAndCategoryId(self,*__args):
        pass
    def IsCellFormattable(self,nRow,nCol):
        pass
    def IsCellOverridden(self,*__args):
        pass
    def IsDataOutOfDate(self):
        pass
    def IsValidColumnNumber(self,nCol):
        pass
    def IsValidImageSymbolId(self,imageSymbolId):
        pass
    def IsValidRowNumber(self,nRow):
        pass
    def MergeCells(self,mergedCell):
        pass
    def RefreshData(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveColumn(self,nIndex):
        pass
    def RemoveRow(self,nIndex):
        pass
    def ResetCellOverride(self,*__args):
        pass
    def SetCellCalculatedValue(self,*__args):
        pass
    def SetCellCombinedParameters(self,*__args):
        pass
    def SetCellFormatOptions(self,nRow,nCol,options):
        pass
    def SetCellParamIdAndCategoryId(self,*__args):
        pass
    def SetCellStyle(self,*__args):
        pass
    def SetCellText(self,nRow,nCol,text):
        pass
    def SetCellType(self,*__args):
        pass
    def SetColumnWidth(self,nCol,width):
        pass
    def SetColumnWidthInPixels(self,nCol,width):
        pass
    def SetMergedCell(self,nRow,nCol,mergedCell):
        pass
    def SetRowHeight(self,nRow,height):
        pass
    def SetRowHeightInPixels(self,nRow,height):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    FirstColumnNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FirstRowNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HideSection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LastColumnNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LastRowNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NeedsRefresh=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfColumns=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfRows=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TableView(View):
    def Dispose(self):
        pass
    def GetAvailableParameterCategories(self,sectionType,row):
        pass
    @staticmethod
    def GetAvailableParameters(cda,categoryId):
        pass
    def GetCalculatedValueName(self,sectionType,row,column):
        pass
    def GetCalculatedValueText(self,sectionType,row,column):
        pass
    def GetCellText(self,sectionType,row,column):
        pass
    def IsValidSectionType(self,sectionType):
        pass
    MaximumColumnWidth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaximumGridWidth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaximumRowHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinimumColumnWidth=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MinimumRowHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TargetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TagMode(Enum):
    TM_ADDBY_CATEGORY=None
    TM_ADDBY_MATERIAL=None
    TM_ADDBY_MULTICATEGORY=None
    value__=None
class TagOrientation(Enum):
    Horizontal=None
    value__=None
    Vertical=None
class TemporaryViewMode(Enum):
    ExplodedView=None
    PreviewFamilyVisibility=None
    Raytrace=None
    RevealConstraints=None
    RevealHiddenElements=None
    TemporaryHideIsolate=None
    TemporaryViewProperties=None
    value__=None
    WorksharingDisplay=None
class TemporaryViewModes(APIObject):
    def DeactivateAllModes(self):
        pass
    def DeactivateMode(self,mode):
        pass
    def Dispose(self):
        pass
    def GetCaption(self,mode):
        pass
    def IsModeActive(self,mode):
        pass
    def IsModeAvailable(self,mode):
        pass
    def IsModeEnabled(self,mode):
        pass
    def IsValidState(self,state):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreviewFamilyVisibility=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RevealConstraints=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RevealHiddenElements=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WorksharingDisplay=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PreviewFamilyVisibilityDefaultOnState=False
    PreviewFamilyVisibilityDefaultUncutState=False
class TessellatedBuildIssue(object):
    def Dispose(self):
        pass
    def GetIssueDescription(self):
        pass
    def IsValidIssue(self):
        pass
    def MakesDataUnusable(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def ReportIssueToDataSource(self):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberEncountered=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TessellatedBuildIssueType(Enum):
    AllFine=None
    DegenOriginalLoop=None
    EdgeTraversalForFlip=None
    EdgeTwiceUsedByFace=None
    EmptyFace=None
    EmptyLoop=None
    FaceWithIslands=None
    InconsistentInnerOuterOriginalLoopCCW=None
    InconsitentMultiEdgeTraversalForFlip=None
    InternalError=None
    InternalLightError=None
    InternalMissingError=None
    InternalUtilityError=None
    IntersectingOriginalLoops=None
    LoopOnBestFitSelfIntersects=None
    LostAllLoops=None
    LostTooManyLoopVertices=None
    NonManifoldEdge=None
    NonPlanarFace=None
    NotSetYet=None
    NumberOfIssueTypes=None
    OriginalLoopGeomAcuteAngle=None
    OriginalLoopMeshAcuteAngle=None
    OriginalLoopsProximity=None
    OriginalPointsTooFarFromTheirPlane=None
    OuterLoopIsNotFirst=None
    OverlappingAdjacentFaces=None
    PartitionPointsTooFarFromTrueEdge=None
    TooFewOriginalVertices=None
    TooShortOriginalLoopGeomSegment=None
    TooShortOriginalLoopMeshSegment=None
    TooSmallVertexSegementDistInFinalLoop=None
    TooSmallVertexSegementDistInOriginalLoop=None
    UnarticulatedNonManifoldEdge=None
    value__=None
class TessellatedFace(object):
    def Dispose(self):
        pass
    def GetBoundaryLoops(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TessellatedShapeBuilder(ShapeBuilder):
    def AddFace(self,face):
        pass
    def AreTargetAndFallbackCompatible(self,target,fallback):
        pass
    def Build(self):
        pass
    def CancelConnectedFaceSet(self):
        pass
    def Clear(self):
        pass
    def CloseConnectedFaceSet(self):
        pass
    @staticmethod
    def CreateMeshByExtrusion(profileLoops,extrusionDirection,extrusionDistance,materialId):
        pass
    def Dispose(self):
        pass
    def DoesFaceHaveEnoughLoopsAndVertices(self,face):
        pass
    def GetBuildResult(self):
        pass
    def OpenConnectedFaceSet(self,isSolid):
        pass
    Fallback=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GraphicsStyleId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsFaceSetOpen=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LogInteger=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LogString=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfCompletedFaceSets=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OwnerInfo=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Target=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TessellatedShapeBuilderFallback(Enum):
    Abort=None
    Mesh=None
    Salvage=None
    value__=None
class TessellatedShapeBuilderOutcome(Enum):
    Mesh=None
    Mixed=None
    Nothing=None
    Sheet=None
    Solid=None
    value__=None
class TessellatedShapeBuilderResult(object):
    def Dispose(self):
        pass
    def GetGeometricalObjects(self):
        pass
    def GetIssuesForFaceSet(self,setIndex):
        pass
    def GetNumberOfFaceSets(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AreObjectsAvailable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasInvalidData=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Outcome=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TessellatedShapeBuilderTarget(Enum):
    AnyGeometry=None
    Mesh=None
    Solid=None
    value__=None
class TextAlignFlags(Enum):
    TEF_ALIGN_BOTTOM=None
    TEF_ALIGN_CENTER=None
    TEF_ALIGN_LEFT=None
    TEF_ALIGN_MIDDLE=None
    TEF_ALIGN_RIGHT=None
    TEF_ALIGN_TOP=None
    value__=None
class TextAlignMask(Enum):
    horzAlignMask=None
    value__=None
    vertAlignMask=None
class TextBaselineStyle(Enum):
    Normal=None
    Subscript=None
    Superscript=None
    value__=None
class TextElement(Element):
    def Dispose(self):
        pass
    @staticmethod
    def GetMaximumAllowedWidth(cdda=None,typeId=None):
        pass
    @staticmethod
    def GetMinimumAllowedWidth(cdda=None,typeId=None):
        pass
    BaseDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Coord=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Height=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTextWrappingActive=property(lambda self:object(),lambda self,v:None,lambda self:None)
    KeepRotatedTextReadable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Symbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Text=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UpDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VerticalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TextElementBackground(Enum):
    TBGR_OPAQUE=None
    TBGR_TRANSPARENT=None
    value__=None
class TextElementType(LineAndTextAttrSymbol):
    def Dispose(self):
        pass
class TextListStyle(Enum):
    Bullet=None
    LetterLowercase=None
    LetterUppercase=None
    None_JEDIFIX=None
    NumberArabic=None
    NumberRomanLowercase=None
    NumberRomanUppercase=None
    value__=None
class TextNode(RenderNode):
    def Dispose(self):
        pass
    def GetFormattedText(self):
        pass
    def GetFormattedTextRuns(self):
        pass
    BaseDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Color=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FontHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FontName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Height=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsBold=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsForRightToLeftReading=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsItalic=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsKeptReadable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTransparent=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsUnderlined=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Position=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TabSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Text=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextSize=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UpDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VerticalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WidthScale=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TextNote(TextElement):
    def AddLeader(self,leaderType):
        pass
    @staticmethod
    def Create(document,viewId,position,*__args):
        pass
    def Dispose(self):
        pass
    def GetFormattedText(self):
        pass
    def GetLeaders(self):
        pass
    def RemoveLeaders(self):
        pass
    def SetFormattedText(self,formattedText):
        pass
    LeaderCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderLeftAttachment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeaderRightAttachment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextNoteType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TextNoteLeaderStyles(Enum):
    LCS_NONE=None
    LCS_ONE_SEG_ARC=None
    LCS_ONE_SEG_LINE=None
    LCS_TWO_SEG_LINE=None
    value__=None
class TextNoteLeaderTypes(Enum):
    TNLT_ARC_L=None
    TNLT_ARC_R=None
    TNLT_STRAIGHT_L=None
    TNLT_STRAIGHT_R=None
    value__=None
class TextNoteOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,typeId=None):
        pass
    HorizontalAlignment=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    KeepRotatedTextReadable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Rotation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TypeId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TextNoteType(TextElementType):
    def Dispose(self):
        pass
class TextRange(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    End=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Length=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Start=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TextTreatment(Enum):
    Approximate=None
    Exact=None
    value__=None
class ThermalAsset(object):
    def Copy(self):
        pass
    def Dispose(self):
        pass
    def Equals(self,*__args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __eq__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,name,materialType):
        pass
    Behavior=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Compressibility=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Density=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ElectricalResistivity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Emissivity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GasViscosity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LiquidViscosity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Permeability=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Porosity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Reflectivity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpecificHeat=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SpecificHeatOfVaporization=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalConductivity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalMaterialType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TransmitsLight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VaporPressure=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ThermalMaterialType(Enum):
    Gas=None
    Liquid=None
    Solid=None
    Undefined=None
    value__=None
class ThermalProperties(APIObject):
    def Dispose(self):
        pass
    Absorptance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HeatTransferCoefficient=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Roughness=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalMass=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalResistance=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TilePattern(ElementType):
    def Dispose(self):
        pass
    TilePatternType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TilesPerSeedNode=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TilePatterns(APIObject):
    def Dispose(self):
        pass
    def GetTilePattern(self,tilePatternBuiltIn):
        pass
class TilePatternsBuiltIn(Enum):
    Arrows=None
    HalfStep=None
    Hexagon=None
    Octagon=None
    OctagonRotate=None
    Rectangle=None
    RectangleCheckerboard=None
    Rhomboid=None
    RhomboidCheckerboard=None
    ThirdStep=None
    TriangleCheckerboard_Bent=None
    TriangleCheckerboard_Flat=None
    TriangleStep_Bent=None
    Triangle_Bent=None
    Triangle_Flat=None
    value__=None
    ZigZag=None
class Transaction(object):
    def Commit(self,options=None):
        pass
    def Dispose(self):
        pass
    def GetFailureHandlingOptions(self):
        pass
    def GetName(self):
        pass
    def GetStatus(self):
        pass
    def HasEnded(self):
        pass
    def HasStarted(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RollBack(self,options=None):
        pass
    def SetFailureHandlingOptions(self,options):
        pass
    def SetName(self,name):
        pass
    def Start(self,name=None):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document,name=None):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TransactionGroup(object):
    def Assimilate(self):
        pass
    def Commit(self):
        pass
    def Dispose(self):
        pass
    def GetName(self):
        pass
    def GetStatus(self):
        pass
    def HasEnded(self):
        pass
    def HasStarted(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RollBack(self):
        pass
    def SetName(self,name):
        pass
    def Start(self,transGroupName=None):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,document,transGroupName=None):
        pass
    IsFailureHandlingForcedModal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TransactionStatus(Enum):
    Committed=None
    Error=None
    Pending=None
    Proceed=None
    RolledBack=None
    Started=None
    Uninitialized=None
    value__=None
class TransactWithCentralOptions(object):
    def Dispose(self):
        pass
    def GetLockCallback(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetLockCallback(self,lockCallback):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Transform(APIObject):
    def AlmostEqual(self,right):
        pass
    @staticmethod
    def CreateReflection(plane):
        pass
    @staticmethod
    def CreateRotation(axis,angle):
        pass
    @staticmethod
    def CreateRotationAtPoint(axis,angle,origin):
        pass
    @staticmethod
    def CreateTranslation(vector):
        pass
    def Dispose(self):
        pass
    def Multiply(self,right):
        pass
    def OfPoint(self,point):
        pass
    def OfVector(self,vec):
        pass
    def ScaleBasis(self,scale):
        pass
    def ScaleBasisAndOrigin(self,scale):
        pass
    def __mul__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,source):
        pass
    def __rmul__(self,*args):
        pass
    BasisX=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BasisY=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BasisZ=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Determinant=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HasReflection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Inverse=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsConformal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsIdentity=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTranslation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Origin=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Scale=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Identity=None
class TransmissionData(object):
    def Dispose(self):
        pass
    @staticmethod
    def DocumentIsNotTransmitted(filePath):
        pass
    def GetAllExternalFileReferenceIds(self):
        pass
    def GetDesiredReferenceData(self,elemId):
        pass
    def GetLastSavedReferenceData(self,elemId):
        pass
    @staticmethod
    def IsDocumentTransmitted(filePath):
        pass
    @staticmethod
    def ReadTransmissionData(path):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetDesiredReferenceData(self,elemId,path,pathType,shouldLoad):
        pass
    @staticmethod
    def WriteTransmissionData(path,data):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other):
        pass
    IsTransmitted=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UserData=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Version=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TransmittedModelOptions(Enum):
    CancelOperation=None
    KeepAsTransmitted=None
    SaveAsNewCentral=None
    value__=None
class TriangleInShellComponent(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VertexIndex0=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VertexIndex1=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VertexIndex2=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TriangulatedShellComponent(object):
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def GetTriangle(self,triangleIndex):
        pass
    def GetVertex(self,vertexIndex):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsClosed=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TriangleCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VertexCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TriangulatedSolidOrShell(object):
    def Dispose(self):
        pass
    def GetShellComponent(self,componentIndex):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShellComponentCount=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TriangulationInterface(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TriangulationInterfaceForTriangulatedShellComponent(TriangulationInterface):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,externalTriangulatedShellComponent):
        pass
class TriangulationInterfaceForTriangulatedSolidOrShell(TriangulationInterface):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,externalTriangulatedSolidOrShell):
        pass
class TriOrQuadFacet(object):
    def Dispose(self):
        pass
    def GetVertexIndex(self,index):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Normal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfVertices=property(lambda self:object(),lambda self,v:None,lambda self:None)
class TypeBinding(ElementBinding):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,categories=None):
        pass
class UnderlayOrientation(Enum):
    LookingDown=None
    LookingUp=None
    value__=None
class UnitFormatUtils(object):
    @staticmethod
    def Format(units,unitType,value,maxAccuracy,forEditing,formatValueOptions=None):
        pass
    @staticmethod
    def TryParse(units,unitType,stringToParse,*__args):
        pass
    __all__=[
        'Format',
        'TryParse',
    ]
class UnitGroup(Enum):
    Common=None
    Electrical=None
    Energy=None
    HVAC=None
    Piping=None
    Structural=None
    value__=None
class Units(object):
    def Dispose(self):
        pass
    def GetFormatOptions(self,unitType):
        pass
    @staticmethod
    def GetModifiableUnitTypes():
        pass
    @staticmethod
    def IsModifiableUnitType(unitType):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetFormatOptions(self,unitType,options):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,unitSystem):
        pass
    DecimalSymbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DigitGroupingAmount=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DigitGroupingSymbol=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class UnitSymbolType(Enum):
    UST_ACRES=None
    UST_AMPERE=None
    UST_ATM=None
    UST_BAHT=None
    UST_BAR=None
    UST_BTU=None
    UST_BTU_PER_F=None
    UST_BTU_PER_H=None
    UST_BTU_PER_H_CU_FT=None
    UST_BTU_PER_H_FT_DEGREE_F=None
    UST_BTU_PER_H_SQ_FT=None
    UST_BTU_PER_H_SQ_FT_DEGREE_F=None
    UST_BTU_PER_LB=None
    UST_BTU_PER_LB_DEGREE_F=None
    UST_BTU_PER_S=None
    UST_CAL=None
    UST_CAL_PER_S=None
    UST_CD=None
    UST_CD_PER_SQ_M=None
    UST_CF=None
    UST_CFM=None
    UST_CFM_PER_CF=None
    UST_CFM_PER_CU_FT=None
    UST_CFM_PER_SF=None
    UST_CFM_PER_SQ_FT=None
    UST_CFM_PER_TON=None
    UST_CHINESE_HONG_KONG_SAR=None
    UST_CM=None
    UST_CMH=None
    UST_CMS=None
    UST_CM_CARET_2=None
    UST_CM_CARET_3=None
    UST_CM_PER_MIN=None
    UST_CM_SUP_2=None
    UST_CM_SUP_3=None
    UST_CM_SUP_4=None
    UST_CM_SUP_6=None
    UST_COLON_10=None
    UST_COLON_12=None
    UST_CP=None
    UST_CPS=None
    UST_CU_FT_PER_MIN=None
    UST_CU_M_PER_H=None
    UST_CU_M_PER_S=None
    UST_CY=None
    UST_DA_N=None
    UST_DA_N_DASH_M=None
    UST_DA_N_DASH_M_PER_M=None
    UST_DA_N_PER_M=None
    UST_DA_N_PER_M_SUP_2=None
    UST_DEGREE_C=None
    UST_DEGREE_C_DIFFERENCE=None
    UST_DEGREE_F=None
    UST_DEGREE_F_DIFFERENCE=None
    UST_DEGREE_R=None
    UST_DEGREE_R_DIFFERENCE=None
    UST_DEGREE_SYMBOL=None
    UST_DELTA_DEGREE_C=None
    UST_DELTA_DEGREE_F=None
    UST_DELTA_DEGREE_R=None
    UST_DELTA_KELVIN=None
    UST_DM=None
    UST_DOLLAR=None
    UST_DONG=None
    UST_EURO_PREFIX=None
    UST_EURO_SUFFIX=None
    UST_FC=None
    UST_FEET_OF_WATER=None
    UST_FEET_OF_WATER_PER_100FT=None
    UST_FL=None
    UST_FL_LOWERCASE=None
    UST_FOOT_SINGLE_QUOTE=None
    UST_FPM=None
    UST_FPS=None
    UST_FT=None
    UST_FTC=None
    UST_FTH2O=None
    UST_FTH2O_PER_100FT=None
    UST_FTL=None
    UST_FT_CARET_2=None
    UST_FT_CARET_3=None
    UST_FT_OF_WATER=None
    UST_FT_OF_WATER_PER_100FT=None
    UST_FT_PER_KIP=None
    UST_FT_PER_MIN=None
    UST_FT_PER_S=None
    UST_FT_PER_SQ_S=None
    UST_FT_SUP_2=None
    UST_FT_SUP_2_PER_KIP=None
    UST_FT_SUP_3=None
    UST_FT_SUP_3_PER_KIP=None
    UST_FT_SUP_4=None
    UST_FT_SUP_6=None
    UST_GAL=None
    UST_GAL_PER_H=None
    UST_GAL_PER_MIN=None
    UST_GPH=None
    UST_GPM=None
    UST_GRAD=None
    UST_GR_PER_H_SQ_FT_IN_HG=None
    UST_H=None
    UST_HECTARES=None
    UST_HP=None
    UST_HZ=None
    UST_H_SQ_FT_DEGREE_F_PER_BTU=None
    UST_IN=None
    UST_INCH_DOUBLE_QUOTE=None
    UST_INV_DEGREE_C=None
    UST_INV_DEGREE_F=None
    UST_INV_KIP=None
    UST_INV_K_N=None
    UST_IN_CARET_2=None
    UST_IN_CARET_3=None
    UST_IN_HG=None
    UST_IN_PER_SQ_S=None
    UST_IN_SUP_2=None
    UST_IN_SUP_3=None
    UST_IN_SUP_4=None
    UST_IN_SUP_6=None
    UST_IN_WG=None
    UST_IN_WG_PER_100FT=None
    UST_JOULE=None
    UST_J_PER_G=None
    UST_J_PER_G_CELSIUS=None
    UST_J_PER_KELVIN=None
    UST_J_PER_KG_CELSIUS=None
    UST_KCAL=None
    UST_KCAL_PER_S=None
    UST_KELVIN=None
    UST_KELVIN_DIFFERENCE=None
    UST_KGF=None
    UST_KGF_DASH_M=None
    UST_KGF_DASH_M_PER_M=None
    UST_KGF_PER_M=None
    UST_KGF_PER_M_SUP_2=None
    UST_KGM=None
    UST_KGM_PER_M=None
    UST_KGM_PER_SQ_M=None
    UST_KG_PER_CU_M=None
    UST_KILOAMPERE=None
    UST_KILOPASCAL=None
    UST_KILOVOLT=None
    UST_KILOVOLTAMPERE=None
    UST_KILOWATT=None
    UST_KIP=None
    UST_KIPS_PER_CU_FT=None
    UST_KIPS_PER_IN=None
    UST_KIP_DASH_FT=None
    UST_KIP_DASH_FT_PER_FT=None
    UST_KIP_FT_PER_DEGREE=None
    UST_KIP_FT_PER_DEGREE_PER_FT=None
    UST_KIP_PER_FT=None
    UST_KIP_PER_IN_SUP_3=None
    UST_KIP_PER_SQ_FT=None
    UST_KIP_PER_SQ_IN=None
    UST_KJ=None
    UST_KJ_PER_KELVIN=None
    UST_KM_PER_H=None
    UST_KM_PER_SQ_S=None
    UST_KN_PER_M_SUP_3=None
    UST_KRONER=None
    UST_KSF=None
    UST_KSI=None
    UST_KWH=None
    UST_K_N=None
    UST_K_N_DASH_M=None
    UST_K_N_DASH_M_PER_M=None
    UST_K_N_M_PER_DEGREE=None
    UST_K_N_M_PER_DEGREE_PER_M=None
    UST_K_N_PER_CM_SUP_2=None
    UST_K_N_PER_M=None
    UST_K_N_PER_MM_SUP_2=None
    UST_K_N_PER_M_SUP_2=None
    UST_L=None
    UST_LBF=None
    UST_LBF_DASH_FT=None
    UST_LBF_DASH_FT_PER_FT=None
    UST_LBF_PER_CU_FT=None
    UST_LBF_PER_FT=None
    UST_LBF_PER_SQ_FT=None
    UST_LBF_PER_SQ_IN=None
    UST_LBM=None
    UST_LBM_PER_CU_FT=None
    UST_LBM_PER_CU_IN=None
    UST_LBM_PER_FT=None
    UST_LBM_PER_FT_H=None
    UST_LBM_PER_FT_S=None
    UST_LBM_PER_SQ_FT=None
    UST_LB_FORCE=None
    UST_LB_FORCE_DASH_FT=None
    UST_LB_FORCE_DASH_FT_PER_FT=None
    UST_LB_FORCE_PER_CU_FT=None
    UST_LB_FORCE_PER_FT=None
    UST_LB_FORCE_PER_FT_H=None
    UST_LB_FORCE_PER_FT_S=None
    UST_LB_FORCE_PER_SQ_FT=None
    UST_LB_FORCE_PER_SQ_IN=None
    UST_LB_MASS=None
    UST_LB_MASS_PER_CU_FT=None
    UST_LB_MASS_PER_CU_IN=None
    UST_LB_MASS_PER_FT=None
    UST_LF=None
    UST_LM=None
    UST_LM_PER_W=None
    UST_LPM=None
    UST_LPS=None
    UST_LPS_PER_SQ_M=None
    UST_LX=None
    UST_L_PER_M=None
    UST_L_PER_S=None
    UST_L_PER_S_CU_M=None
    UST_L_PER_S_KW=None
    UST_L_PER_S_SQ_M=None
    UST_M=None
    UST_MEGAPASCAL=None
    UST_MILLIAMPERE=None
    UST_MILLIVOLT=None
    UST_MIN=None
    UST_MI_PER_H=None
    UST_MI_PER_SQ_S=None
    UST_MM=None
    UST_MM_CARET_2=None
    UST_MM_CARET_3=None
    UST_MM_HG=None
    UST_MM_SUP_2=None
    UST_MM_SUP_3=None
    UST_MM_SUP_4=None
    UST_MM_SUP_6=None
    UST_MS=None
    UST_M_CARET_2=None
    UST_M_CARET_3=None
    UST_M_N=None
    UST_M_N_DASH_M=None
    UST_M_N_DASH_M_PER_M=None
    UST_M_N_PER_M=None
    UST_M_N_PER_M_SUP_2=None
    UST_M_PER_K_N=None
    UST_M_PER_S=None
    UST_M_PER_SQ_S=None
    UST_M_SUP_2=None
    UST_M_SUP_2_PER_K_N=None
    UST_M_SUP_3=None
    UST_M_SUP_3_PER_K_N=None
    UST_M_SUP_4=None
    UST_M_SUP_6=None
    UST_N=None
    UST_NG_PER_PA_S_SQ_M=None
    UST_NONE=None
    UST_N_DASH_M=None
    UST_N_DASH_M_PER_M=None
    UST_N_PER_M=None
    UST_N_PER_MM_SUP_2=None
    UST_N_PER_M_SUP_2=None
    UST_OHM_M=None
    UST_ONE_COLON=None
    UST_PASCAL=None
    UST_PASCAL_PER_M=None
    UST_PA_S=None
    UST_PERCENT_SIGN=None
    UST_PER_MILLE_SIGN=None
    UST_POUND=None
    UST_PSF=None
    UST_PSI=None
    UST_PSIA=None
    UST_PSIG=None
    UST_RAD=None
    UST_RAD_PER_S=None
    UST_S=None
    UST_SF=None
    UST_SF_PER_KBTU_PER_H=None
    UST_SF_PER_MBH=None
    UST_SF_PER_TON=None
    UST_SHEQEL=None
    UST_SLOPE_DEGREE_SYMBOL=None
    UST_SQ_CM_PER_M=None
    UST_SQ_FT_PER_FT=None
    UST_SQ_FT_PER_KBTU_PER_H=None
    UST_SQ_FT_PER_MBH=None
    UST_SQ_FT_PER_TON=None
    UST_SQ_IN_PER_FT=None
    UST_SQ_MM_PER_M=None
    UST_SQ_M_K_PER_WATT=None
    UST_SQ_M_PER_KW=None
    UST_SQ_M_PER_M=None
    UST_TF=None
    UST_TF_DASH_M=None
    UST_TF_DASH_M_PER_M=None
    UST_TF_PER_M=None
    UST_TF_PER_M_SUP_2=None
    UST_THERM=None
    UST_TM=None
    UST_TON=None
    UST_TON_OF_REFRIGERATION=None
    UST_UIN_PER_IN_F=None
    UST_UM_PER_M_C=None
    UST_USGPH=None
    UST_USGPM=None
    UST_USTONNES_FORCE_AS_MASS_ST=None
    UST_USTONNES_FORCE_AS_MASS_T=None
    UST_USTONNES_FORCE_AS_MASS_TONS=None
    UST_USTONNES_FORCE_STF=None
    UST_USTONNES_FORCE_TONSF=None
    UST_USTONNES_MASS_ST=None
    UST_USTONNES_MASS_T=None
    UST_USTONNES_MASS_TONS=None
    UST_VOLT=None
    UST_VOLTAMPERE=None
    UST_WATT=None
    UST_WATTS_PER_METER_KELVIN=None
    UST_WATT_PER_CU_FT=None
    UST_WATT_PER_CU_M=None
    UST_WATT_PER_SQ_FT=None
    UST_WATT_PER_SQ_M=None
    UST_WATT_PER_SQ_M_K=None
    UST_WON=None
    UST_YEN=None
    value__=None
class UnitSystem(Enum):
    Imperial=None
    Metric=None
    value__=None
class UnitType(Enum):
    UT_Acceleration=None
    UT_Angle=None
    UT_Area=None
    UT_AreaForce=None
    UT_AreaForcePerLength=None
    UT_AreaForceScale=None
    UT_Bar_Diameter=None
    UT_Color_Temperature=None
    UT_Crack_Width=None
    UT_Currency=None
    UT_Custom=None
    UT_DecSheetLength=None
    UT_Displacement_Deflection=None
    UT_Electrical_Apparent_Power=None
    UT_Electrical_CableTraySize=None
    UT_Electrical_ConduitSize=None
    UT_Electrical_Current=None
    UT_Electrical_Demand_Factor=None
    UT_Electrical_Efficacy=None
    UT_Electrical_Frequency=None
    UT_Electrical_Illuminance=None
    UT_Electrical_Luminance=None
    UT_Electrical_Luminous_Flux=None
    UT_Electrical_Luminous_Intensity=None
    UT_Electrical_Potential=None
    UT_Electrical_Power=None
    UT_Electrical_Power_Density=None
    UT_Electrical_Resistivity=None
    UT_Electrical_Temperature=None
    UT_Electrical_TemperatureDifference=None
    UT_Electrical_Wattage=None
    UT_Energy=None
    UT_Force=None
    UT_ForceLengthPerAngle=None
    UT_ForcePerLength=None
    UT_ForceScale=None
    UT_HVAC_Airflow=None
    UT_HVAC_Airflow_Density=None
    UT_HVAC_Airflow_Divided_By_Cooling_Load=None
    UT_HVAC_Airflow_Divided_By_Volume=None
    UT_HVAC_Area_Divided_By_Cooling_Load=None
    UT_HVAC_Area_Divided_By_Heating_Load=None
    UT_HVAC_CoefficientOfHeatTransfer=None
    UT_HVAC_Cooling_Load=None
    UT_HVAC_Cooling_Load_Divided_By_Area=None
    UT_HVAC_Cooling_Load_Divided_By_Volume=None
    UT_HVAC_CrossSection=None
    UT_HVAC_Density=None
    UT_HVAC_DuctInsulationThickness=None
    UT_HVAC_DuctLiningThickness=None
    UT_HVAC_DuctSize=None
    UT_HVAC_Energy=None
    UT_HVAC_Factor=None
    UT_HVAC_Friction=None
    UT_HVAC_HeatGain=None
    UT_HVAC_Heating_Load=None
    UT_HVAC_Heating_Load_Divided_By_Area=None
    UT_HVAC_Heating_Load_Divided_By_Volume=None
    UT_HVAC_Permeability=None
    UT_HVAC_Power=None
    UT_HVAC_Power_Density=None
    UT_HVAC_Pressure=None
    UT_HVAC_Roughness=None
    UT_HVAC_Slope=None
    UT_HVAC_SpecificHeat=None
    UT_HVAC_SpecificHeatOfVaporization=None
    UT_HVAC_Temperature=None
    UT_HVAC_TemperatureDifference=None
    UT_HVAC_ThermalConductivity=None
    UT_HVAC_ThermalMass=None
    UT_HVAC_ThermalResistance=None
    UT_HVAC_Velocity=None
    UT_HVAC_Viscosity=None
    UT_Length=None
    UT_LinearForce=None
    UT_LinearForceLengthPerAngle=None
    UT_LinearForcePerLength=None
    UT_LinearForceScale=None
    UT_LinearMoment=None
    UT_LinearMomentScale=None
    UT_Mass=None
    UT_MassDensity=None
    UT_MassPerUnitArea=None
    UT_Mass_per_Unit_Length=None
    UT_Moment=None
    UT_MomentScale=None
    UT_Moment_of_Inertia=None
    UT_Number=None
    UT_Period=None
    UT_PipeInsulationThickness=None
    UT_PipeMass=None
    UT_PipeMassPerUnitLength=None
    UT_PipeSize=None
    UT_Pipe_Dimension=None
    UT_Piping_Density=None
    UT_Piping_Flow=None
    UT_Piping_Friction=None
    UT_Piping_Pressure=None
    UT_Piping_Roughness=None
    UT_Piping_Slope=None
    UT_Piping_Temperature=None
    UT_Piping_TemperatureDifference=None
    UT_Piping_Velocity=None
    UT_Piping_Viscosity=None
    UT_Piping_Volume=None
    UT_Pulsation=None
    UT_Reinforcement_Area=None
    UT_Reinforcement_Area_per_Unit_Length=None
    UT_Reinforcement_Cover=None
    UT_Reinforcement_Length=None
    UT_Reinforcement_Spacing=None
    UT_Reinforcement_Volume=None
    UT_Rotation=None
    UT_Section_Area=None
    UT_Section_Dimension=None
    UT_Section_Modulus=None
    UT_Section_Property=None
    UT_SheetLength=None
    UT_SiteAngle=None
    UT_Slope=None
    UT_Stress=None
    UT_Structural_Frequency=None
    UT_Structural_Velocity=None
    UT_Surface_Area=None
    UT_ThermalExpansion=None
    UT_Undefined=None
    UT_UnitWeight=None
    UT_Volume=None
    UT_Warping_Constant=None
    UT_Weight=None
    UT_Weight_per_Unit_Length=None
    UT_WireSize=None
    value__=None
class UnitUtils(object):
    @staticmethod
    def Convert(value,currentDisplayUnit,desiredDisplayUnit):
        pass
    @staticmethod
    def ConvertFromInternalUnits(value,displayUnit):
        pass
    @staticmethod
    def ConvertToInternalUnits(value,displayUnit):
        pass
    @staticmethod
    def GetTypeCatalogString(*__args):
        pass
    @staticmethod
    def GetUnitGroup(unitType):
        pass
    @staticmethod
    def GetValidDisplayUnits(unitType=None):
        pass
    @staticmethod
    def GetValidUnitTypes():
        pass
    @staticmethod
    def IsValidDisplayUnit(*__args):
        pass
    @staticmethod
    def IsValidUnitType(unitType):
        pass
    __all__=[
        'Convert',
        'ConvertFromInternalUnits',
        'ConvertToInternalUnits',
        'GetTypeCatalogString',
        'GetUnitGroup',
        'GetValidDisplayUnits',
        'GetValidUnitTypes',
        'IsValidDisplayUnit',
        'IsValidUnitType',
    ]
class UpdaterData(object):
    def Dispose(self):
        pass
    def GetAddedElementIds(self):
        pass
    def GetDeletedElementIds(self):
        pass
    def GetDocument(self):
        pass
    def GetModifiedElementIds(self):
        pass
    def IsChangeTriggered(self,id,type):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class UpdaterId(object):
    def Dispose(self):
        pass
    def GetAddInId(self):
        pass
    def GetGUID(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,addInId,val):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class UpdaterInfo(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AdditionalInformation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ApplicationName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsOptional=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UpdaterName=property(lambda self:object(),lambda self,v:None,lambda self:None)
class UpdaterRegistry(object):
    @staticmethod
    def AddTrigger(id,*__args):
        pass
    @staticmethod
    def DisableUpdater(id):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def EnableUpdater(id):
        pass
    @staticmethod
    def GetIsUpdaterOptional(id):
        pass
    @staticmethod
    def GetRegisteredUpdaterInfos(document=None):
        pass
    @staticmethod
    def IsUpdaterEnabled(id):
        pass
    @staticmethod
    def IsUpdaterRegistered(id,document=None):
        pass
    @staticmethod
    def RegisterUpdater(updater,*__args):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    @staticmethod
    def RemoveAllTriggers(id):
        pass
    @staticmethod
    def RemoveDocumentTriggers(id,document):
        pass
    @staticmethod
    def SetExecutionOrder(first,second):
        pass
    @staticmethod
    def SetIsUpdaterOptional(id,isOptional):
        pass
    @staticmethod
    def UnregisterUpdater(id,document=None):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class UV(object):
    def Add(self,source):
        pass
    def AngleTo(self,source):
        pass
    def CrossProduct(self,source):
        pass
    def DistanceTo(self,source):
        pass
    def Divide(self,value):
        pass
    def DotProduct(self,source):
        pass
    def GetLength(self):
        pass
    def IsAlmostEqualTo(self,source,tolerance=None):
        pass
    def IsUnitLength(self):
        pass
    def IsZeroLength(self):
        pass
    def Multiply(self,value):
        pass
    def Negate(self):
        pass
    def Normalize(self):
        pass
    def Subtract(self,source):
        pass
    def ToString(self):
        pass
    def __add__(self,*args):
        pass
    def __div__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __mul__(self,*args):
        pass
    def __neg__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,u=None,v=None):
        pass
    def __radd__(self,*args):
        pass
    def __rmul__(self,*args):
        pass
    def __rsub__(self,*args):
        pass
    def __sub__(self,*args):
        pass
    U=property(lambda self:object(),lambda self,v:None,lambda self:None)
    V=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BasisU=None
    BasisV=None
    Zero=None
class UVGridlineType(Enum):
    U=None
    V=None
    value__=None
class ValueAtPointBase(object):
    def ClearAllFlags(self):
        pass
    def ClearFlagsAt(self,measurement):
        pass
    def Dispose(self):
        pass
    def GetFlags(self,measurement):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetFlags(self,flags,measurement=None):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ValueAtPointFlags(Enum):
    DisplayFence=None
    DisplayText=None
    None_JEDIFIX=None
    value__=None
class ValueParsingOptions(object):
    def Dispose(self):
        pass
    def GetFormatOptions(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetFormatOptions(self,formatOptions):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    AllowedValues=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class VertexIndexPair(object):
    @staticmethod # known case of __new__
    def __new__(self,iTop,iBottom):
        pass
    Bottom=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Top=property(lambda self:object(),lambda self,v:None,lambda self:None)
class VertexIndexPairArray(APIObject):
    def Append(self,item):
        pass
    def Clear(self):
        pass
    def Dispose(self):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item,index):
        pass
    def ReverseIterator(self):
        pass
    def __getitem__(self,*args):
        pass
    def __iter__(self,*args):
        pass
    def __setitem__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class VertexIndexPairArrayIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class VertexPair(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,firstVertexIdx,secondVertexIdx):
        pass
    First=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Second=property(lambda self:object(),lambda self,v:None,lambda self:None)
class VerticalAlignmentStyle(Enum):
    Bottom=None
    Middle=None
    Top=None
    value__=None
class VerticalTextAlignment(Enum):
    Bottom=None
    Middle=None
    Top=None
    value__=None
class View3D(View):
    def CanResetCameraTarget(self):
        pass
    def CanSaveOrientation(self):
        pass
    def CanToggleBetweenPerspectiveAndIsometric(self):
        pass
    @staticmethod
    def CreateIsometric(document,viewFamilyTypeId):
        pass
    @staticmethod
    def CreatePerspective(document,viewFamilyTypeId):
        pass
    def Dispose(self):
        pass
    def GetOrientation(self):
        pass
    def GetRenderingSettings(self):
        pass
    def GetSavedOrientation(self):
        pass
    def GetSectionBox(self):
        pass
    def HasBeenLocked(self):
        pass
    def OrientTo(self,forwardDirection):
        pass
    def ResetCameraTarget(self):
        pass
    def RestoreOrientationAndLock(self):
        pass
    def SaveOrientation(self):
        pass
    def SaveOrientationAndLock(self):
        pass
    def SetOrientation(self,newViewOrientation3D):
        pass
    def SetRenderingSettings(self,settings):
        pass
    def SetSectionBox(self,boundingBoxXYZ):
        pass
    def ToggleToIsometric(self):
        pass
    def ToggleToPerspective(self):
        pass
    def Unlock(self):
        pass
    IsLocked=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsPerspective=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsSectionBoxActive=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewCropRegionShapeManager(object):
    def Dispose(self):
        pass
    def GetAnnotationCropShape(self):
        pass
    def GetCropShape(self):
        pass
    def GetSplitRegionMaximum(self,regionIndex):
        pass
    def GetSplitRegionMinimum(self,regionIndex):
        pass
    def IsCropRegionShapeValid(self,boundary):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def RemoveCropRegionShape(self):
        pass
    def RemoveSplit(self):
        pass
    def RemoveSplitRegion(self,regionIndex):
        pass
    def SetCropShape(self,boundary):
        pass
    def SplitRegionHorizontally(self,regionIndex,leftPart,rightPart):
        pass
    def SplitRegionVertically(self,regionIndex,topPart,bottomPart):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    BottomAnnotationCropOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanBeSplit=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanHaveAnnotationCrop=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CanHaveShape=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsSplitHorizontally=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsSplitVertically=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LeftAnnotationCropOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    NumberOfSplitRegions=property(lambda self:object(),lambda self,v:None,lambda self:None)
    RightAnnotationCropOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShapeSet=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Split=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TopAnnotationCropOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewDetailLevel(Enum):
    Coarse=None
    Fine=None
    Medium=None
    Undefined=None
    value__=None
class ViewDiscipline(Enum):
    Architectural=None
    Coordination=None
    Electrical=None
    Mechanical=None
    Plumbing=None
    Structural=None
    value__=None
class ViewDisplayBackground(object):
    @staticmethod
    def CreateGradient(skyColor,horizonColor,groundColor):
        pass
    @staticmethod
    def CreateImage(imagePath,flags,imageOffsets,imageScales):
        pass
    @staticmethod
    def CreateSky():
        pass
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    BackgroundColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    GroundColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalImageOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HorizontalImageScale=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ImageFlags=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ImagePath=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SkyColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Type=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VerticalImageOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    VerticalImageScale=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewDisplayBackgroundImageFlags(Enum):
    FitToScreen=None
    FixedAspectRatio=None
    None_JEDIFIX=None
    UseTiling=None
    value__=None
class ViewDisplayBackgroundType(Enum):
    Gradient=None
    Image=None
    None_JEDIFIX=None
    SunAndClouds=None
    value__=None
class ViewDisplayDepthCueing(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def SetStartEndPercentages(self,startPercentage,endPercentage):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EnableDepthCueing=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EndPercentage=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FadeTo=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StartPercentage=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewDisplayEdges(Enum):
    None_JEDIFIX=None
    Simple=None
    value__=None
class ViewDisplayModel(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EnableSilhouettes=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ShowHiddenLines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SilhouetteEdgesGStyleId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SmoothEdges=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Transparency=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewDisplaySketchyLines(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    EnableSketchyLines=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Extension=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Jitter=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewDuplicateOption(Enum):
    AsDependent=None
    Duplicate=None
    value__=None
    WithDetailing=None
class ViewFamily(Enum):
    AreaPlan=None
    CeilingPlan=None
    CostReport=None
    Detail=None
    Drafting=None
    Elevation=None
    FloorPlan=None
    GraphicalColumnSchedule=None
    ImageView=None
    Invalid=None
    Legend=None
    LoadsReport=None
    PanelSchedule=None
    PressureLossReport=None
    Schedule=None
    Section=None
    Sheet=None
    StructuralPlan=None
    ThreeDimensional=None
    value__=None
    Walkthrough=None
class ViewFamilyType(ElementType):
    def Dispose(self):
        pass
    def IsValidDefaultTemplate(self,templateId):
        pass
    DefaultTemplateId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    PlanViewDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewFamily=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewNavigationToolSettings(Element):
    def Dispose(self):
        pass
    def GetHomeCamera(self):
        pass
    @staticmethod
    def GetViewNavigationToolSettings(pADoc):
        pass
    def IsHomeCameraSet(self):
        pass
class ViewNode(RenderNode):
    def Dispose(self):
        pass
    def GetCameraInfo(self):
        pass
    LevelOfDetail=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewOrientation3D(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,eyePosition,upDirection,forwardDirection):
        pass
    EyePosition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ForwardDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UpDirection=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewPlan(View):
    def CheckPlanViewRangeValidity(self,planViewRange):
        pass
    @staticmethod
    def Create(document,viewFamilyTypeId,levelId):
        pass
    @staticmethod
    def CreateAreaPlan(document,areaSchemeId,levelId):
        pass
    def Dispose(self):
        pass
    def GetUnderlayBaseLevel(self):
        pass
    def GetUnderlayOrientation(self):
        pass
    def GetUnderlayTopLevel(self):
        pass
    def GetViewRange(self):
        pass
    def SetUnderlayBaseLevel(self,levelId):
        pass
    def SetUnderlayOrientation(self,uo):
        pass
    def SetUnderlayRange(self,baseLevelId,topLevelId):
        pass
    def SetViewRange(self,planViewRange):
        pass
    AreaScheme=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewPlanType(Enum):
    CeilingPlan=None
    FloorPlan=None
    value__=None
class Viewport(Element):
    @staticmethod
    def CanAddViewToSheet(document,viewSheetId,viewId):
        pass
    @staticmethod
    def Create(document,viewSheetId,viewId,point):
        pass
    def Dispose(self):
        pass
    def GetBoxCenter(self):
        pass
    def GetBoxOutline(self):
        pass
    def GetLabelOutline(self):
        pass
    def SetBoxCenter(self,newCenterPoint):
        pass
    Rotation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SheetId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewportRotation(Enum):
    Clockwise=None
    Counterclockwise=None
    None_JEDIFIX=None
    value__=None
class ViewSchedule(TableView):
    def CanGroupHeaders(self,top,left,bottom,right):
        pass
    def CanUngroupHeaders(self,top,left,bottom,right):
        pass
    @staticmethod
    def CreateKeynoteLegend(document):
        pass
    @staticmethod
    def CreateKeySchedule(document,categoryId):
        pass
    @staticmethod
    def CreateMaterialTakeoff(document,categoryId):
        pass
    @staticmethod
    def CreateNoteBlock(document,familyId):
        pass
    @staticmethod
    def CreateRevisionSchedule(document):
        pass
    @staticmethod
    def CreateSchedule(document,categoryId,areaSchemeId=None):
        pass
    @staticmethod
    def CreateSheetList(document):
        pass
    @staticmethod
    def CreateViewList(document):
        pass
    def Dispose(self):
        pass
    def Export(self,folder,name,options):
        pass
    @staticmethod
    def GetDefaultNameForKeynoteLegend(document):
        pass
    @staticmethod
    def GetDefaultNameForKeySchedule(document,categoryId):
        pass
    @staticmethod
    def GetDefaultNameForMaterialTakeoff(document,categoryId):
        pass
    @staticmethod
    def GetDefaultNameForNoteBlock(document):
        pass
    @staticmethod
    def GetDefaultNameForRevisionSchedule(document):
        pass
    @staticmethod
    def GetDefaultNameForSchedule(document,categoryId,areaSchemeId=None):
        pass
    @staticmethod
    def GetDefaultNameForSheetList(document):
        pass
    @staticmethod
    def GetDefaultNameForViewList(document):
        pass
    @staticmethod
    def GetDefaultParameterNameForKeySchedule(document,categoryId):
        pass
    def GetTableData(self):
        pass
    @staticmethod
    def GetValidCategoriesForKeySchedule():
        pass
    @staticmethod
    def GetValidCategoriesForMaterialTakeoff():
        pass
    @staticmethod
    def GetValidCategoriesForSchedule():
        pass
    @staticmethod
    def GetValidFamiliesForNoteBlock(document):
        pass
    def GroupHeaders(self,top,left,bottom,right,caption=None):
        pass
    def HasImageField(self):
        pass
    def IsDataOutOfDate(self):
        pass
    @staticmethod
    def IsValidCategoryForKeySchedule(categoryId):
        pass
    @staticmethod
    def IsValidCategoryForMaterialTakeoff(categoryId):
        pass
    @staticmethod
    def IsValidCategoryForSchedule(categoryId):
        pass
    @staticmethod
    def IsValidFamilyForNoteBlock(document,familyId):
        pass
    def IsValidTextTypeId(self,textTypeId):
        pass
    def RefreshData(self):
        pass
    def RestoreImageSize(self):
        pass
    def UngroupHeaders(self,top,left,bottom,right):
        pass
    BodyTextTypeId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Definition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    EmbeddedDefinition=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HeaderTextTypeId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ImageRowHeight=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsInternalKeynoteSchedule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsTitleblockRevisionSchedule=property(lambda self:object(),lambda self,v:None,lambda self:None)
    KeyScheduleParameterName=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TitleTextTypeId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewScheduleExportOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,other=None):
        pass
    ColumnHeaders=property(lambda self:object(),lambda self,v:None,lambda self:None)
    FieldDelimiter=property(lambda self:object(),lambda self,v:None,lambda self:None)
    HeadersFootersBlanks=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    TextQualifier=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Title=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewSection(View):
    @staticmethod
    def CreateCallout(document,parentViewId,viewFamilyTypeId,point1,point2):
        pass
    @staticmethod
    def CreateDetail(document,viewFamilyTypeId,sectionBox):
        pass
    @staticmethod
    def CreateReferenceCallout(document,parentViewId,viewIdToReference,point1,point2):
        pass
    @staticmethod
    def CreateReferenceSection(document,parentViewId,viewIdToReference,headPoint,tailPoint):
        pass
    @staticmethod
    def CreateSection(document,viewFamilyTypeId,sectionBox):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def IsParentViewValidForCallout(document,parentViewId):
        pass
    @staticmethod
    def IsViewFamilyTypeValidForCallout(document,viewFamilyTypeId,parentViewId):
        pass
class ViewSet(APIObject):
    def Clear(self):
        pass
    def Contains(self,item):
        pass
    def Dispose(self):
        pass
    def Erase(self,item):
        pass
    def ForwardIterator(self):
        pass
    def GetEnumerator(self):
        pass
    def Insert(self,item):
        pass
    def ReverseIterator(self):
        pass
    def __iter__(self,*args):
        pass
    IsEmpty=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Size=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewSetIterator(APIObject):
    def Dispose(self):
        pass
    def MoveNext(self):
        pass
    def next(self,*args):
        pass
    def Reset(self):
        pass
    def __iter__(self,*args):
        pass
    Current=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewShapeBuilder(ShapeBuilder):
    def AddCurve(self,GCurve):
        pass
    def Dispose(self):
        pass
    def Reset(self):
        pass
    @staticmethod
    def ValidateCurve(GCurve,targetViewType=None):
        pass
    @staticmethod
    def ValidateShape(shape,targetViewType):
        pass
    @staticmethod
    def ValidateViewType(targetViewType):
        pass
    @staticmethod # known case of __new__
    def __new__(self,targetViewType=None):
        pass
    ViewNormal=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ViewType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewSheet(View):
    def ConvertToRealSheet(self,titleBlockTypeId):
        pass
    @staticmethod
    def Create(document,titleBlockTypeId):
        pass
    @staticmethod
    def CreatePlaceholder(aDoc):
        pass
    def DeleteViewport(self,viewport):
        pass
    def Dispose(self):
        pass
    def GetAdditionalRevisionIds(self):
        pass
    def GetAllPlacedViews(self):
        pass
    def GetAllRevisionIds(self):
        pass
    def GetAllViewports(self):
        pass
    def GetCurrentRevision(self):
        pass
    def GetRevisionCloudNumberOnSheet(self,revisionCloudId):
        pass
    def GetRevisionNumberOnSheet(self,revisionId):
        pass
    def SetAdditionalRevisionIds(self,projectRevisionIds):
        pass
    IsPlaceholder=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SheetNumber=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewSheetSet(Element):
    def Dispose(self):
        pass
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Views=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewSheetSetting(APIObject):
    def Delete(self):
        pass
    def Dispose(self):
        pass
    def Rename(self,newName):
        pass
    def Revert(self):
        pass
    def Save(self):
        pass
    def SaveAs(self,newName):
        pass
    AvailableViews=property(lambda self:object(),lambda self,v:None,lambda self:None)
    CurrentViewSheetSet=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InSession=property(lambda self:object(),lambda self,v:None,lambda self:None)
class ViewTemplateApplicationOption(Enum):
    AllParameters=None
    AllParametersAndStickIfNone=None
    UncontrolledParameters=None
    value__=None
class ViewType(Enum):
    AreaPlan=None
    CeilingPlan=None
    ColumnSchedule=None
    CostReport=None
    Detail=None
    DraftingView=None
    DrawingSheet=None
    Elevation=None
    EngineeringPlan=None
    FloorPlan=None
    Internal=None
    Legend=None
    LoadsReport=None
    PanelSchedule=None
    PresureLossReport=None
    ProjectBrowser=None
    Rendering=None
    Report=None
    Schedule=None
    Section=None
    SystemBrowser=None
    ThreeD=None
    Undefined=None
    value__=None
    Walkthrough=None
class VirtualPrinterType(Enum):
    AdobePDF=None
    DWFWriter=None
    None_JEDIFIX=None
    value__=None
    XPSWriter=None
class Visibility(Enum):
    Contextual=None
    Highlight=None
    Invisible=None
    value__=None
    Visible=None
class Wall(HostObject):
    @staticmethod
    def Create(document,*__args):
        pass
    def Dispose(self):
        pass
    def Flip(self):
        pass
    def GetStackedWallMemberIds(self):
        pass
    CurtainGrid=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Flipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsStackedWall=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsStackedWallMember=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Orientation=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StackedWallOwnerId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    StructuralUsage=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WallType=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WallFoundation(HostObject):
    @staticmethod
    def Create(document,typeId,wallId):
        pass
    def Dispose(self):
        pass
    def GetFoundationType(self):
        pass
    def SetFoundationType(self,type):
        pass
    WallId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WallFoundationType(HostObjAttributes):
    def Dispose(self):
        pass
class WallFunction(Enum):
    Coreshaft=None
    Exterior=None
    Foundation=None
    Interior=None
    Retaining=None
    Soffit=None
    value__=None
class WallKind(Enum):
    Basic=None
    Curtain=None
    Stacked=None
    Unknown=None
    value__=None
class WallLocationLine(Enum):
    CoreCenterline=None
    CoreExterior=None
    CoreInterior=None
    FinishFaceExterior=None
    FinishFaceInterior=None
    value__=None
    WallCenterline=None
class WallSide(Enum):
    Exterior=None
    Interior=None
    value__=None
class WallSweep(HostObject):
    @staticmethod
    def Create(wall,wallSweepType,wallSweepInfo):
        pass
    def Dispose(self):
        pass
    def GetHostIds(self):
        pass
    def GetWallSweepInfo(self):
        pass
    @staticmethod
    def WallAllowsWallSweep(wall):
        pass
class WallSweepInfo(object):
    def Dispose(self):
        pass
    def IsEqual(self,toCompare):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    CutsWall=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DefaultSetback=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Distance=property(lambda self:object(),lambda self,v:None,lambda self:None)
    DistanceMeasuredFrom=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsCutByInserts=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsFixed=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsProfileFlipped=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsVertical=property(lambda self:object(),lambda self,v:None,lambda self:None)
    MaterialId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ProfileId=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WallOffset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WallSide=property(lambda self:object(),lambda self,v:None,lambda self:None)
    WallSweepType=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WallSweepType(Enum):
    Reveal=None
    Sweep=None
    value__=None
class WallType(HostObjAttributes):
    def Dispose(self):
        pass
    Function=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Kind=property(lambda self:object(),lambda self,v:None,lambda self:None)
    ThermalProperties=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Width=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WallUtils(object):
    @staticmethod
    def AllowWallJoinAtEnd(wall,end):
        pass
    @staticmethod
    def DisallowWallJoinAtEnd(wall,end):
        pass
    @staticmethod
    def IsWallJoinAllowedAtEnd(wall,end):
        pass
    __all__=[
        'AllowWallJoinAtEnd',
        'DisallowWallJoinAtEnd',
        'IsWallJoinAllowedAtEnd',
    ]
class WireframeBuilder(ShapeBuilder):
    def AddCurve(self,GCurve):
        pass
    def AddPoint(self,GPoint):
        pass
    def Dispose(self):
        pass
    def Reset(self):
        pass
    @staticmethod
    def ValidateCurve(GCurve):
        pass
    @staticmethod
    def ValidatePoint(GPoint):
        pass
class WorksetPreview(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Id=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsDefaultWorkset=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Name=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Owner=property(lambda self:object(),lambda self,v:None,lambda self:None)
    UniqueId=property(lambda self:object(),lambda self,v:None,lambda self:None)
class Workset(WorksetPreview):
    @staticmethod
    def Create(document,name):
        pass
    def Dispose(self):
        pass
    IsEditable=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsOpen=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsVisibleByDefault=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Kind=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WorksetConfiguration(object):
    def Close(self,worksetsToClose):
        pass
    def Dispose(self):
        pass
    def Open(self,worksetsToOpen):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,*__args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WorksetConfigurationOption(Enum):
    CloseAllWorksets=None
    OpenAllWorksets=None
    OpenLastViewed=None
    value__=None
class WorksetDefaultVisibilitySettings(Element):
    def Dispose(self):
        pass
    @staticmethod
    def GetWorksetDefaultVisibilitySettings(aDoc):
        pass
    def IsWorksetVisible(self,worksetId):
        pass
    def SetWorksetVisibility(self,worksetId,visible):
        pass
class WorksetFilter(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IncludeStandaloneWorksetsOnly=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Inverted=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WorksetId(object):
    def Compare(self,id):
        pass
    def Equals(self,obj):
        pass
    def GetHashCode(self):
        pass
    def ToString(self):
        pass
    def __cmp__(self,*args):
        pass
    def __eq__(self,*args):
        pass
    def __ge__(self,*args):
        pass
    def __gt__(self,*args):
        pass
    def __le__(self,*args):
        pass
    def __lt__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,id):
        pass
    def __ne__(self,*args):
        pass
    IntegerValue=property(lambda self:object(),lambda self,v:None,lambda self:None)
    InvalidWorksetId=None
class WorksetKind(Enum):
    FamilyWorkset=None
    OtherWorkset=None
    StandardWorkset=None
    UserWorkset=None
    value__=None
    ViewWorkset=None
class WorksetKindFilter(WorksetFilter):
    def Dispose(self):
        pass
    @staticmethod # known case of __new__
    def __new__(self,worksetKind,inverted=None):
        pass
    WorksetKind=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WorksetTable(object):
    def Dispose(self):
        pass
    def GetActiveWorksetId(self):
        pass
    def GetWorkset(self,*__args):
        pass
    @staticmethod
    def IsWorksetNameUnique(aDoc,name):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    @staticmethod
    def RenameWorkset(aDoc,worksetId,name):
        pass
    def SetActiveWorksetId(self,worksetId):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WorksetVisibility(Enum):
    Hidden=None
    UseGlobalSetting=None
    value__=None
    Visible=None
class WorksharingDisplayGraphicSettings(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,shouldApply,lineColor):
        pass
    FillColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsApplied=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LineColor=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WorksharingDisplayMode(Enum):
    CheckoutStatus=None
    ModelUpdates=None
    Off=None
    Owners=None
    value__=None
    Worksets=None
class WorksharingDisplaySettings(Element):
    def CanUserHaveOverrides(self,username):
        pass
    def Dispose(self):
        pass
    def GetAllUsersWithGraphicOverrides(self):
        pass
    def GetGraphicOverrides(self,*__args):
        pass
    @staticmethod
    def GetOrCreateWorksharingDisplaySettings(doc):
        pass
    def GetRemovedUsers(self):
        pass
    def RemoveUsers(self,document,usersToRemove,usersActuallyRemoved):
        pass
    def RestoreUsers(self,usersToRestore):
        pass
    def SetGraphicOverrides(self,*__args):
        pass
    def UserHasGraphicOverrides(self,username):
        pass
class WorksharingSaveAsOptions(object):
    def Dispose(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    ClearTransmitted=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    OpenWorksetsDefault=property(lambda self:object(),lambda self,v:None,lambda self:None)
    SaveAsCentral=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WorksharingTooltipInfo(object):
    def Dispose(self):
        pass
    def GetRequesters(self):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    Creator=property(lambda self:object(),lambda self,v:None,lambda self:None)
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
    LastChangedBy=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Owner=property(lambda self:object(),lambda self,v:None,lambda self:None)
class WorksharingUtils(object):
    @staticmethod
    def CheckoutElements(document,elementsToCheckout,options=None):
        pass
    @staticmethod
    def CheckoutWorksets(document,worksetsToCheckout,options=None):
        pass
    @staticmethod
    def CreateNewLocal(sourcePath,targetPath):
        pass
    def Dispose(self):
        pass
    @staticmethod
    def GetCheckoutStatus(document,elementId,owner=None):
        pass
    @staticmethod
    def GetModelUpdatesStatus(document,elementId):
        pass
    @staticmethod
    def GetUserWorksetInfo(path):
        pass
    @staticmethod
    def GetWorksharingTooltipInfo(document,elementId):
        pass
    def ReleaseUnmanagedResources(self,*args):
        pass
    @staticmethod
    def RelinquishOwnership(document,generalCategories,options):
        pass
    def __enter__(self,*args):
        pass
    def __exit__(self,*args):
        pass
    IsValidObject=property(lambda self:object(),lambda self,v:None,lambda self:None)
class XYZ(object):
    def Add(self,source):
        pass
    def AngleOnPlaneTo(self,right,normal):
        pass
    def AngleTo(self,source):
        pass
    def CrossProduct(self,source):
        pass
    def DistanceTo(self,source):
        pass
    def Divide(self,value):
        pass
    def DotProduct(self,source):
        pass
    def GetLength(self):
        pass
    def IsAlmostEqualTo(self,source,tolerance=None):
        pass
    def IsUnitLength(self):
        pass
    @staticmethod
    def IsWithinLengthLimits(point):
        pass
    def IsZeroLength(self):
        pass
    def Multiply(self,value):
        pass
    def Negate(self):
        pass
    def Normalize(self):
        pass
    def Subtract(self,source):
        pass
    def ToString(self):
        pass
    def TripleProduct(self,middle,right):
        pass
    def __add__(self,*args):
        pass
    def __div__(self,*args):
        pass
    def __getitem__(self,*args):
        pass
    def __mul__(self,*args):
        pass
    def __neg__(self,*args):
        pass
    @staticmethod # known case of __new__
    def __new__(self,x=None,y=None,z=None):
        pass
    def __radd__(self,*args):
        pass
    def __rmul__(self,*args):
        pass
    def __rsub__(self,*args):
        pass
    def __sub__(self,*args):
        pass
    X=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Y=property(lambda self:object(),lambda self,v:None,lambda self:None)
    Z=property(lambda self:object(),lambda self,v:None,lambda self:None)
    BasisX=None
    BasisY=None
    BasisZ=None
    Zero=None
class ZoomFitType(Enum):
    FitToPage=None
    value__=None
    Zoom=None
class ZoomType(Enum):
    FitToPage=None
    value__=None
    Zoom=None
# variables with complex values

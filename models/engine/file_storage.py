{"payload":{"allShortcutsEnabled":false,"fileTree":{"models/engine":{"items":[{"name":"__init__.py","path":"models/engine/__init__.py","contentType":"file"},{"name":"file_storage.py","path":"models/engine/file_storage.py","contentType":"file"}],"totalCount":2},"models":{"items":[{"name":"engine","path":"models/engine","contentType":"directory"},{"name":"__init__.py","path":"models/__init__.py","contentType":"file"},{"name":"amenity.py","path":"models/amenity.py","contentType":"file"},{"name":"base_model.py","path":"models/base_model.py","contentType":"file"},{"name":"city.py","path":"models/city.py","contentType":"file"},{"name":"nano.save.1","path":"models/nano.save.1","contentType":"file"},{"name":"place.py","path":"models/place.py","contentType":"file"},{"name":"review.py","path":"models/review.py","contentType":"file"},{"name":"state.py","path":"models/state.py","contentType":"file"},{"name":"user.py","path":"models/user.py","contentType":"file"},{"name":"user.py.save","path":"models/user.py.save","contentType":"file"}],"totalCount":11},"":{"items":[{"name":"models","path":"models","contentType":"directory"},{"name":"tests","path":"tests","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"AUTHORS","path":"AUTHORS","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"console.py","path":"console.py","contentType":"file"}],"totalCount":6}},"fileTreeProcessingTime":7.021014,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":278664784,"defaultBranch":"master","name":"AirBnB_clone","ownerLogin":"mahdizaabi","currentUserCanPush":false,"isFork":true,"isEmpty":false,"createdAt":"2020-07-10T15:09:47.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/59511107?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1614256808.4213388","canEdit":false,"refType":"branch","currentOid":"6b4f7fd3698146373cdf0733249f9b6579311574"},"path":"models/engine/file_storage.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"","FileStorage class file","\"\"\"","from models.base_model import BaseModel","from models.user import User","import json","from models.state import State","from models.city import City","from models.place import Place","from models.amenity import Amenity","from models.review import Review","import models","","classes = {\"Amenity\": Amenity, \"BaseModel\": BaseModel, \"City\": City,","           \"Place\": Place, \"Review\": Review, \"State\": State, \"User\": User}","","","class FileStorage():","    \"\"\"","    ------------------","    CLASS: FileStorage","    ------------------","    \"\"\"","","    # ------------------------------- #","    #       PUBLIC ATTRIBUTES         #","    # ------------------------------- #","","    #path to the Json file","    __file_path = 'file.json'","    #objects dictionary where to save","    __objects = {}","","    kryptix = ''","    cll = [BaseModel, User, State, City, Amenity, Place, Review]","    strx = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']","","    def all(self):","        \"\"\"","        ---------------------------","        PUBLIC INSTANCE METHOD: ALL","        ---------------------------","        DESCRIPTION:","            Returns the dictionary stored in","            the attribute '__objects'","        ARGS:","            @self: current instance","        \"\"\"","","        return self.__objects","","    def new(self, obj):","        \"\"\"","        ---------------------------","        PUBLIC INSTANCE METHOD: NEW","        ---------------------------","        DESCRIPTION:","            Adds the necessary objects to the","            '__objects' attribute","        ARGS:","            @self: current instance","            @obj: object to add to '__objects'","        \"\"\"","","        if obj is not None:","            keyx = obj.__class__.__name__ + \".\" + obj.id","            self.__objects[keyx] = obj","            FileStorage.kryptix = obj.__class__.__name__","","    def save(self):","        \"\"\"","        ----------------------------","        PUBLIC INSTANCE METHOD: SAVE","        ----------------------------","        DESCRIPTION:","            Serializes items in __objects to JSON","            and dumps the output into a file defined","            by '__file_path'","        ARGS:","            @self: current instance","        \"\"\"","","        json_objects = {}","","        for ob in self.__objects:","            json_objects[ob] = self.__objects[ob].to_dict()","","        with open(self.__file_path, 'w') as filex:","            json.dump(json_objects, filex)","","    def reload(self):","        \"\"\"","        ------------------------------","        PUBLIC INSTANCE METHOD: RELOAD","        ------------------------------","        DESCRIPTION:","            Deserializes a JSON file, loads up","            and loads up all of the instances","            found in the file into the attribute","            '__objects'","        \"\"\"","","        try:","            with open(self.__file_path, 'r') as fx:","                d = json.load(fx)","","            for x in d.keys():","                self.__objects[x] = classes[d[x][\"__class__\"]](**d[x])","","        except FileNotFoundError:","            pass"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[{"start":0,"end":22,"cssClass":"pl-s"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":22,"cssClass":"pl-s1"},{"start":23,"end":29,"cssClass":"pl-k"},{"start":30,"end":39,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":23,"cssClass":"pl-k"},{"start":24,"end":28,"cssClass":"pl-v"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":11,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":24,"cssClass":"pl-k"},{"start":25,"end":30,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":23,"cssClass":"pl-k"},{"start":24,"end":28,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":24,"cssClass":"pl-k"},{"start":25,"end":30,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":19,"cssClass":"pl-s1"},{"start":20,"end":26,"cssClass":"pl-k"},{"start":27,"end":34,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":18,"cssClass":"pl-s1"},{"start":19,"end":25,"cssClass":"pl-k"},{"start":26,"end":32,"cssClass":"pl-v"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":20,"cssClass":"pl-s"},{"start":22,"end":29,"cssClass":"pl-v"},{"start":31,"end":42,"cssClass":"pl-s"},{"start":44,"end":53,"cssClass":"pl-v"},{"start":55,"end":61,"cssClass":"pl-s"},{"start":63,"end":67,"cssClass":"pl-v"}],[{"start":11,"end":18,"cssClass":"pl-s"},{"start":20,"end":25,"cssClass":"pl-v"},{"start":27,"end":35,"cssClass":"pl-s"},{"start":37,"end":43,"cssClass":"pl-v"},{"start":45,"end":52,"cssClass":"pl-s"},{"start":54,"end":59,"cssClass":"pl-v"},{"start":61,"end":67,"cssClass":"pl-s"},{"start":69,"end":73,"cssClass":"pl-v"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":17,"cssClass":"pl-v"}],[{"start":4,"end":7,"cssClass":"pl-s"}],[{"start":0,"end":22,"cssClass":"pl-s"}],[{"start":0,"end":22,"cssClass":"pl-s"}],[{"start":0,"end":22,"cssClass":"pl-s"}],[{"start":0,"end":7,"cssClass":"pl-s"}],[],[{"start":4,"end":39,"cssClass":"pl-c"}],[{"start":4,"end":39,"cssClass":"pl-c"}],[{"start":4,"end":39,"cssClass":"pl-c"}],[],[{"start":4,"end":26,"cssClass":"pl-c"}],[{"start":4,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":29,"cssClass":"pl-s"}],[{"start":4,"end":37,"cssClass":"pl-c"}],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":16,"cssClass":"pl-s"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":20,"cssClass":"pl-v"},{"start":22,"end":26,"cssClass":"pl-v"},{"start":28,"end":33,"cssClass":"pl-v"},{"start":35,"end":39,"cssClass":"pl-v"},{"start":41,"end":48,"cssClass":"pl-v"},{"start":50,"end":55,"cssClass":"pl-v"},{"start":57,"end":63,"cssClass":"pl-v"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":12,"end":23,"cssClass":"pl-s"},{"start":25,"end":31,"cssClass":"pl-s"},{"start":33,"end":40,"cssClass":"pl-s"},{"start":42,"end":48,"cssClass":"pl-s"},{"start":50,"end":59,"cssClass":"pl-s"},{"start":61,"end":68,"cssClass":"pl-s"},{"start":70,"end":78,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":11,"cssClass":"pl-en"},{"start":12,"end":16,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":20,"cssClass":"pl-s"}],[{"start":0,"end":44,"cssClass":"pl-s"}],[{"start":0,"end":37,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":29,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":11,"cssClass":"pl-en"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":18,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":20,"cssClass":"pl-s"}],[{"start":0,"end":45,"cssClass":"pl-s"}],[{"start":0,"end":33,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":46,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":18,"end":21,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-c1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":22,"cssClass":"pl-s1"},{"start":23,"end":32,"cssClass":"pl-s1"},{"start":33,"end":41,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":44,"end":47,"cssClass":"pl-s"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":50,"end":53,"cssClass":"pl-s1"},{"start":54,"end":56,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":26,"cssClass":"pl-s1"},{"start":27,"end":31,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":35,"end":38,"cssClass":"pl-s1"}],[{"start":12,"end":23,"cssClass":"pl-v"},{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":37,"cssClass":"pl-s1"},{"start":38,"end":47,"cssClass":"pl-s1"},{"start":48,"end":56,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":36,"cssClass":"pl-s"}],[{"start":0,"end":36,"cssClass":"pl-s"}],[{"start":0,"end":36,"cssClass":"pl-s"}],[{"start":0,"end":20,"cssClass":"pl-s"}],[{"start":0,"end":49,"cssClass":"pl-s"}],[{"start":0,"end":52,"cssClass":"pl-s"}],[{"start":0,"end":28,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[],[{"start":8,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"}],[],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":14,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":18,"end":22,"cssClass":"pl-s1"},{"start":23,"end":32,"cssClass":"pl-s1"}],[{"start":12,"end":24,"cssClass":"pl-s1"},{"start":25,"end":27,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":31,"end":35,"cssClass":"pl-s1"},{"start":36,"end":45,"cssClass":"pl-s1"},{"start":46,"end":48,"cssClass":"pl-s1"},{"start":50,"end":57,"cssClass":"pl-en"}],[],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":17,"cssClass":"pl-en"},{"start":18,"end":22,"cssClass":"pl-s1"},{"start":23,"end":34,"cssClass":"pl-s1"},{"start":36,"end":39,"cssClass":"pl-s"},{"start":41,"end":43,"cssClass":"pl-k"},{"start":44,"end":49,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":21,"cssClass":"pl-en"},{"start":22,"end":34,"cssClass":"pl-s1"},{"start":36,"end":41,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":20,"cssClass":"pl-s"}],[{"start":0,"end":46,"cssClass":"pl-s"}],[{"start":0,"end":45,"cssClass":"pl-s"}],[{"start":0,"end":48,"cssClass":"pl-s"}],[{"start":0,"end":23,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[],[{"start":8,"end":11,"cssClass":"pl-k"}],[{"start":12,"end":16,"cssClass":"pl-k"},{"start":17,"end":21,"cssClass":"pl-en"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":38,"cssClass":"pl-s1"},{"start":40,"end":43,"cssClass":"pl-s"},{"start":45,"end":47,"cssClass":"pl-k"},{"start":48,"end":50,"cssClass":"pl-s1"}],[{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":29,"cssClass":"pl-en"},{"start":30,"end":32,"cssClass":"pl-s1"}],[],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-s1"},{"start":23,"end":27,"cssClass":"pl-en"}],[{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":30,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":36,"end":43,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-s1"},{"start":49,"end":60,"cssClass":"pl-s"},{"start":63,"end":65,"cssClass":"pl-c1"},{"start":65,"end":66,"cssClass":"pl-s1"},{"start":67,"end":68,"cssClass":"pl-s1"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":32,"cssClass":"pl-v"}],[{"start":12,"end":16,"cssClass":"pl-k"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/mahdizaabi/AirBnB_clone/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/mahdizaabi/AirBnB_clone/security/dependabot","repoSecurityAndAnalysisPath":"/mahdizaabi/AirBnB_clone/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"file_storage.py","displayUrl":"https://github.com/mahdizaabi/AirBnB_clone/blob/master/models/engine/file_storage.py?raw=true","headerInfo":{"blobSize":"2.94 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"1596fae","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fmahdizaabi%2FAirBnB_clone%2Fblob%2Fmaster%2Fmodels%2Fengine%2Ffile_storage.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"112","truncatedSloc":"94"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/mahdizaabi/AirBnB_clone/discussions/new","newIssuePath":"/mahdizaabi/AirBnB_clone/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/mahdizaabi/AirBnB_clone/blob/master/models/engine/file_storage.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/mahdizaabi/AirBnB_clone/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/mahdizaabi/AirBnB_clone/raw/master/models/engine/file_storage.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"mahdizaabi","repoName":"AirBnB_clone","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"classes","kind":"constant","identStart":305,"identEnd":312,"extentStart":305,"extentEnd":448,"fullyQualifiedName":"classes","identUtf16":{"start":{"lineNumber":14,"utf16Col":0},"end":{"lineNumber":14,"utf16Col":7}},"extentUtf16":{"start":{"lineNumber":14,"utf16Col":0},"end":{"lineNumber":15,"utf16Col":74}}},{"name":"FileStorage","kind":"class","identStart":457,"identEnd":468,"extentStart":451,"extentEnd":3011,"fullyQualifiedName":"FileStorage","identUtf16":{"start":{"lineNumber":18,"utf16Col":6},"end":{"lineNumber":18,"utf16Col":17}},"extentUtf16":{"start":{"lineNumber":18,"utf16Col":0},"end":{"lineNumber":111,"utf16Col":16}}},{"name":"__file_path","kind":"constant","identStart":710,"identEnd":721,"extentStart":710,"extentEnd":735,"fullyQualifiedName":"FileStorage.__file_path","identUtf16":{"start":{"lineNumber":30,"utf16Col":4},"end":{"lineNumber":30,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":30,"utf16Col":4},"end":{"lineNumber":30,"utf16Col":29}}},{"name":"__objects","kind":"constant","identStart":778,"identEnd":787,"extentStart":778,"extentEnd":792,"fullyQualifiedName":"FileStorage.__objects","identUtf16":{"start":{"lineNumber":32,"utf16Col":4},"end":{"lineNumber":32,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":32,"utf16Col":4},"end":{"lineNumber":32,"utf16Col":18}}},{"name":"kryptix","kind":"constant","identStart":798,"identEnd":805,"extentStart":798,"extentEnd":810,"fullyQualifiedName":"FileStorage.kryptix","identUtf16":{"start":{"lineNumber":34,"utf16Col":4},"end":{"lineNumber":34,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":34,"utf16Col":4},"end":{"lineNumber":34,"utf16Col":16}}},{"name":"cll","kind":"constant","identStart":815,"identEnd":818,"extentStart":815,"extentEnd":875,"fullyQualifiedName":"FileStorage.cll","identUtf16":{"start":{"lineNumber":35,"utf16Col":4},"end":{"lineNumber":35,"utf16Col":7}},"extentUtf16":{"start":{"lineNumber":35,"utf16Col":4},"end":{"lineNumber":35,"utf16Col":64}}},{"name":"strx","kind":"constant","identStart":880,"identEnd":884,"extentStart":880,"extentEnd":955,"fullyQualifiedName":"FileStorage.strx","identUtf16":{"start":{"lineNumber":36,"utf16Col":4},"end":{"lineNumber":36,"utf16Col":8}},"extentUtf16":{"start":{"lineNumber":36,"utf16Col":4},"end":{"lineNumber":36,"utf16Col":79}}},{"name":"all","kind":"function","identStart":965,"identEnd":968,"extentStart":961,"extentEnd":1292,"fullyQualifiedName":"FileStorage.all","identUtf16":{"start":{"lineNumber":38,"utf16Col":8},"end":{"lineNumber":38,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":38,"utf16Col":4},"end":{"lineNumber":50,"utf16Col":29}}},{"name":"new","kind":"function","identStart":1302,"identEnd":1305,"extentStart":1298,"extentEnd":1829,"fullyQualifiedName":"FileStorage.new","identUtf16":{"start":{"lineNumber":52,"utf16Col":8},"end":{"lineNumber":52,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":52,"utf16Col":4},"end":{"lineNumber":68,"utf16Col":56}}},{"name":"save","kind":"function","identStart":1839,"identEnd":1843,"extentStart":1835,"extentEnd":2405,"fullyQualifiedName":"FileStorage.save","identUtf16":{"start":{"lineNumber":70,"utf16Col":8},"end":{"lineNumber":70,"utf16Col":12}},"extentUtf16":{"start":{"lineNumber":70,"utf16Col":4},"end":{"lineNumber":89,"utf16Col":42}}},{"name":"reload","kind":"function","identStart":2415,"identEnd":2421,"extentStart":2411,"extentEnd":3011,"fullyQualifiedName":"FileStorage.reload","identUtf16":{"start":{"lineNumber":91,"utf16Col":8},"end":{"lineNumber":91,"utf16Col":14}},"extentUtf16":{"start":{"lineNumber":91,"utf16Col":4},"end":{"lineNumber":111,"utf16Col":16}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/mahdizaabi/AirBnB_clone/branches":{"post":"zpmR79WiV4aJeqKqYmqyQg_VODMQFwKbW2jDOaAAn7q9nH8IQfvo14mfFj3Mvm_MgMHIykoKFJhnfVyM4WhKtw"},"/repos/preferences":{"post":"SgucFFR2ZvTsK7-gA4SpKntVNZ2A1Bxq90xWMvINTgizTz229ps91L4xs1tM4RfVV2rwwJdOd2j-hpgAJ6M_9w"}}},"title":"AirBnB_clone/models/engine/file_storage.py at master · mahdizaabi/AirBnB_clone"}
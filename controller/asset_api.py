import gazu

class AssetAPI:
    __project = None
    __sequence = None
    __shot = None
    __asset = None
    __task_type = None
    __task = None
    __entity = None

    def __init__(self):
        gazu.client.set_host("http://192.168.3.117/api")
        gazu.log_in("admin@netflixacademy.com", "netflixacademy")

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, name):
        self.__project = gazu.project.get_project_by_name(name)

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, name):
        self.__sequence = gazu.shot.get_sequence_by_name(self.project, name)

    @property
    def shot(self):
        return self.__shot

    @shot.setter
    def shot(self, name):
        self.__shot = gazu.shot.get_shot_by_name(self.sequence, name)
        self.__entity = self.__shot

    @property
    def asset(self):
        return self.__asset

    @asset.setter
    def asset(self, name):
        self.__asset = gazu.asset.get_asset_by_name(self.project, name)
        self.__entity = self.__asset

    def get_all_task(self):
        return gazu.user.all_tasks_to_do()

    # 프로젝트를 파라미터로 받아 해당 프로젝트의 모든 에셋들을 반환한다
    def get_all_asset_by_project(self, project_dict):
        __project = project_dict
        return gazu.asset.all_assets_for_project(project_dict)

    # asset을 파라미터로 받아 해당 어셋 타입 이름을 반환한다
    def get_asset_type_name(self, asset_dict):
        # asset_type의 name은 따로 가져와야한다, asset을 가져오면 'entity_type_id'를 얻을 수 있는데 이를 활용한다
        # gazu API의 asset 관련 메서드 중 get_asset_type()에 'entity_type_id'를 파라미터로 넘겨준다
        # 얻은 asset_type의 'name' key를 이용하여 asset_type name을 가져온다
        asset_type = gazu.asset.get_asset_type(asset_dict['entity_type_id'])
        asset_type_name = asset_type['name']
        return asset_type_name

    def create_asset(self, project_name, asset_type_name, asset_name):
        project = gazu.project.get_project_by_name(project_name)
        asset_type = gazu.asset.get_asset_type_by_name(asset_type_name)
        # print(project)
        # print(type(asset_type))

        asset = gazu.asset.new_asset(
            project,
            asset_type,
            asset_name,
            "My asset description"
        )

    def delete_asset(self, asset_name):
        asset = gazu.asset.get_asset_by_name(self.project, asset_name)
        gazu.asset.remove_asset(asset)

    def update_asset(self):
        pass
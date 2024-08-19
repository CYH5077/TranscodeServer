from dataclasses import dataclass, asdict

import yaml


@dataclass
class Config:
    redis_url: str


class TranscodeServerConfig:
    def __init__(self):
        self.config = Config(redis_url="redis://localhost:5000")
        pass

    def load_config(self, file_path: str = "./config.yaml"):
        try:
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)
            self.config.redis_url = data['redis_url']

        except Exception as e:
            # 기본 설정파일을 생성한다.
            self.config.redis_url = "redis://localhost:5000"
            with open(file_path, 'w', encoding='utf-8') as file:
                yaml.safe_dump(asdict(self.config), file)
            print(f"Generate default config file: {file_path}")
            raise e

    def get_redis_url(self) -> str:
        return self.config.redis_url

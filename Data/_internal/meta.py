from typing import Dict, Any, Type

class DataMeta(type):
    """Metaclass to process configuration arguments at class definition time."""
    def __new__(mcs, name: str, bases: tuple[Type, ...], namespace: Dict[str, Any], **kwargs: Any) -> Type:
        config_args = kwargs.pop('config', {})
        config_args.update(kwargs)
        new_cls = super().__new__(mcs, name, bases, namespace)
        new_cls._config = config_args 
        return new_cls
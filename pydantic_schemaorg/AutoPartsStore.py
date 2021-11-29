from pydantic import Field
from pydantic_schemaorg.Store import Store
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoPartsStore(Store, AutomotiveBusiness):
    """An auto parts store.

    See https://schema.org/AutoPartsStore.

    """

    locals().update({"@type": Field("AutoPartsStore", const=True)})


AutoPartsStore.update_forward_refs()
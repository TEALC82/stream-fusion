from fastapi.exceptions import HTTPException

from stream_fusion.utils.debrid.alldebrid import AllDebrid
from stream_fusion.utils.debrid.premiumize import Premiumize
from stream_fusion.utils.debrid.realdebrid import RealDebrid
from stream_fusion.utils.debrid.torbox import TorBox


def get_debrid_service(config):
    service_name = config['service']
    if service_name == "Real-Debrid":
        debrid_service = RealDebrid(config)
    elif service_name == "AllDebrid":
        debrid_service = AllDebrid(config)
    elif service_name == "Premiumize":
        debrid_service = Premiumize(config)
    elif service_name == "TorBox":
        debrid_service = TorBox(config)
    else:
        raise HTTPException(status_code=500, detail="Invalid service configuration.")

    return debrid_service

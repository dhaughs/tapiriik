from .service_base import *
from .api import *
from tapiriik.services.RunKeeper import RunKeeperService
RunKeeper = RunKeeperService()
from tapiriik.services.Strava import StravaService
Strava = StravaService()
from tapiriik.services.Endomondo import EndomondoService
Endomondo = EndomondoService()
from tapiriik.services.Dropbox import DropboxService
Dropbox = DropboxService()
from tapiriik.services.GarminConnect import GarminConnectService
GarminConnect = GarminConnectService()
from tapiriik.services.SportTracks import SportTracksService
SportTracks = SportTracksService()
from tapiriik.services.RideWithGPS import RideWithGPSService
RideWithGPS = RideWithGPSService()
from tapiriik.services.TrainingPeaks import TrainingPeaksService
TrainingPeaks = TrainingPeaksService()
from tapiriik.services.Motivato import MotivatoService
Motivato = MotivatoService()

PRIVATE_SERVICES = []
try:
    from private.tapiriik.services import *
except ImportError:
    pass

from .service import *
from .service_record import *

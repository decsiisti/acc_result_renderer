from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Driver:
    firstName: str
    lastName: str
    playerId: str
    shortName: str

    @staticmethod
    def from_dict(obj: Any) -> 'Driver':
        _firstName = str(obj.get("firstName"))
        _lastName = str(obj.get("lastName"))
        _playerId = str(obj.get("playerId"))
        _shortName = str(obj.get("shortName"))
        return Driver(_firstName, _lastName, _playerId, _shortName)

@dataclass
class Car:
    carId: int
    carModel: int
    cupCategory: int
    drivers: List[Driver]
    nationality: int
    raceNumber: int
    teamName: str

    @staticmethod
    def from_dict(obj: Any) -> 'Car':
        _carId = int(obj.get("carId"))
        _carModel = int(obj.get("carModel"))
        _cupCategory = int(obj.get("cupCategory"))
        _drivers = [Driver.from_dict(y) for y in obj.get("drivers")]
        _nationality = int(obj.get("nationality"))
        _raceNumber = int(obj.get("raceNumber"))
        _teamName = str(obj.get("teamName"))
        return Car(_carId, _carModel, _cupCategory, _drivers, _nationality, _raceNumber, _teamName)

@dataclass
class CurrentDriver:
    firstName: str
    lastName: str
    playerId: str
    shortName: str

    @staticmethod
    def from_dict(obj: Any) -> 'CurrentDriver':
        _firstName = str(obj.get("firstName"))
        _lastName = str(obj.get("lastName"))
        _playerId = str(obj.get("playerId"))
        _shortName = str(obj.get("shortName"))
        return CurrentDriver(_firstName, _lastName, _playerId, _shortName)

@dataclass
class Lap:
    carId: int
    driverIndex: int
    isValidForBest: bool
    laptime: int
    splits: List[int]

    @staticmethod
    def from_dict(obj: Any) -> 'Lap':
        _carId = int(obj.get("carId"))
        _driverIndex = int(obj.get("driverIndex"))
        _isValidForBest = bool(obj.get("isValidForBest"))
        _laptime = int(obj.get("laptime"))
        _splits = [obj.get("splits")]
        return Lap(_carId, _driverIndex, _isValidForBest, _laptime, _splits)

@dataclass
class Timing:
    bestLap: int
    bestSplits: List[int]
    lapCount: int
    lastLap: int
    lastSplitId: int
    lastSplits: List[int]
    totalTime: int

    @staticmethod
    def from_dict(obj: Any) -> 'Timing':
        _bestLap = int(obj.get("bestLap"))
        _bestSplits = [obj.get("bestSplits")]
        _lapCount = int(obj.get("lapCount"))
        _lastLap = int(obj.get("lastLap"))
        _lastSplitId = int(obj.get("lastSplitId"))
        _lastSplits = [obj.get("lastSplits")]
        _totalTime = int(obj.get("totalTime"))
        return Timing(_bestLap, _bestSplits, _lapCount, _lastLap, _lastSplitId, _lastSplits, _totalTime)

@dataclass
class LeaderBoardLine:
    car: Car
    currentDriver: CurrentDriver
    currentDriverIndex: int
    driverTotalTimes: List[float]
    missingMandatoryPitstop: int
    timing: Timing

    @staticmethod
    def from_dict(obj: Any) -> 'LeaderBoardLine':
        _car = Car.from_dict(obj.get("car"))
        _currentDriver = CurrentDriver.from_dict(obj.get("currentDriver"))
        _currentDriverIndex = int(obj.get("currentDriverIndex"))
        _driverTotalTimes = [obj.get("driverTotalTimes")]
        _missingMandatoryPitstop = int(obj.get("missingMandatoryPitstop"))
        _timing = Timing.from_dict(obj.get("timing"))
        return LeaderBoardLine(_car, _currentDriver, _currentDriverIndex, _driverTotalTimes, _missingMandatoryPitstop, _timing)

@dataclass
class Penalty:
    carId: int
    clearedInLap: int
    driverIndex: int
    penalty: str
    penaltyValue: int
    reason: str
    violationInLap: int

    @staticmethod
    def from_dict(obj: Any) -> 'Penalty':
        _carId = int(obj.get("carId"))
        _clearedInLap = int(obj.get("clearedInLap"))
        _driverIndex = int(obj.get("driverIndex"))
        _penalty = str(obj.get("penalty"))
        _penaltyValue = int(obj.get("penaltyValue"))
        _reason = str(obj.get("reason"))
        _violationInLap = int(obj.get("violationInLap"))
        return Penalty(_carId, _clearedInLap, _driverIndex, _penalty, _penaltyValue, _reason, _violationInLap)

@dataclass
class SessionResult:
    bestSplits: List[int]
    bestlap: int
    isWetSession: int
    leaderBoardLines: List[LeaderBoardLine]
    type: int

    @staticmethod
    def from_dict(obj: Any) -> 'SessionResult':
        _bestSplits = [obj.get("bestSplits")]
        _bestlap = int(obj.get("bestlap"))
        _isWetSession = int(obj.get("isWetSession"))
        _leaderBoardLines = [LeaderBoardLine.from_dict(y) for y in obj.get("leaderBoardLines")]
        _type = int(obj.get("type"))
        return SessionResult(_bestSplits, _bestlap, _isWetSession, _leaderBoardLines, _type)

@dataclass
class AccResult:
    laps: List[Lap]
    penalties: List[Penalty]
    sessionIndex: int
    sessionResult: SessionResult
    sessionType: str
    trackName: str
    metaData: str
    Date: str
    SessionFile: str

    @staticmethod
    def from_dict(obj: Any) -> 'AccResult':
        _laps = [Lap.from_dict(y) for y in obj.get("laps")]
        _penalties = [Penalty.from_dict(y) for y in obj.get("penalties")]
        _sessionIndex = int(obj.get("sessionIndex"))
        _sessionResult = SessionResult.from_dict(obj.get("sessionResult"))
        _sessionType = str(obj.get("sessionType"))
        _trackName = str(obj.get("trackName"))
        _metaData = str(obj.get("metaData"))
        _Date = str(obj.get("Date"))
        _SessionFile = str(obj.get("SessionFile"))
        return AccResult(_laps, _penalties, _sessionIndex, _sessionResult, _sessionType, _trackName, _metaData, _Date, _SessionFile)
    
    
    def carModelToString(self, carModel):
        match carModel:
            case 8:
                return "Bentley Continental GT3 (2018)"
            case 25:
                return "Mercedes-AMG GT3 2020"
            case 30:
                return "BMW M4 GT3"
            case 32:
                return "Ferrari 296 GT3"
            case 33:
                return "Lamborghini Huracan Evo2"
            case 34:
                return "Porsche 992 GT3 R"
            case _:
                return "Batmobile"
    
    def getResultTable(self):
        table = []
        i = 1
        for lbl in self.sessionResult.leaderBoardLines:
            table.append([i, lbl.currentDriver.firstName + " " + lbl.currentDriver.lastName, self.carModelToString(lbl.car.carModel)])
            i+=1
        return table
import BigWorld
from gui.Scaleform.Battle import Battle
import datetime

print 'STATA mod started '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

def BF_new_afterCreate(self):
    BF_orig_afterCreate(self)
    f = open('c:\games\list_gamers.txt', 'a')
    print 'Battle starts '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print self
    f.write('Battle starts '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+'\n')
    print BigWorld.player().name
    print BigWorld.player()
    for pl in BigWorld.player().arena.vehicles.values():
        print pl
#        print self
        f.write(pl['name'])
        f.write(' ')
        f.write('\n')
    f.close() 

BF_orig_afterCreate = Battle.afterCreate
Battle.afterCreate = BF_new_afterCreate

#---------------------------------------------------------------------------
from Vehicle import Vehicle
old_onHealthChanged = Vehicle.onHealthChanged

def new_onHealthChanged(self, newHealth, attackerID, attackReasonID):
    old_onHealthChanged(self, newHealth, attackerID, attackReasonID)
    print self
    print 'Damaga '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+ ' newHealth:'+str(newHealth)+' attackerID:'+str(attackerID)+ '   tot kto otgreb self.id:'+str(self.id)+'   attackReasonID:'+str(attackReasonID)

old_onHealthChanged = Vehicle.onHealthChanged
Vehicle.onHealthChanged = new_onHealthChanged


#---------------------------------------------------------------------------
from gui.battle_control.battle_msgs_ctrl import BattleMessagesController
old_BattleMessagesController_showVehicleKilledMessage = BattleMessagesController.showVehicleKilledMessage

def new_showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
    old_BattleMessagesController_showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason)
    print self
    print 'Kill '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+ ' targetID:'+str(targetID)+' attackerID:'+str(attackerID)+'   reason:'+str(reason) + '  equipmentID:'+str(equipmentID)

BattleMessagesController.showVehicleKilledMessage = new_showVehicleKilledMessage    
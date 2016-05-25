import BigWorld
from gui.Scaleform.Battle import Battle
import datetime

f = open('gamelog.txt', 'a')
print 'STATA mod started '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
f.close() 

def BF_new_afterCreate(self):
    BF_orig_afterCreate(self)
    f = open('gamelog.txt', 'a')
    f.write('Battle starts '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+'\n')
    f.write( 'I am '+BigWorld.player().name +'\n')
    print BigWorld.player()
    for pl in BigWorld.player().arena.vehicles.values():
        f.write(pl['name']+' '+pl['accountDBID']+'\n')
    f.close() 

BF_orig_afterCreate = Battle.afterCreate
Battle.afterCreate = BF_new_afterCreate

#---------------------------------------------------------------------------
from gui.battle_control import g_sessionProvider
from Vehicle import Vehicle
old_onHealthChanged = Vehicle.onHealthChanged
def new_onHealthChanged(self, newHealth, attackerID, attackReasonID):
    old_onHealthChanged(self, newHealth, attackerID, attackReasonID)
    EnemyVihInfo = BigWorld.player().arena.vehicles.get(self.id)
    nameWHOdamage = g_sessionProvider.getCtx().getFullPlayerName(attackerID, showClan=False)
    f = open('gamelog.txt', 'a')
    f.write ('Damaga '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+ 
    ' Player '+nameWHOdamage + ' kicked '+ EnemyVihInfo['name']+' and he has ' +str(newHealth)+' hp left')
    f.close() 
old_onHealthChanged = Vehicle.onHealthChanged
Vehicle.onHealthChanged = new_onHealthChanged


#---------------------------------------------------------------------------
#from gui.battle_control.battle_msgs_ctrl import BattleMessagesController
#old_BattleMessagesController_showVehicleKilledMessage = BattleMessagesController.showVehicleKilledMessage

#def new_showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
#    old_BattleMessagesController_showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason)
#    print self
#    print 'Kill '+datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+ ' targetID:'+str(targetID)+' attackerID:'+str(attackerID)+'   reason:'+str(reason) + '  equipmentID:'+str(equipmentID)
#BattleMessagesController.showVehicleKilledMessage = new_showVehicleKilledMessage    
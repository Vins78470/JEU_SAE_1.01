
import unittest
from Rules import *
from Game import Game
from Mission import *
from Coder import *
# coding: utf-8


class TestRules(unittest.TestCase):
    
    def test_check_nombre_coder_valid(self):
        self.assertEqual(CheckNombreCoder(1), True)
        self.assertEqual(CheckNombreCoder(4), True)

    def test_check_nombre_coder_invalid(self):
        self.assertEqual(CheckNombreCoder(0), False)
        self.assertEqual(CheckNombreCoder(5), False)

    def test_check_level_choice_valid(self):
        self.assertEqual(CheckLevelChoice("facile"), True)
        self.assertEqual(CheckLevelChoice("intermediaire"), True)
        self.assertEqual(CheckLevelChoice("difficile"), True)

    def test_check_level_choice_invalid(self):
        self.assertEqual(CheckLevelChoice("trop_facile"), False)
        self.assertEqual(CheckLevelChoice("dur"), False)


        

class TestCoderMethods(unittest.TestCase):

    def setUp(self):
        # Initialisation d'un objet Coder pour les tests
        self.coder = Coder('C', (2, 2), 5, 10, 5, 100, 'blue')

    def test_GetSymbol(self):
        self.assertEqual(self.coder.GetSymbol(), 'C')

    def test_GetPosition(self):
        self.assertEqual(self.coder.GetPosition(), (2, 2))

    def test_GetCodingLevel(self):
        self.assertEqual(self.coder.GetCodingLevel(), 5)

    def test_GetEnergyMax(self):
        self.assertEqual(self.coder.GetEnergyMax(), 10)

    def test_GetEnergy(self):
        self.assertEqual(self.coder.GetEnergy(), 5)

    def test_GetMoneyAmount(self):
        self.assertEqual(self.coder.GetMoneyAmount(), 100)

    def test_ResetEnergy(self):
        self.coder.ResetEnergy()
        self.assertEqual(self.coder.GetEnergy(), 10)  # V�rifie si l'�nergie est remise � sa valeur maximale

    def test_ChangePosition(self):
        self.coder.ChangePosition((1, 1))
        self.assertEqual(self.coder.GetPosition(), (1, 1))

    def test_UpgradeCodingLevel(self):
        self.coder.UpgradeCodingLevel()
        self.assertEqual(self.coder.GetCodingLevel(), 6)

    def test_UpgradeEnergyMax(self):
        self.coder.UpgradeEnergyMax()
        self.assertEqual(self.coder.GetEnergyMax(), 10)

    def test_UpgradeMoneyAmount(self):
        self.coder.UpgradeMoneyAmount(50)
        self.assertEqual(self.coder.GetMoneyAmount(), 150)
    
    def test_UpgradeEnergy(self):
        self.coder.UpgradeEnergy(5)
        self.assertEqual(self.coder.GetEnergy(), 10)
    
    def test_UpgradeEnergy(self):
        self.coder.UpgradeEnergy(-5)
        self.assertEqual(self.coder.GetEnergy(), 0)        
        
    def test_UpgradeEnergy(self):
        self.coder.UpgradeEnergy(3)
        self.assertEqual(self.coder.GetEnergy(), 8)

    def test_ResetEnergy(self):
        self.coder.ResetEnergy()
        self.assertEqual(self.coder.GetEnergy(), self.coder.GetEnergyMax())

    def test_ChangePosition(self):
        self.coder.ChangePosition((5, 5))
        self.assertEqual(self.coder.GetPosition(), (5, 5))

   
    def test_UpgradeCodingLevel(self):
        self.coder.UpgradeCodingLevel()
        self.assertEqual(self.coder.GetCodingLevel(), 6)

    def test_UpgradeEnergyMax(self):
        self.coder.UpgradeEnergyMax()
        self.assertEqual(self.coder.GetEnergyMax(), 10)

    def test_UpgradeEnergy(self):
        self.coder.UpgradeEnergy(-15)
        self.assertEqual(self.coder.GetEnergy(), 0)

    def test_UpgradeMoneyAmount(self):
        self.coder.UpgradeMoneyAmount(-600)
        self.assertEqual(self.coder.GetMoneyAmount(), 100)



# Test pour les missions
class TestMission(unittest.TestCase):
    
    def setUp(self):
        self.mission = Mission("M1", 10, 5, (5, 5))

    def test_GetSymbol(self):
        self.assertEqual(self.mission.GetSymbol(), "M1")

    def test_GetPosition(self):
        self.assertEqual(self.mission.GetPosition(), (5, 5))

    def test_GetStartingWorkLoad(self):
        self.assertEqual(self.mission.GetStartingWorkLoad(), 10)

    def test_GetRemainingWorkLoad(self):
        self.assertEqual(self.mission.GetRemainingWorkLoad(), 10)

    def test_GetDifficulty(self):
        self.assertEqual(self.mission.GetDifficulty(), 5)

    def test_RendreIndisponible(self):
        self.mission.rendre_indisponible(3)
        self.assertFalse(self.mission.est_disponible())

    def test_EstIndisponible(self):
        self.assertFalse(self.mission.est_indisponible())

    def test_DecrementerIndisponibilite(self):
        self.mission.rendre_indisponible(3)
        self.mission.decrementer_indisponibilite()
        self.assertEqual(self.mission.indisponible_round, 2)

    def test_RedrawAfterMissionNotAvailable(self):
        Board = [["  " for _ in range(10)] for _ in range(10)]
        self.mission.rendre_indisponible(3)
        self.mission.RedrawAfterMissionNotAvailable(Board)
        self.assertEqual(Board[5][5], "M1")

    def test_ResetValues(self):
        self.mission.rendre_indisponible(3)
        self.mission.ResetValues()
        self.assertEqual(self.mission.GetSymbol(), "M1")
        self.assertEqual(self.mission.GetStartingWorkLoad(), 10)
        self.assertEqual(self.mission.GetRemainingWorkLoad(), 10)
        self.assertEqual(self.mission.GetDifficulty(), 5)
        self.assertEqual(self.mission.GetPosition(), (5, 5))

    def test_UpgradeRemainingWorkLoad(self):
        self.mission.UpgradeRemainingWorkLoad(3)
        self.assertEqual(self.mission.GetRemainingWorkLoad(), 13)

    def test_ResetRemainingWorkLoad(self):
        self.mission.ResetRemainingWorkLoad()
        self.assertEqual(self.mission.GetRemainingWorkLoad(), 0)



class TestCoderActions(unittest.TestCase):

    def setUp(self):
        # Initialisation d'un objet Coder pour les tests
        self.coder = Coder('C', (0, 0), 3, 10, 8, 200, 'blue')

    def test_CoutDepenseArgentAuJobCenterPourEnergyMax_valid(self):
        self.assertFalse(CoutDepenseArgentAuJobCenterPourEnergyMax(self.coder))
     

    def test_CoutDepenseArgentAujobCenterPourCodingLevel_valid(self):
    
        CoutDepenseArgentAujobCenterPourCodingLevel(self.coder)
        self.assertEqual(self.coder.GetCodingLevel(), 4)  # V�rifie si le niveau de codage a augment�
        
    def test_UpgradeCodingLevel(self):
            # V�rifie si le niveau de codage augmente de 1
            self.coder.UpgradeCodingLevel()
            self.assertEqual(self.coder.GetCodingLevel(), 4)

    def test_UpgradeCodingLevel_multiple_times(self):
        # V�rifie si le niveau de codage augmente plusieurs fois
        for i in range(5):
            self.coder.UpgradeCodingLevel()
        self.assertEqual(self.coder.GetCodingLevel(), 8) 

    def test_UpgradeCodingLevel_max_limit(self):
        # V�rifie si le niveau de codage atteint la limite maximale
        for i in range(20):
            self.coder.UpgradeCodingLevel()
        self.assertEqual(self.coder.GetCodingLevel(), 10)  # Limite maximale : 10

    def test_CoutDepenseArgentAujobCenterPourCodingLevel_valid_multiple_times(self):
        # V�rifie si le niveau de codage augmente de 1 apr�s avoir d�pens� de l'argent
        CoutDepenseArgentAujobCenterPourCodingLevel(self.coder)
        self.assertEqual(self.coder.GetCodingLevel(), 4)

    def test_CoutDepenseArgentAujobCenterPourCodingLevel_invalid(self):
        # V�rifie si le niveau de codage reste le m�me en cas d'insuffisance d'argent
        self.coder.UpgradeMoneyAmount(-200)  # R�duit l'argent pour simuler l'insuffisance
        CoutDepenseArgentAujobCenterPourCodingLevel(self.coder)
        self.assertEqual(self.coder.GetCodingLevel(), 7)  # Le niveau de codage reste � 7


    def test_CoutDepenseArgentAuJobCenterPourEnergyMax_invalid(self):
        # Simuler le manque d'argent pour augmenter l'�nergie maximale
        self.coder.UpgradeMoneyAmount(-150)  # Abaisser le montant d'argent pour simuler le manque
        self.assertFalse(CoutDepenseArgentAuJobCenterPourEnergyMax(self.coder))
        self.assertEqual(self.coder.GetEnergyMax(), 10)  # V�rifie si l'�nergie maximale est rest�e la m�me

    def test_CoutDepenseArgentAujobCenterPourCodingLevel_invalid(self):
        # Simuler le manque d'argent pour augmenter le niveau de codage
        self.coder.UpgradeMoneyAmount(-160)  # Abaisser le montant d'argent pour simuler le manque
        CoutDepenseArgentAujobCenterPourCodingLevel(self.coder)
        self.assertEqual(self.coder.GetCodingLevel(), 3)  # Verifie si le niveau de codage est rest� le m�me





unittest.main()




class Test(unittest.TestCase):

  def test_predecir_respuesta_20(self):
    self.assertEquals(predecir_respuesta(20), 85.05642088787117, 0.5)
    
  def test_predecir_respuesta_30(self):
    self.assertEquals(predecir_respuesta(30), 190.17295167042818, 0.5)
    
  def test_predecir_respuesta_15(self):
    self.assertEquals(predecir_respuesta(15), 32.49815549659269, 0.5)    
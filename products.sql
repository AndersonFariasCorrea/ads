CREATE TABLE store.products (
  cod_prod INT NOT NULL AUTO_INCREMENT,
  nome_prod TEXT NOT NULL,
  quant_prod INT NOT NULL,
  unit_value FLOAT NOT NULL,
  situation_prod TINYINT NOT NULL,
  PRIMARY KEY (cod_prod)
) ENGINE = InnoDB;
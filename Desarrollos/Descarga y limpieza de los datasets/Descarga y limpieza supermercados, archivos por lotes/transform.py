import pandas as pd
from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import operator
from datetime import datetime
from datetime import timedelta
import unidecode

def transform(food) -> pd.DataFrame:
    """Gets pandas dataframe and returns it transformed

    Args:
        food (DataFrame)

    Return:
        DataFrame
    """
    blacklist = ['cocina','basura','detergente','electrodomestico','corporal','higienico','limpieza', 'jardineria',
    'casa', 'hogar', 'cuidado', 'cabello', 'bebe',
    'perfumeria', 'mascota', 'parafarmacia', 'farmacia', 'maquillaje','drogueria','soy_solidario','perfumeria_e_higiene_cuidado_facial_hidratantes_y_nutritivas','perfumeria_e_higiene_cuidado_facial_antiarrugas_y_antiedad',
    'perfumeria_e_higiene_cuidado_facial_mascarillas','perfumeria_e_higiene_cuidado_corporal_anticeluliticos','perfumeria_e_higiene_cuidado_corporal_cremas_cuerpo__body_milk',
    'bebe_higiene_champu','bebe_higiene_colonia_infantil','bebe_higiene_cremas_y_lociones',
    'perfumeria_e_higiene_botiquin_gel_higienizante_y_mascarillas','perfumeria_e_higiene_colonias_masculinas',
    'perfumeria_e_higiene_colonias_femeninas','perfumeia_e_higiene_colonias_familiar','perfumeria_e_higiene_desodorante_roll_on','perfumeria_e_higiene_cuidado_del_cabello_champu',
    'perfumeria_e_higiene_cuidado_del_cabello_acondicionador_y_suavizante','perfumeria_e_higiene_cuidado_del_cabello_mascarillas_cabello',
    'perfumeria_e_higiene_cuidado_del_cabello_laca_espuma_y_fijadores','perfumeria_e_higiene_desodorante_spray',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_fregasuelos','drogueria_y_limpieza_limpiadores_para_el_hogar_abrillantador_suelos',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_desatascador_limpia_tuberias','drogueria_y_limpieza_limpiadores_para_el_hogar_limpiador_multiusos',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_limpia_vitroceramica','drogueria_y_limpieza_limpiadores_para_el_hogar_antical',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_limpia_banos','drogueria_y_limpieza_lavavajillas_a_mano',
    'perfumeria_e_higiene_higiene_bucal_dentifricos','perfumeria_e_higiene_gel_de_bano_gel_de_bano','perfumeria_e_higiene_depilacion_crema_gel_y_spray',
    'perfumeria_e_higiene_cuidado_manos_jabon_de_manos_liquido','perfumeria_e_higiene_cuidado_manos_crema_de_manos',
    'perfumeria_e_higiene_limpieza_facial_exfoliante','perfumeria_e_higiene_limpieza_facial_limpieza_desmaquilladores','perfumeria_e_higiene_limpieza_facial_leche_y_tonicos_limpiadores',
    'perfumeria_e_higiene_cuidado_corporal_aceite','mascotas_gatos_alimento_humedo','mascotas_gatos_alimento_seco','mascotas_perros_alimento_humedo',
    'mascotas_perros_alimento_seco','mascotas_perros_snacks','mascotas_resto_animales_alimento_pajaros',
    'mascotas_resto_animales_alimento_peces_tortugas','limpieza_y_hogar_lejia_y_liquidos_fuertes','limpieza_y_hogar_limpiacristales',
    'limpieza_y_hogar_limpieza_muebles_y_multiusos','limpieza_y_hogar_limpieza_vajilla','limpieza_y_hogar_utensilios_de_limpieza_y_calzado',
    'cuidado_facial_y_corporal_afeitado_y_cuidado_para_hombre','cuidado_facial_y_corporal_cuidado_corporal','cuidado_facial_y_corporal_cuidado_e_higiene_facial',
    'cuidado_facial_y_corporal_depilacion','cuidado_facial_y_corporal_desodorante','cuidado_facial_y_corporal_higiene_bucal',
    'cuidado_facial_y_corporal_higiene_intima','cuidado_facial_y_corporal_manicura_y_pedicura',
    'cuidado_facial_y_corporal_perfume_y_colonia','limpieza_y_hogar_insecticida_y_ambientador',
    'limpieza_y_hogar_limpieza_bano_y_wc','maquillaje_bases_de_maquillaje_y_corrector','maquillaje_ojos','mascotas_gato',
    'mascotas_perro','cuidado_del_cabello_acondicionador_y_mascarilla','cuidado_del_cabello_champu',
    'cuidado_del_cabello_fijacion_cabello','drogueria_y_limpieza_cuidado_ropa__detergente_prendas_delicadas',
    'drogueria_y_limpieza_cuidado_ropa__detergente_maquina_liquido','drogueria_y_limpieza_cuidado_ropa__suavizante_concentrado',
    'drogueria_y_limpieza_cuidado_ropa__detergente_a_mano_y_jabon_comun',
    'limpieza_y_hogar_detergente_y_suavizante_ropa','fitoterapia_y_parafarmacia_fitoterapia',
    'cuidado_facial_y_corporal_gel_y_jabon_de_manos','maquillaje_colorete_y_polvos','maquillaje_labios',
    'bebe_higiene_puericultura','bebe_higiene_toallitas','bebe_panales_pequenos_hasta_6_kg','bebe_panales_medianos_410_kg',
    'bebe_panales_grandes_915_kg','bebe_panales_de_noche_y_aprendizaje','bebe_panales_banadores',
    'perfumeria_e_higiene_afeitado_maquinillas_y_hojas_de_afeitar','perfumeria_e_higiene_afeitado_maquinillas_desechables',
    'perfumeria_e_higiene_botiquin_tiritas_protectoras','perfumeria_e_higiene_afeitado_espuma_gel_y_crema_afeitar',
    'perfumeria_e_higiene_botiquin_algodon_bastoncillos','perfumeria_e_higiene_cuidado_del_cabello_tintes_y_coloracion',
    'perfumeria_e_higiene_cuidado_del_cabello_accesorios_cabello','perfumeria_e_higiene_cuidado_corporal_protector_solar',
    'perfumeria_e_higiene_cuidado_pies_crema','perfumeria_e_higiene_depilacion_bandas',
    'perfumeria_e_higiene_depilacion_maquinillas_y_recambios','perfumeria_e_higiene_desodorante_crema_y_barra',
    'perfumeria_e_higiene_gel_de_bano_sal_y_espuma_de_bano','perfumeria_e_higiene_gel_de_bano_esponja_y_accesorios',
    'perfumeria_e_higiene_higiene_bucal_cepillos_de_dientes','perfumeria_e_higiene_higiene_bucal_seda_dental',
    'perfumeria_e_higiene_higiene_bucal_productos_protesicos','perfumeria_e_higiene_higiene_intima_compresas',
    'perfumeria_e_higiene_higiene_intima_protege_slips','perfumeria_e_higiene_higiene_intima_aseo_intimo',
    'perfumeria_e_higiene_higiene_intima_incontinencia','perfumeria_e_higiene_higiene_sexual_lubricantes',
    'perfumeria_e_higiene_higiene_sexual_preservativos','drogueria_y_limpieza_accesorios_limpieza_bayetas_y_gamuzas',
    'drogueria_y_limpieza_accesorios_limpieza_estropajos','drogueria_y_limpieza_accesorios_limpieza_fregonas',
    'drogueria_y_limpieza_accesorios_limpieza_guantes','drogueria_y_limpieza_ambientadores_electricos_y_automaticos',
    'drogueria_y_limpieza_ambientadores_antihumedad','drogueria_y_limpieza_ambientadores_para_coche_y_espacios_pequenos',
    'drogueria_y_limpieza_cerillas_y_mecheros_cerillas_y_mecheros','drogueria_y_limpieza_bolsas_basura_y_reutilizable_bolsas_y_sacos_de_basura',
    'drogueria_y_limpieza_conservacion_alimentos_bolsas_de_congelar','drogueria_y_limpieza_celulosa_papel_de_cocina',
    'drogueria_y_limpieza_celulosa_servilletas_de_papel','drogueria_y_limpieza_cuidado_ropa__complementos_aditivos_para_el_lavado',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_limpia_inodoro_wc',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_amoniaco_desinfectantes_agua_destilada',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_lejia',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_limpia_cristales',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_limpia_muebles',
    'drogueria_y_limpieza_pilas_y_bombillas_pilas','mascotas_accesorios_accesorios',
    'soy_solidario_soy_solidario_soy_solidario','perfumeria_e_higiene_cabello_cepillos_peines_y_accesorios',
    'limpieza_y_hogar_estropajo_bayeta_y_guantes','limpieza_y_hogar_limpieza_cocina',
    'limpieza_y_hogar_limpiahogar_y_friegasuelos','limpieza_y_hogar_menaje_y_conservacion_de_alimentos',
    'perfumeria_e_higiene_bano_e_higiene_corporal_colonias',
    'perfumeria_e_higiene_bano_e_higiene_corporal_esponjas_manoplas_y_cepillos_de_bano',
    'perfumeria_e_higiene_cabello_cuidado_y_tratamientos_del_cabello','perfumeria_e_higiene_cabello_acondicionadores',
    'perfumeria_e_higiene_cabello_fijadores','perfumeria_e_higiene_cuidado_y_proteccion_corporal_piel',
    'perfumeria_e_higiene_cuidado_y_proteccion_corporal_body_milk_hidratacion_bajo_la_ducha',
    'perfumeria_e_higiene_botiquin_optica',
    'perfumeria_e_higiene_cuidado_y_proteccion_corporal_limpieza_facial',
    'perfumeria_e_higiene_cuidado_y_proteccion_corporal_productos_para_viaje',
    'perfumeria_e_higiene_boca_y_sonrisa_cepillos_recambios_y_accesorios',
    'perfumeria_e_higiene_higiene_intima_tampones',
    'perfumeria_e_higiene_higiene_intima_toallitas_y_geles_intimos',
    'perfumeria_e_higiene_higiene_intima_protege_slip',
    'perfumeria_e_higiene_cuidado_facial_cremas_especificas','drogueria_y_limpieza_insecticidas_hogar_y_plantas',
    'drogueria_y_limpieza_insecticidas_antipolillas_y_carcoma','drogueria_y_limpieza_insecticidas_caminantes',
    'drogueria_y_limpieza_insecticidas_voladores','drogueria_y_limpieza_lavavajillas_complementos_lavavajillas',
    'drogueria_y_limpieza_lavavajillas_maquina_liquido__polvo','drogueria_y_limpieza_limpiadores_para_el_hogar_quitagrasas',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_limpiador_suelo_madera',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_limpiador_especifico','bebe_panales_y_toallitas_panales_carrefour_baby',
    'bebe_panales_y_toallitas_toallitas','bebe_perfumeria_e_higiene_jabon_liquido','bebe_puericultura_accesorios',
    'limpieza_y_hogar_menaje_ollas_cazos_y_accesorios','bebe_perfumeria_e_higiene_crema_corporal_talcos_y_antiirritacion',
    'bebe_perfumeria_e_higiene_bastoncillos_algodon_y_sueros','bebe_perfumeria_e_higiene_colonia',
    'limpieza_y_hogar_cuidado_de_la_ropa_detergentes','limpieza_y_hogar_cuidado_de_la_ropa_tendido_y_planchado',
    'limpieza_y_hogar_cuidado_de_la_ropa_agua_de_plancha_y_apresto',
    'limpieza_y_hogar_cuidado_de_la_ropa_toallitas_atrapacolores','limpieza_y_hogar_cuidado_de_la_ropa_tinte_para_la_ropa',
    'limpieza_y_hogar_papel_y_celulosa_servilletas','limpieza_y_hogar_papel_y_celulosa_panuelos',
    'limpieza_y_hogar_productos_para_cocina_lavavajillas_a_mano',
    'limpieza_y_hogar_productos_para_cocina_aditivos_y_limpiamaquinas','limpieza_y_hogar_productos_para_bano_wc',
    'limpieza_y_hogar_productos_para_bano_desatascadores_y_limpia_tuberias',
    'limpieza_y_hogar_productos_para_bano_limpiadores_antical_bano','limpieza_y_hogar_productos_para_bano_limpiajuntas',
    'limpieza_y_hogar_productos_para_toda_la_casa_suelos',
    'limpieza_y_hogar_productos_para_toda_la_casa_limpiacristales_y_multiusos',
    'limpieza_y_hogar_productos_para_toda_la_casa_insecticidas',
    'limpieza_y_hogar_utensilios_de_limpieza_bayetas_microfibra_atrapapolvo','limpieza_y_hogar_utensilios_de_limpieza_estropajos',
    'limpieza_y_hogar_utensilios_de_limpieza_plumeros_rodillos_y_recambios',
    'limpieza_y_hogar_conservacion_de_alimentos_papel_de_aluminio','limpieza_y_hogar_conservacion_de_alimentos_bolsas',
    'limpieza_y_hogar_ambientadores_electricos',
    'limpieza_y_hogar_ambientadores_automaticos','limpieza_y_hogar_ambientadores_coche',
    'limpieza_y_hogar_ambientadores_antihumedad','limpieza_y_hogar_ambientadores_un_toque',
    'limpieza_y_hogar_calzado_desodorantes_para_calzado','limpieza_y_hogar_calzado_plantillas_de_calzado',
    'limpieza_y_hogar_calzado_crema','limpieza_y_hogar_menaje_utensilios_de_cocina',
    'limpieza_y_hogar_menaje_jarras_y_filtros_de_agua',
    'limpieza_y_hogar_menaje_sartenes_paelleras_y_wok_fondue_parrillas_grill_accesorios',
    'limpieza_y_hogar_menaje_vajillas_y_vasos','limpieza_y_hogar_menaje_cuberteria',
    'limpieza_y_hogar_papeleria_cartuchos_de_tinta','limpieza_y_hogar_bazar_barbacoas_y_accesorios',
    'mascotas_perros_pienso_para_perros','limpieza_y_hogar_papeleria_pequeno_accesorio',
    'limpieza_y_hogar_papeleria_cuadernos_y_carpetas','limpieza_y_hogar_papeleria_accesorios_manualidades',
    'limpieza_y_hogar_papeleria_archivadores','limpieza_y_hogar_papeleria_dibujo_artistico',
    'limpieza_y_hogar_papeleria_dibujo_tecnico','limpieza_y_hogar_bazar_jardineria',
    'limpieza_y_hogar_bazar_pequeno_electrodomestico','limpieza_y_hogar_bazar_pegamentos_y_siliconas',
    'perfumeria_e_higiene_bano_e_higiene_corporal_jabon_de_manos','perfumeria_e_higiene_boca_y_sonrisa_dentifricos',
    'perfumeria_e_higiene_depilacion_y_afeitado_afeitado','perfumeria_e_higiene_cosmetica_unas',
    'perfumeria_e_higiene_depilacion_y_afeitado_after_shave','perfumeria_e_higiene_cosmetica_ojos',
    'perfumeria_e_higiene_cosmetica_accesorios_de_maquillaje_y_manicura_y_pedicura','perfumeria_e_higiene_cosmetica_labios',
    'mascotas_gatos_arena','mascotas_perros_champus_para_perro','mascotas_perros_comederos','mascotas_gatos_pienso_para_gatos',
    'mascotas_conejos_y_roedores_pienso_para_conejos_y_rodeores','mascotas_conejos_y_roedores_accesorios_e_higiene',
    'mascotas_pajaros_pienso_para_pajaros','parafarmacia_higiene_bucal_colutorio',
    'parafarmacia_higiene_bucal_frescor_y_aliento','parafarmacia_higiene_bucal_cuidado_y_fijacion_protesis_dentales',
    'parafarmacia_higiene_bucal_ortodoncia','parafarmacia_higiene_bucal_cepillos_y_seda',
    'parafarmacia_botiquin_mascarillas','parafarmacia_botiquin_higiene_y_tiras_nasales',
    'parafarmacia_botiquin_antisepticos_y_talcos','parafarmacia_botiquin_tos_y_garganta',
    'parafarmacia_botiquin_alivio_del_dolor','parafarmacia_botiquin_oido_y_protectores',
    'parafarmacia_botiquin_termometro_y_tensiometros','parafarmacia_botiquin_antimosquitos',
    'parafarmacia_cuidado_corporal_cremas_y_lociones','parafarmacia_cuidado_corporal_cuidado_intimo',
    'parafarmacia_cuidado_e_higiene_facial_cremas_faciales','parafarmacia_cuidado_e_higiene_facial_cuidado_labial',
    'parafarmacia_cuidado_e_higiene_facial_exfoliantes_y_mascarillas','parafarmacia_cuidado_e_higiene_facial_tonicos_y_lociones',
    'parafarmacia_cuidado_e_higiene_facial_maquillaje','parafarmacia_cabello_champus_anticaida',
    'parafarmacia_cabello_otros_champus_de_tratamiento','parafarmacia_cabello_antiparasitarios',
    'parafarmacia_nutricion_y_dietetica_tratamientos_naturales','parafarmacia_nutricion_y_dietetica_control_de_peso',
    'bebe_higiene_gel_y_jabon','perfumeria_e_higiene_higiene_bucal_enjuagues_y_antisepticos',
    'drogueria_y_limpieza_limpiadores_para_el_hogar_limpia_alfombras_tapicerias','cuidado_facial_y_corporal_protector_solar_y_aftersun',
    'drogueria_y_limpieza_conservacion_alimentos_papel_aluminio','drogueria_y_limpieza_conservacion_alimentos_film_transparente',
    'drogueria_y_limpieza_cuidado_ropa__detergente_maquina_tabletas','drogueria_y_limpieza_cuidado_ropa__detergente_maquina_polvo',
    'drogueria_y_limpieza_pilas_y_bombillas_bombillas','drogueria_y_limpieza_otros_articulos_bazar_filtros_cafe',
    'drogueria_y_limpieza_otros_articulos_bazar_cubiertos_vasos_y_platos_desechables','drogueria_y_limpieza_otros_articulos_bazar_otros_articulos_bazar',
    'mascotas_gatos_snacks','mascotas_gatos_arena_higiene','perfumeria_e_higiene_cosmetica_cosmetica',
    'drogueria_y_limpieza_conservacion_alimentos_bolsas_de_conservacion',
    'drogueria_y_limpieza_conservacion_alimentos_papel_horno','drogueria_y_limpieza_celulosa_panuelos_y_tissues',
    'limpieza_y_hogar_papel_higienico_y_celulosa','limpieza_y_hogar_pilas_y_bolsas_de_basura','perfumeria_e_higiene_cabello_champus','perfumeria_e_higiene_cabello_tinte','perfumeria_e_higiene_botiquin_alcohol_agua_oxigenada_y_otros',
    'perfumeria_e_higiene_cuidado_y_proteccion_corporal_pies','perfumeria_e_higiene_cuidado_facial_protector_labial','perfumeria_e_higiene_cuidado_facial_contorno_de_ojos',
    'perfumeria_e_higiene_limpieza_facial_limpieza_especificos','drogueria_y_limpieza_ambientadores_aerosol_spray','drogueria_y_limpieza_ambientadores_continuos_y_decorativos',
    'drogueria_y_limpieza_bolsas_basura_y_reutilizable_bolsas_reutilizables','parafarmacia_nutricion_y_dietetica_complementos_vitaminicos',
    'limpieza_y_hogar_utensilios_de_limpieza_fregonas','bebe_panales_y_toallitas_baberos_protegecamas_y_bolsas_para_panales','bebe_panales_y_toallitas_panales_huggies','bebe_perfumeria_e_higiene_champu',
    'bebe_puericultura_chupetes_biberones_y_tetinas','limpieza_y_hogar_cuidado_de_la_ropa_suavizantes','limpieza_y_hogar_cuidado_de_la_ropa_aditivos_y_quitamanchas',
    'limpieza_y_hogar_cuidado_de_la_ropa_limpiadores_y_antical_para_lavadora','limpieza_y_hogar_cuidado_de_la_ropa_lejias_lavadora','limpieza_y_hogar_papel_y_celulosa_papel_cocina_y_multiusos',
    'limpieza_y_hogar_papel_y_celulosa_toallitas_gafas','limpieza_y_hogar_productos_para_cocina_lavavajillas_a_maquina','limpieza_y_hogar_productos_para_cocina_quitagrasas',
    'limpieza_y_hogar_productos_para_cocina_vitroceramicas_e_induccion','limpieza_y_hogar_productos_para_cocina_limpiadores_electrodomesticos_cocina','limpieza_y_hogar_productos_para_toda_la_casa_lejias_y_amoniacos',
    'limpieza_y_hogar_productos_para_toda_la_casa_limpia_muebles','limpieza_y_hogar_productos_para_toda_la_casa_limpiador_de_alfombras_y_tapicerias','limpieza_y_hogar_productos_para_toda_la_casa_limpiametales',
    'limpieza_y_hogar_utensilios_de_limpieza_bolsas_de_basura','limpieza_y_hogar_utensilios_de_limpieza_escobas_mopas_y_recogedores','limpieza_y_hogar_utensilios_de_limpieza_guantes',
    'limpieza_y_hogar_utensilios_de_limpieza_cubos_de_basura','limpieza_y_hogar_utensilios_de_limpieza_cubos_de_fregar_y_barrenos','limpieza_y_hogar_utensilios_de_limpieza_otros_utiles',
    'limpieza_y_hogar_conservacion_de_alimentos_film_transparente','limpieza_y_hogar_conservacion_de_alimentos_papel_y_moldes_para_horno','limpieza_y_hogar_ambientadores_decorativos',
    'limpieza_y_hogar_ambientadores_aerosol_o_pistola','limpieza_y_hogar_ambientadores_absorbeolores','limpieza_y_hogar_menaje_menaje_desechable','limpieza_y_hogar_papeleria_colorear',
    'limpieza_y_hogar_papeleria_maquinaria_de_oficina','limpieza_y_hogar_menaje_ordenacion','limpieza_y_hogar_menaje_hermeticos','limpieza_y_hogar_papeleria_boligrafos_y_correctores',
    'limpieza_y_hogar_papeleria_lapices_y_accesorios','limpieza_y_hogar_papeleria_marcadores','limpieza_y_hogar_papeleria_forralibros','limpieza_y_hogar_bazar_pilas',
    'limpieza_y_hogar_bazar_bombillas_y_tubos','limpieza_y_hogar_bazar_automovil','perfumeria_e_higiene_bano_e_higiene_corporal_geles_de_bano','perfumeria_e_higiene_bano_e_higiene_corporal_desodorantes',
    'perfumeria_e_higiene_depilacion_y_afeitado_maquinillas_y_recambios','perfumeria_e_higiene_cosmetica_rostro','perfumeria_e_higiene_cosmetica_estuches_de_bano_y_cosmetica',
    'perfumeria_e_higiene_bienestar_sexual_preservativos','mascotas_perros_premios_snacks_y_huesos','mascotas_perros_confort','mascotas_perros_higiene',
    'mascotas_gatos_accesorios_e_higiene','mascotas_pajaros_accesorios_e_higiene','mascotas_peces_y_tortugas_tortugas','mascotas_peces_y_tortugas_peces','mascotas_peces_y_tortugas_accesorios_peces_y_tortugas',
    'parafarmacia_bebe_anti_irritacion','parafarmacia_bebe_hidratantes_y_aceites_corporales','parafarmacia_bebe_toallitas_bebe','parafarmacia_higiene_bucal_pasta_de_dientes','parafarmacia_botiquin_geles_hidroalcoholicos',
    'parafarmacia_botiquin_apositos_y_gasas','parafarmacia_cuidado_corporal_jabones_y_geles','parafarmacia_cuidado_e_higiene_facial_desmaquillantes','parafarmacia_cuidado_e_higiene_facial_cuidado_acne',
    'parafarmacia_cuidado_de_manos_y_pies_crema_de_manos','parafarmacia_cuidado_de_manos_y_pies_desodorante_pies','parafarmacia_cuidado_de_manos_y_pies_apositos_y_plantillas','charcuteria_y_quesos_pates_foie_y_untables_foie','charcuteria_y_quesos_pates_foie_y_untables_sobrasada'] #categorias que no son alimentos y queremos eliminar de nuestro dataset

    food = food[~food.category.str.contains('|'.join(blacklist))]
    food = food.drop(columns = ['product_id'])
    food = food.rename(columns = {'insert_date' : 'date'})
    food['date'] = food['date'].astype('datetime64[ns]')
    food.loc[food.description=="Granel","price"]= food.reference_price
    #select todays date and substract one day from it
    food[food.date ==(pd.to_datetime('today')-timedelta(days=1)).strftime('%Y-%m-%d')]
    

    food=food.replace('ñ','-&-', regex=True)
    cols = food.select_dtypes(include=[np.object]).columns
    food[cols] = food[cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    food = food.replace('-&-','ñ', regex=True)
    
    return food
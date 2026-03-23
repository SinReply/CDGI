# CDGI

Calcula y analiza daños en combate con este sistema de Python.  
Incluye la gestión de ataques, defensas y resistencias de enemigos y personajes, con soporte para estadísticas elementales (bonos, reacciones, maestría, etc.).

## Archivos principales

- [`Damage.py`](./Damage.py) → Código fuente principal y punto de entrada del programa.

## Cómo usar

1. Asegúrate de tener **Python 3.8+** instalado.
2. Descarga o clona el repositorio:

```bash
git clone https://github.com/tu-usuario/CDGI.git
cd CDGI
```

3. (Opcional) Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows
```
4. Instala las dependencias:

```bash
pip install colorama keyboard
```

5. Ejecuta el programa:

```bash
python Damage.py
```

El programa te irá pidiendo por consola los valores necesarios (ataque base, nivel, resistencias, bonos elementales, críticos, etc.) y mostrará los cálculos de daño paso a paso.

## Estructura de datos

El programa guarda y carga automáticamente la información en la carpeta `Data/` con esta organización:

Data/

├── Attacks/

├── Levels/

├── General_Stats/

├── Defenses/

├── Resistances/

└── Elemental_Stats/


## Cómo funciona (resumen)

- Permite ingresar y guardar estadísticas de forma persistente (pickle).
- Calcula daño base → daño con bonos → daño tras defensa → daño final tras resistencias.
- Soporta modificadores elementales, críticos, reacciones y multiplicadores complejos.
- Interfaz por consola con colores (colorama) y control de teclas (keyboard).

## Licencia

**Copyright © 2023-2026 No-Reply**  
Todos los derechos reservados.

Este software está protegido por la Ley de Propiedad Intelectual de España (Real Decreto Legislativo 1/1996, de 12 de abril).  

- Uso **personal y privado** permitido.  
- Prohibida la redistribución, modificación, publicación, venta o uso comercial sin autorización expresa por escrito del autor.  
- Para cualquier consulta o permiso contactar al autor.

Ver encabezado de [`Damage.py`](./Damage.py) ó [`LICENCIA.md`](./LICENSE.md) para más detalles legales.

## Requisitos

- Python 3.8 o superior
- Librerías:
  - colorama
  - keyboard
  - pickle (viene con Python)

## Autor

**No-Reply**  
2026

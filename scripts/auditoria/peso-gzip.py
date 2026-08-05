import gzip, glob, os
def gz(p):
    return len(gzip.compress(open(p, 'rb').read(), 6))
for p in ['dist/index.html',
          'dist/productos/deteccion-y-alarma/index.html',
          'dist/directorio/puebla/estacion-libres/index.html']:
    print('  %-46s %7.1f KB   gz %6.1f KB' % (p.replace('dist/', ''),
          os.path.getsize(p) / 1024, gz(p) / 1024))
fs = glob.glob('dist/**/*.html', recursive=True)
print('  TOTAL %d paginas: %.2f MB   gz %.2f MB'
      % (len(fs), sum(os.path.getsize(f) for f in fs) / 1e6, sum(gz(f) for f in fs) / 1e6))

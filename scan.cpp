#include <QTextStream>
#include <QDir>
#include <QDirIterator>

QTextStream out(stdout);

void scanDir(QDir dir)
{
  QDirIterator iterator(dir.absolutePath(), QDirIterator::Subdirectories);
  out << "CREATE TABLE idx (DIR, FILE);\n";
  while (iterator.hasNext()) {
    iterator.next();
    out << "INSERT INTO idx VALUES ('" << dir.absolutePath() << "', '"
        << iterator.fileInfo().absoluteFilePath() << "');\n";
  }
}

int main(int argc, char *argv[])
{
  QDir dir(argv[1]);
  scanDir(dir);
  
  return 0;
}

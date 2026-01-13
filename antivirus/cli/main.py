from antivirus.core.scanner import FileScanner

def start():
    print("=" * 50)
    print("        Projeto Anti-Vírus (CLI)")
    print("=" * 50)

    scanner = FileScanner()

    path = input("\nInforme o caminho do arquivo ou pasta para escanear: ").strip()

    print("\nIniciando varredura...\n")
    scanner.scan_path(path)

    summary = scanner.summary()

    print("\n===== RESULTADO =====")
    print(f"Arquivos escaneados : {summary['scanned']}")
    print(f"Ameaças detectadas  : {summary['infected']}")

    if summary["infected"] > 0:
        print("\nDetalhes:")
        for item in summary["details"]:
            print(f" - {item['file']} | {item['threat']}")

    input("\nPressione ENTER para sair...")

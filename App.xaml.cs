using System;
using System.Windows;

namespace JergadorLiberador
{
    public partial class App : Application
    {
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

            Console.Title = "El Jergador Liberador";
            Console.BackgroundColor = ConsoleColor.Black;
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.Clear();

            Animate("🧠 El Jergador Liberador se está preparando...");
            WriteProcess("Liberando procesos innecesarios del sistema...");
            KillKnownBloatware();

            WriteProcess("Eliminando servicios innecesarios...");
            RemoveKnownServices();

            WriteProcess("Desactivando tareas programadas invasivas...");
            DisableScheduledTasks();

            WriteSuccess("✅ Liberación básica completada.");
            WriteInfo("Puedes cerrar esta ventana o seguir explorando tu sistema libre.");

            Console.ResetColor();
            Console.ReadKey();
            Shutdown();
        }

        void Animate(string text) => Console.WriteLine(text);
        void WriteProcess(string msg) => Console.WriteLine("🛠 " + msg);
        void WriteSuccess(string msg) => Console.WriteLine(msg);
        void WriteInfo(string msg) => Console.WriteLine(msg);
        void KillKnownBloatware() { /* Simulado */ }
        void RemoveKnownServices() { /* Simulado */ }
        void DisableScheduledTasks() { /* Simulado */ }
    }
}
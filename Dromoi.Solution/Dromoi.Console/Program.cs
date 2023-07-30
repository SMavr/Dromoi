// See https://aka.ms/new-console-template for more information

using Dromoi.Infrastructure;

AudioRecorder audioRecorder = new AudioRecorder();
audioRecorder.Start();

Console.WriteLine("C# Audio Level Meter");
Console.WriteLine("(press any key to exit)");
Console.ReadKey();

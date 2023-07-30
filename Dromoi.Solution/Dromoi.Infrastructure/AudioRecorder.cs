using NAudio.Wave;

namespace Dromoi.Infrastructure;
public class AudioRecorder
{

    public void Start()
    {
        var waveIn = new WaveInEvent
        {
            DeviceNumber = 0, // indicates which microphone to use
            WaveFormat = new NAudio.Wave.WaveFormat(rate: 44100, bits: 16, channels: 1),
            BufferMilliseconds = 20
        };
        waveIn.DataAvailable += WaveIn_DataAvailable;
        waveIn.StartRecording();
    }

    private static void WaveIn_DataAvailable(object? sender, WaveInEventArgs e)
    {
        // copy buffer into an array of integers
        short[] values = new short[e.Buffer.Length / 2];
        Buffer.BlockCopy(e.Buffer, 0, values, 0, e.Buffer.Length);

        // determine the highest value as a fraction of the maximum possible value
        float fraction = (float)values.Max() / 32768;

        // print a level meter using the console
        string bar = new('#', (int)(fraction * 70));
        string meter = "[" + bar.PadRight(60, '-') + "]";
        Console.CursorLeft = 0;
        Console.CursorVisible = false;
        Console.Write($"{meter} {fraction * 100:00.0}%");
    }
}
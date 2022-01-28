using System;
using System.Diagnostics;
using System.IO;
using Lusid.Sdk.Model;
using Newtonsoft.Json;
using NUnit.Framework;

namespace OpenAPIPerf
{
    public class Tests
    {

        [Test]
        public void Deserialize()
        {
            using var file = File.OpenText("response.json");
            var serializer = new JsonSerializer();
            var stopwatch = Stopwatch.StartNew();
            
            var response = serializer.Deserialize(file, typeof(VersionedResourceListOfTransaction)) as VersionedResourceListOfTransaction;
            
            stopwatch.Stop();
            
            Console.WriteLine($"deserialized in {stopwatch.ElapsedMilliseconds} ms");
            
            Assert.That(response, Is.Not.Null);
            Assert.That(response.Values.Count, Is.EqualTo(5000));
        }
    }
}
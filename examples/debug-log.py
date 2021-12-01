"""
This example demonstrate how debug-log works

"""
from juju import jasyncio
from juju.model import Model


async def main():
    model = Model()
    await model.connect_current()

    await model.debug_log(limit=3)

    application = await model.deploy(
        'cs:ubuntu-10',
        application_name='ubuntu',
        series='trusty',
        channel='stable',
    )

    await model.wait_for_idle(status='active')

    await application.remove()
    await model.disconnect()


if __name__ == '__main__':
    jasyncio.run(main())
